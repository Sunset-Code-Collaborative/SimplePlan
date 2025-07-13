# SimplePlan MCP Usage Examples

🎯 **Real-world examples of AI using SimplePlan MCP tools**

## 🚀 Scenario 1: New Project Creation

**Human:** "I want to build a personal finance tracker web app"

**AI Response using SimplePlan MCP:**

```python
# Step 1: Create the project
create_project_plan(
    name="Personal Finance Tracker",
    description="Full-stack web application for tracking personal expenses and income",
    initiator="User"
)

# Step 2: Add foundation steps
add_project_step(
    description="Set up development environment and project structure",
    step_type="setup",
    assigned_to="Developer"
)

add_project_step(
    description="Design database schema for transactions and categories",
    step_type="development",
    dependencies=["STEP-001"]
)

add_project_step(
    description="Create REST API endpoints for CRUD operations",
    step_type="development",
    dependencies=["STEP-002"]
)

add_project_step(
    description="Build React frontend components",
    step_type="development",
    dependencies=["STEP-001"]
)

add_project_step(
    description="Implement user authentication system",
    step_type="development",
    dependencies=["STEP-003", "STEP-004"]
)

add_project_step(
    description="Write unit and integration tests",
    step_type="testing",
    dependencies=["STEP-003", "STEP-004", "STEP-005"]
)

add_project_step(
    description="Deploy to production environment",
    step_type="deployment",
    dependencies=["STEP-006"]
)

# Step 3: Show the plan
get_project_status()
```

**Result:** Complete project plan with 7 steps, proper dependencies, and 0% completion.

---

## 📊 Scenario 2: Progress Tracking

**Human:** "I finished setting up the development environment"

**AI Response:**

```python
# Check what's available to complete
get_next_steps()
# Returns: STEP-001 (Set up development environment)

# Mark it complete
complete_step(step_id="STEP-001")

# Check new status
get_project_status()
# Returns: 1/7 steps complete (14.3%)

# Show what's now available
get_next_steps()
# Returns: STEP-002 (Design database schema) and STEP-004 (Build React frontend)
```

**AI:** "Great! I've marked the environment setup as complete. You can now work on either the database schema design or the React frontend components, since they both have their dependencies satisfied."

---

## 🔍 Scenario 3: Project Health Check

**Human:** "Something seems off with my project plan"

**AI Response:**

```python
# First, validate the project structure
validate_project_plan()
# Returns: {
#   "success": true,
#   "is_valid": false,
#   "errors": [
#     "Step STEP-005 depends on STEP-999 which does not exist",
#     "Circular dependency detected: STEP-003 → STEP-004 → STEP-003"
#   ]
# }

# Get full project overview
list_all_steps(show_completed=true)

# Check current status for context
get_project_status()
```

**AI:** "I found 2 issues with your project plan:
1. STEP-005 references a non-existent step (STEP-999)
2. There's a circular dependency between STEP-003 and STEP-004

Let me help you fix these issues..."

---

## 🎯 Scenario 4: Sprint Planning

**Human:** "What should I work on next this week?"

**AI Response:**

```python
# Check available work
get_next_steps()
# Returns available steps with no blocking dependencies

# Get full context
get_project_status()
# Shows: 3/10 steps complete (30%)

# Review all remaining work
list_all_steps(show_completed=false)
# Shows only incomplete steps
```

**AI:** "Based on your current progress (30% complete), here are your best options for this week:

**High Priority:**
- STEP-004: Create REST API endpoints (depends on completed database schema)
- STEP-005: Build React frontend components (no dependencies)

**Medium Priority:**
- STEP-007: Implement authentication (waiting for API and frontend)

I recommend focusing on STEP-004 and STEP-005 since they can be done in parallel and will unblock STEP-007."

---

## 🔄 Scenario 5: Multi-Project Management

**AI managing multiple projects:**

```python
# Check web app project
get_project_status(project_file="finance_tracker.json")

# Check mobile app project
get_project_status(project_file="mobile_app.json")

# Add cross-project dependency
add_project_step(
    description="Integrate with web app API",
    step_type="development",
    project_file="mobile_app.json",
    dependencies=["STEP-003"]  # From finance_tracker.json
)
```

**AI:** "I'm tracking 2 related projects:
- Finance Tracker Web App: 60% complete
- Mobile App: 25% complete

The mobile app is waiting for the web API to be finished before it can integrate. Let me prioritize the web app API completion..."

---

## 🚨 Scenario 6: Crisis Management

**Human:** "The client changed requirements completely!"

**AI Response:**

```python
# First, assess current state
get_project_status()
list_all_steps(show_completed=true)

# Add new requirements as steps
add_project_step(
    description="Redesign UI for new user workflow",
    step_type="design",
    assigned_to="Design Team"
)

add_project_step(
    description="Refactor API to support new data structure",
    step_type="development",
    dependencies=["STEP-NEW-001"]
)

# Validate the updated plan
validate_project_plan()
```

**AI:** "I understand the requirements changed. I've added the new design and refactoring steps to your plan. The good news is that 40% of your existing work (database setup, testing framework, deployment pipeline) can still be reused. Here's the updated timeline..."

---

## 📈 Scenario 7: Team Coordination

**AI coordinating team work:**

```python
# Check what each team member can work on
get_next_steps()

# Assign specific steps
add_project_step(
    description="Implement payment processing integration",
    step_type="development",
    assigned_to="Backend Team",
    dependencies=["STEP-003"]
)

add_project_step(
    description="Create responsive dashboard layout",
    step_type="development",
    assigned_to="Frontend Team",
    dependencies=["STEP-002"]
)

# Track overall progress
get_project_status()
```

**AI:** "Team assignments updated:
- **Backend Team**: Payment processing (can start immediately)
- **Frontend Team**: Dashboard layout (can start immediately)
- **QA Team**: Ready to test user authentication (STEP-005 complete)

All teams can work in parallel right now. Next bottleneck will be in 3 days when integration testing begins."

---

## 🎓 Learning from Examples

### Key Patterns

1. **Status First**: Always check `get_project_status()` to understand context
2. **Dependency Awareness**: Use `get_next_steps()` to find available work
3. **Validation**: Regular `validate_project_plan()` to catch issues early
4. **Progress Tracking**: Mark steps complete as work finishes
5. **Team Coordination**: Use `assigned_to` and dependencies for collaboration

### AI Best Practices

- **Proactive**: Check project health without being asked
- **Contextual**: Consider project phase and team capacity
- **Helpful**: Suggest next steps and priorities
- **Preventive**: Catch dependency issues before they block work
- **Adaptive**: Handle changing requirements gracefully

### User Benefits

- **Real-time Updates**: AI tracks progress automatically
- **Smart Suggestions**: AI recommends optimal next steps
- **Error Prevention**: AI catches planning mistakes early
- **Team Coordination**: AI facilitates multi-person projects
- **Requirement Changes**: AI helps adapt to new requirements

---

**🎯 These examples show how SimplePlan MCP transforms AI from a passive advisor to an active project management partner!**
