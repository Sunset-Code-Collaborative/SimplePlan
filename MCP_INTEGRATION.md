# SimplePlan MCP Integration Guide

🎯 **Transform AI project management from suggestions to real-time control**

## 📋 Overview

SimplePlan's Model Context Protocol (MCP) integration enables any AI system to directly manage project plans through Claude Desktop and other MCP-compatible hosts. No more manual CLI commands - AI can create, modify, and track project progress in real-time.

### 🔄 Before vs After MCP Integration

**Before (CLI Only):**
- AI: "You should run `simpleplan add 'Implement feature X'`"
- User: *manually runs command*
- AI: "Now check status with `simpleplan status`"
- User: *manually runs command*

**After (MCP Integration):**
- AI: *directly creates project steps, checks status, manages dependencies*
- User: *sees real-time updates and progress*
- AI: *can autonomously manage entire project workflows*

## 🚀 Quick Start

### Prerequisites
- Claude Desktop installed
- Python 3.11+ with Poetry
- SimplePlan project cloned

### 1. Install SimplePlan with MCP Support

```bash
git clone <your-repo>
cd SimplePlan
poetry install
```

### 2. Configure Claude Desktop

Create or update `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "simpleplan": {
      "command": "/Users/YOUR_USERNAME/Library/Caches/pypoetry/virtualenvs/simpleplan-HASH-py3.12/bin/python",
      "args": ["/path/to/SimplePlan/mcp_server_robust.py"],
      "cwd": "/path/to/SimplePlan",
      "env": {}
    }
  }
}
```

**Find your Poetry virtualenv path:**
```bash
poetry env info --path
```

### 3. Restart Claude Desktop

Completely quit and restart Claude Desktop to load the MCP server.

### 4. Test Integration

Ask Claude: "Can you check my project status using SimplePlan?"

If working, you'll see Claude directly accessing your project data! 🎉

## 🛠️ Available MCP Tools

SimplePlan provides 7 powerful MCP tools for AI project management:

### 1. `create_project_plan`
**Purpose:** Create new project plans
**Parameters:**
- `name` (required): Project name
- `description` (optional): Project description 
- `initiator` (optional): Who started the project (defaults to "AI")
- `project_file` (optional): Custom file path

**Example AI Usage:**
```
AI: I'll create a new project plan for your web app.
Result: Creates project with ID and returns confirmation
```

### 2. `get_project_status`
**Purpose:** Check project completion and progress
**Parameters:**
- `project_file` (optional): Specific project file path

**Example Response:**
```json
{
  "success": true,
  "project_name": "SimplePlan Development",
  "completion_percentage": 88.9,
  "completed_steps": 8,
  "total_steps": 9,
  "status_summary": "8/9 steps complete (88.9%)"
}
```

### 3. `add_project_step`
**Purpose:** Add new steps to project plan
**Parameters:**
- `description` (required): What this step accomplishes
- `step_type` (optional): Type of work (development, testing, documentation, etc.)
- `dependencies` (optional): List of step IDs that must complete first
- `assigned_to` (optional): Who will complete this step

**Example AI Usage:**
```
AI: I'll add a step to implement user authentication.
Parameters: {
  "description": "Implement JWT-based user authentication system",
  "step_type": "development", 
  "dependencies": ["STEP-002"],
  "assigned_to": "Backend Team"
}
```

### 4. `complete_step`
**Purpose:** Mark steps as complete with dependency validation
**Parameters:**
- `step_id` (required): Step ID like "STEP-001"
- `project_file` (optional): Specific project file

**Example AI Usage:**
```
AI: I see you've finished the database setup. Let me mark STEP-003 as complete.
Result: Validates dependencies and marks step complete
```

### 5. `get_next_steps`
**Purpose:** Find available work (dependencies satisfied)
**Parameters:**
- `project_file` (optional): Specific project file

**Example Response:**
```json
{
  "success": true,
  "available_steps": [
    {
      "id": "STEP-005",
      "description": "Create user registration API",
      "step_type": "development",
      "assigned_to": "AI"
    }
  ],
  "count": 1
}
```

### 6. `list_all_steps`
**Purpose:** Show all project steps and status
**Parameters:**
- `show_completed` (optional): Include completed steps (default: true)
- `project_file` (optional): Specific project file

**Perfect for AI to understand full project scope**

### 7. `validate_project_plan`
**Purpose:** Check for dependency errors and issues
**Parameters:**
- `project_file` (optional): Specific project file

**Example Response:**
```json
{
  "success": true,
  "is_valid": false,
  "errors": [
    "Step STEP-005 depends on non-existent step STEP-999"
  ],
  "error_count": 1
}
```

## 💡 Real-World Usage Examples

### Example 1: AI Project Setup
```
Human: "Help me set up a new React app project"

AI Actions:
1. create_project_plan(name="React Todo App", description="Modern todo app with React and Node.js")
2. add_project_step(description="Set up React project structure", step_type="setup")
3. add_project_step(description="Create component hierarchy", step_type="development", dependencies=["STEP-001"])
4. add_project_step(description="Implement API endpoints", step_type="development")
5. get_project_status() → Shows 0/3 steps complete

Result: Complete project plan created and ready to execute
```

### Example 2: AI Progress Tracking
```
Human: "I finished setting up the React project"

AI Actions:
1. get_next_steps() → Finds "Set up React project structure" 
2. complete_step(step_id="STEP-001")
3. get_next_steps() → Now shows "Create component hierarchy" available
4. get_project_status() → Shows 1/3 steps complete (33.3%)

Result: AI tracks progress and knows what's available to work on next
```

### Example 3: AI Quality Assurance
```
Human: "Something seems wrong with my project plan"

AI Actions:
1. validate_project_plan() → Finds dependency errors
2. list_all_steps() → Reviews all steps for logical flow
3. AI suggests fixes based on validation results

Result: AI proactively identifies and helps fix project issues
```

## 🏗️ Architecture Overview

### MCP Integration Flow
```
Claude Desktop (Host) 
    ↓ JSON-RPC 2.0 via stdio
SimplePlan MCP Server (FastMCP)
    ↓ Function calls
SimplePlan Core (project_plan_io.py)
    ↓ File operations  
Project Plan JSON Files
```

### Key Components
- **`mcp_server_robust.py`**: Entry point with environment setup
- **`src/simpleplan/mcp_server.py`**: FastMCP server with 7 tools
- **`src/simpleplan/project_plan_io.py`**: Core project management logic
- **`src/simpleplan/models.py`**: Pydantic data models

### MCP Compliance
✅ **Client-Server Architecture**: Claude Desktop ↔ SimplePlan
✅ **Stdio Transport**: Local process communication
✅ **JSON-RPC 2.0**: Standard MCP messaging
✅ **Tool Registration**: All 7 tools properly exposed
✅ **Error Handling**: Graceful error responses
✅ **Schema Validation**: Input/output type safety

## 🔧 Troubleshooting

### Server Connection Issues

**Problem:** "Server disconnected" in Claude Desktop
**Solution:**
1. Check Python path in config: `poetry env info --path`
2. Use absolute paths for all file references
3. Restart Claude Desktop completely
4. Check logs: `~/Library/Logs/Claude/mcp*.log`

**Problem:** "File not found" errors  
**Solution:**
```bash
# Test server manually
cd SimplePlan
poetry run python mcp_server_robust.py
# Should show FastMCP startup banner
```

### Tool Not Available

**Problem:** SimplePlan tools don't appear in Claude
**Solution:**
1. Verify config file location: `~/Library/Application Support/Claude/claude_desktop_config.json`
2. Check JSON syntax with `json` validator
3. Ensure Poetry environment is activated
4. Restart Claude Desktop

### Permission Issues

**Problem:** Cannot read/write project files
**Solution:**
1. Check working directory: `"cwd": "/path/to/SimplePlan"`
2. Verify file permissions: `ls -la project_plan.json`
3. Ensure SimplePlan directory is writable

### Debugging Commands

```bash
# Test MCP server directly
poetry run python mcp_server_robust.py

# Check Poetry environment
poetry env info

# Validate project plan
poetry run simpleplan validate

# Monitor logs in real-time
tail -f ~/Library/Logs/Claude/mcp*.log
```

## 🎯 Integration Best Practices

### For AI Systems
1. **Always check status first** with `get_project_status()`
2. **Validate dependencies** before adding steps
3. **Use meaningful step descriptions** for clarity
4. **Check for errors** with `validate_project_plan()`
5. **Track progress** with regular status updates

### For Developers
1. **Use descriptive step types** (development, testing, documentation, etc.)
2. **Set clear dependencies** to maintain logical flow
3. **Assign ownership** with `assigned_to` parameter
4. **Regular validation** to catch issues early
5. **Backup project files** before major changes

### For Teams
1. **Consistent naming** conventions for projects
2. **Clear step descriptions** that anyone can understand
3. **Proper dependency mapping** for parallel work
4. **Regular progress reviews** using status tools
5. **Document decisions** in step descriptions

## 🚀 Advanced Usage

### Multiple Project Files
```python
# Work with specific project files
get_project_status(project_file="/path/to/other_project.json")
add_project_step(description="New feature", project_file="/path/to/other_project.json")
```

### Batch Operations
AI can chain multiple operations:
1. Create project plan
2. Add multiple steps with dependencies  
3. Validate the complete plan
4. Show next available work

### Integration with Other Tools
SimplePlan MCP can work alongside other MCP servers:
- File management servers
- Database servers  
- API testing servers
- Documentation generators

## 📊 Success Metrics

### Integration Health
- ✅ All 7 tools respond correctly
- ✅ Schema validation passes
- ✅ No connection errors in logs
- ✅ Real-time project updates work

### AI Effectiveness  
- 🎯 AI can create complete project plans
- 🎯 AI tracks progress automatically
- 🎯 AI suggests next steps intelligently
- 🎯 AI catches and fixes planning errors

### User Experience
- 🚀 No manual CLI commands needed
- 🚀 Real-time project visibility
- 🚀 Seamless AI collaboration
- 🚀 Consistent project management

## 🎉 What's Next?

SimplePlan MCP integration opens up powerful possibilities:

1. **Multi-AI Collaboration**: Multiple AI systems managing different aspects
2. **Automated Workflows**: AI-driven project execution and monitoring  
3. **Integration Ecosystem**: Connect with CI/CD, issue tracking, documentation
4. **Advanced Analytics**: AI-powered project insights and optimization
5. **Team Coordination**: AI facilitating human-AI team collaboration

---

**🏆 SimplePlan is now a universal AI project management platform!**

From CLI tool → MCP-enabled AI assistant → Autonomous project management system

*Ready to revolutionize how AI and humans collaborate on projects? The future of AI-assisted development starts here!* 🚀 
