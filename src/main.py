from pathlib import Path
import json

# Create the project_plan_io.py module
project_plan_io_code = """
import json
from pathlib import Path
from typing import Dict, Any

PLAN_PATH = Path("project_plan.json")

def save_project_plan(plan: Dict[str, Any], path: Path = PLAN_PATH):
    path.write_text(json.dumps(plan, indent=2))

def load_project_plan(path: Path = PLAN_PATH) -> Dict[str, Any]:
    return json.loads(path.read_text())

def get_status_summary(path: Path = PLAN_PATH) -> str:
    plan = load_project_plan(path)
    steps = plan.get("steps", [])
    total = len(steps)
    complete = sum(1 for step in steps if step.get("complete"))
    return f"{complete}/{total} steps complete"

def mark_step_complete(step_id: str, path: Path = PLAN_PATH):
    plan = load_project_plan(path)
    for step in plan["steps"]:
        if step["id"] == step_id:
            step["complete"] = True
    save_project_plan(plan, path)
"""

project_plan_json = {
    "project_id": "abc123",
    "name": "Refactor Authentication System",
    "created_at": "2025-07-04T12:00:00Z",
    "steps": [
        {
            "id": "STEP-001",
            "description": "Extract logic to service object",
            "complete": False,
            "dependencies": [],
            "assigned_to": "AI",
            "step_type": "refactor",
            "metadata": {}
        },
        {
            "id": "STEP-002",
            "description": "Write tests for service object",
            "complete": False,
            "dependencies": ["STEP-001"],
            "assigned_to": "AI",
            "step_type": "testing",
            "metadata": {}
        }
    ],
    "metadata": {
        "initiator": "bjorn",
        "ai_generated": True
    }
}

# Save the files
project_plan_io_path = Path("/mnt/data/project_plan_io.py")
project_plan_json_path = Path("/mnt/data/project_plan.json")

project_plan_io_path.write_text(project_plan_io_code.strip())
project_plan_json_path.write_text(json.dumps(project_plan_json, indent=2))

project_plan_io_path, project_plan_json_path
