"""Tests for SimplePlan core functionality."""

import json
import pytest
from pathlib import Path
from datetime import datetime
import tempfile
import os

from src.simpleplan.models import ProjectPlan, ProjectStep, ProjectMetadata
from src.simpleplan.project_plan_io import ProjectPlanIO, ProjectPlanError, ProjectPlanNotFoundError


class TestProjectPlanModels:
    """Test the Pydantic models."""
    
    def test_project_step_creation(self):
        """Test creating a ProjectStep."""
        step = ProjectStep(
            id="STEP-001",
            description="Test step",
            step_type="task"
        )
        
        assert step.id == "STEP-001"
        assert step.description == "Test step"
        assert step.complete is False
        assert step.step_type == "task"
        assert step.dependencies == []
        assert step.assigned_to == "AI"
    
    def test_project_plan_creation(self):
        """Test creating a ProjectPlan."""
        metadata = ProjectMetadata(initiator="test_user")
        plan = ProjectPlan(
            project_id="test123",
            name="Test Project",
            metadata=metadata
        )
        
        assert plan.project_id == "test123"
        assert plan.name == "Test Project"
        assert plan.metadata.initiator == "test_user"
        assert plan.steps == []
        assert plan.get_completion_percentage() == 0.0
    
    def test_project_plan_completion_percentage(self):
        """Test completion percentage calculation."""
        metadata = ProjectMetadata(initiator="test_user")
        step1 = ProjectStep(id="STEP-001", description="Step 1", complete=True)
        step2 = ProjectStep(id="STEP-002", description="Step 2", complete=False)
        step3 = ProjectStep(id="STEP-003", description="Step 3", complete=True)
        
        plan = ProjectPlan(
            project_id="test123",
            name="Test Project",
            metadata=metadata,
            steps=[step1, step2, step3]
        )
        
        assert abs(plan.get_completion_percentage() - 66.67) < 0.1  # 2/3 * 100, approximately
    
    def test_next_available_steps(self):
        """Test getting next available steps based on dependencies."""
        metadata = ProjectMetadata(initiator="test_user")
        step1 = ProjectStep(id="STEP-001", description="Step 1", complete=True)
        step2 = ProjectStep(id="STEP-002", description="Step 2", complete=False, dependencies=["STEP-001"])
        step3 = ProjectStep(id="STEP-003", description="Step 3", complete=False, dependencies=["STEP-002"])
        step4 = ProjectStep(id="STEP-004", description="Step 4", complete=False)
        
        plan = ProjectPlan(
            project_id="test123",
            name="Test Project",
            metadata=metadata,
            steps=[step1, step2, step3, step4]
        )
        
        next_steps = plan.get_next_available_steps()
        next_step_ids = [step.id for step in next_steps]
        
        assert "STEP-002" in next_step_ids  # Dependencies satisfied
        assert "STEP-004" in next_step_ids  # No dependencies
        assert "STEP-003" not in next_step_ids  # Dependencies not satisfied
    
    def test_dependency_validation(self):
        """Test dependency validation."""
        metadata = ProjectMetadata(initiator="test_user")
        step1 = ProjectStep(id="STEP-001", description="Step 1", dependencies=["STEP-999"])  # Non-existent
        step2 = ProjectStep(id="STEP-002", description="Step 2", dependencies=["STEP-001"])  # Valid
        
        plan = ProjectPlan(
            project_id="test123",
            name="Test Project",
            metadata=metadata,
            steps=[step1, step2]
        )
        
        errors = plan.validate_dependencies()
        assert len(errors) == 1
        assert "STEP-001 depends on non-existent step STEP-999" in errors[0]


class TestProjectPlanIO:
    """Test the ProjectPlanIO class."""
    
    def setup_method(self):
        """Set up test environment."""
        # Create a temporary directory for tests
        self.test_dir = tempfile.mkdtemp()
        self.test_file = Path(self.test_dir) / "test_project_plan.json"
        self.io = ProjectPlanIO()
    
    def teardown_method(self):
        """Clean up test environment."""
        # Clean up temporary files
        if self.test_file.exists():
            self.test_file.unlink()
        os.rmdir(self.test_dir)
    
    def test_create_project_plan(self):
        """Test creating a new project plan."""
        plan = self.io.create_project_plan(
            name="Test Project",
            description="A test project",
            initiator="test_user",
            path=self.test_file
        )
        
        assert plan.name == "Test Project"
        assert plan.description == "A test project"
        assert plan.metadata.initiator == "test_user"
        assert self.test_file.exists()
    
    def test_save_and_load_project_plan(self):
        """Test saving and loading a project plan."""
        # Create a plan
        metadata = ProjectMetadata(initiator="test_user")
        step = ProjectStep(id="STEP-001", description="Test step")
        plan = ProjectPlan(
            project_id="test123",
            name="Test Project",
            metadata=metadata,
            steps=[step]
        )
        
        # Save the plan
        self.io.save_project_plan(plan, self.test_file)
        assert self.test_file.exists()
        
        # Load the plan
        loaded_plan = self.io.load_project_plan(self.test_file)
        assert loaded_plan.name == "Test Project"
        assert loaded_plan.project_id == "test123"
        assert len(loaded_plan.steps) == 1
        assert loaded_plan.steps[0].id == "STEP-001"
    
    def test_load_nonexistent_file(self):
        """Test loading a non-existent file."""
        non_existent = Path(self.test_dir) / "nonexistent.json"
        
        with pytest.raises(ProjectPlanNotFoundError):
            self.io.load_project_plan(non_existent)
    
    def test_mark_step_complete(self):
        """Test marking a step as complete."""
        # Create a plan with steps
        plan = self.io.create_project_plan(
            name="Test Project",
            initiator="test_user",
            path=self.test_file
        )
        
        # Add a step
        step_id = self.io.add_step(
            description="Test step",
            path=self.test_file
        )
        
        # Mark step as complete
        success = self.io.mark_step_complete(step_id, self.test_file)
        assert success
        
        # Verify it's marked as complete
        loaded_plan = self.io.load_project_plan(self.test_file)
        completed_step = next(step for step in loaded_plan.steps if step.id == step_id)
        assert completed_step.complete is True
        assert completed_step.completed_at is not None
    
    def test_mark_step_complete_with_dependencies(self):
        """Test marking a step complete that has dependencies."""
        # Create a plan
        plan = self.io.create_project_plan(
            name="Test Project",
            initiator="test_user",
            path=self.test_file
        )
        
        # Add steps with dependencies
        step1_id = self.io.add_step(
            description="First step",
            path=self.test_file
        )
        step2_id = self.io.add_step(
            description="Second step",
            dependencies=[step1_id],
            path=self.test_file
        )
        
        # Try to complete step2 before step1 - should fail
        success = self.io.mark_step_complete(step2_id, self.test_file)
        assert success is False
        
        # Complete step1 first
        success = self.io.mark_step_complete(step1_id, self.test_file)
        assert success is True
        
        # Now complete step2 - should succeed
        success = self.io.mark_step_complete(step2_id, self.test_file)
        assert success is True
    
    def test_get_status_summary(self):
        """Test getting status summary."""
        # Create a plan
        plan = self.io.create_project_plan(
            name="Test Project",
            initiator="test_user",
            path=self.test_file
        )
        
        # Add steps
        step1_id = self.io.add_step(description="Step 1", path=self.test_file)
        step2_id = self.io.add_step(description="Step 2", path=self.test_file)
        
        # Initial status
        summary = self.io.get_status_summary(self.test_file)
        assert "0/2 steps complete (0.0%)" in summary
        
        # Complete one step
        self.io.mark_step_complete(step1_id, self.test_file)
        summary = self.io.get_status_summary(self.test_file)
        assert "1/2 steps complete (50.0%)" in summary
    
    def test_add_step(self):
        """Test adding a new step."""
        # Create a plan
        plan = self.io.create_project_plan(
            name="Test Project",
            initiator="test_user",
            path=self.test_file
        )
        
        # Add a step
        step_id = self.io.add_step(
            description="New step",
            step_type="testing",
            assigned_to="human",
            path=self.test_file
        )
        
        assert step_id is not None
        assert step_id.startswith("STEP-")
        
        # Verify step was added
        loaded_plan = self.io.load_project_plan(self.test_file)
        assert len(loaded_plan.steps) == 1
        
        added_step = loaded_plan.steps[0]
        assert added_step.id == step_id
        assert added_step.description == "New step"
        assert added_step.step_type == "testing"
        assert added_step.assigned_to == "human"
