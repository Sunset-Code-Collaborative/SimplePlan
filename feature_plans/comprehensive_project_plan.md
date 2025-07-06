# 🚀 SimplePlan - Comprehensive Project Plan

## 📋 Project Overview

**SimplePlan** is a Python CLI tool that provides an Agentic Project Plan IO Protocol - a portable, AI-friendly workflow for project planning that works seamlessly across AI tools (Cursor, OpenAI, Claude, etc.).

## 🎯 Strategic Context

- **Project Phase**: Phase 2 - MCP Integration (Phase 1 MVP Complete ✅)
- **Priority Tier**: ⭐⭐⭐ Critical (Universal AI accessibility via MCP)
- **Current State**: Production-ready CLI tool with full functionality
- **Target**: MCP server enabling AI systems to directly manage project plans

## 🧩 Current State Analysis

### ✅ Phase 1 Complete (MVP)
- ✅ Full CLI tool with Click framework
- ✅ Complete project_plan_io module implementation
- ✅ Pydantic data models with validation
- ✅ Rich terminal UI with tables and colors
- ✅ Comprehensive test suite (12 tests passing)
- ✅ JSON persistence with schema validation
- ✅ Dependency management between steps
- ✅ Error handling and user-friendly messages

### 🎯 Phase 2 Ready (MCP Integration)
- ❌ MCP server implementation
- ❌ Claude Desktop integration
- ❌ Universal AI tool accessibility
- ❌ Real-time project plan management during AI conversations

## 🎯 Development Roadmap

### Phase 1: Core Foundation (MVP) ✅ COMPLETE
- [x] **STEP-001**: Implement core project_plan_io module
  - ✅ Create src/project_plan_io.py with all documented functions
  - ✅ Add proper error handling and validation
  - ✅ Include JSON schema validation
  - ✅ Success: Module can create, read, update project plans

- [x] **STEP-002**: Create CLI interface
  - ✅ Create CLI entry point with Click framework
  - ✅ Support commands: create, status, complete, list, add, next, validate
  - ✅ Add --help documentation with rich formatting
  - ✅ Success: CLI can execute all basic operations

- [x] **STEP-003**: Write comprehensive tests
  - ✅ Unit tests for all core functions
  - ✅ Integration tests for CLI operations
  - ✅ Error handling and validation tests
  - ✅ Success: 12 tests passing, robust test coverage

### Phase 2: MCP Integration (Universal AI Access)
- [ ] **STEP-004**: Install MCP dependencies (fastmcp, mcp)
  - Add FastMCP and MCP to pyproject.toml
  - Install dependencies via Poetry
  - Success: MCP libraries available for development

- [ ] **STEP-005**: Create MCP server wrapper (mcp_server.py) with FastMCP integration
  - Create new mcp_server.py file
  - Initialize FastMCP server instance
  - Set up basic server structure and imports
  - Success: MCP server can be started and accepts connections

- [ ] **STEP-006**: Implement MCP tools for project plan operations
  - create_project_plan() - Create new projects via AI
  - get_project_status() - Check project progress 
  - add_project_step() - Add steps during AI conversations
  - complete_step() - Mark steps complete from AI tools
  - get_next_steps() - Show available work to AI
  - list_all_steps() - Display project overview
  - Success: All core SimplePlan operations available via MCP

- [ ] **STEP-007**: Configure Claude Desktop integration with claude_desktop_config.json
  - Create Claude Desktop configuration file
  - Set up server connection parameters
  - Configure MCP server discovery
  - Success: Claude Desktop can discover and connect to SimplePlan MCP server

- [ ] **STEP-008**: Test MCP server integration with Claude Desktop
  - Start MCP server and verify Claude connection
  - Test project creation via Claude conversations
  - Test step management and status checking
  - Validate real-time project plan updates
  - Success: Full project planning workflow works through Claude

- [ ] **STEP-009**: Create MCP integration documentation and usage examples
  - Document MCP server setup and configuration
  - Create usage examples for AI-driven project planning
  - Add troubleshooting guide
  - Document benefits of MCP vs CLI-only approach
  - Success: Clear documentation for MCP setup and usage

### Phase 3: Advanced Features
- [ ] **STEP-008**: Add AI integration hooks
  - Plugin system for AI tools
  - Webhook support for external integrations
  - API endpoints for programmatic access
  - Success: External tools can integrate with SimplePlan

- [ ] **STEP-009**: Version control integration
  - Git integration for plan history
  - Commit hooks for automatic updates
  - Branch-based planning
  - Success: Version control workflow integration

- [ ] **STEP-010**: Web UI development
  - Simple web interface for plan viewing
  - Interactive step completion
  - Progress visualization
  - Success: Web-based project management interface

## 🛠️ Technical Architecture

### Core Components
1. **project_plan_io.py** - Core I/O operations ✅
2. **cli.py** - Command-line interface ✅
3. **models.py** - Data models and validation ✅
4. **mcp_server.py** - MCP server for AI integration 🆕
5. **exporters.py** - Format export functionality
6. **integrations.py** - External tool integrations

### Dependencies ✅ Current
- `click` - CLI framework ✅
- `jsonschema` - JSON validation ✅
- `rich` - Terminal UI enhancement ✅
- `pydantic` - Data validation ✅
- `jinja2` - Template rendering ✅

### Dependencies 🆕 MCP Phase
- `fastmcp` - FastMCP server framework
- `mcp` - Model Context Protocol library

## 🔧 Project Structure (Target)
```
SimplePlan/
├── src/
│   ├── simpleplan/
│   │   ├── __init__.py
│   │   ├── cli.py
│   │   ├── project_plan_io.py
│   │   ├── models.py
│   │   ├── exporters.py
│   │   └── integrations.py
│   └── main.py
├── templates/
│   ├── project_template.json
│   └── step_templates/
├── examples/
│   ├── basic_project.json
│   └── complex_project.json
└── docs/
    ├── CLI_USAGE.md
    └── API_REFERENCE.md
```

## 🎯 Success Criteria

### Phase 1 (MVP) ✅ COMPLETE
- [x] CLI tool can create and manage project plans
- [x] JSON I/O operations work reliably
- [x] Basic step completion tracking
- [x] Clear documentation and examples

### Phase 2 (MCP Integration)
- [ ] MCP server successfully runs and accepts connections
- [ ] Claude Desktop can discover and connect to SimplePlan
- [ ] AI can create, manage, and track project plans via conversation
- [ ] Real-time project updates during AI interactions
- [ ] Universal compatibility with MCP-enabled AI tools

### Phase 3 (Advanced)
- [ ] Web UI functional
- [ ] Git integration working
- [ ] Plugin system operational
- [ ] Production deployment ready

## 🧪 Testing Strategy

- Unit tests for all core functions
- Integration tests for CLI operations
- End-to-end tests for complete workflows
- Performance tests for large project plans
- Cross-platform compatibility testing

## 📈 Timeline Estimate

- **Phase 1**: 2-3 weeks (MVP)
- **Phase 2**: 3-4 weeks (Enhanced features)
- **Phase 3**: 4-6 weeks (Advanced features)

## 🎯 Immediate Next Steps

1. **START HERE**: Install MCP dependencies (STEP-004)
2. Create MCP server wrapper with FastMCP
3. Implement core MCP tools for project management
4. Configure Claude Desktop integration
5. Test full AI-driven project planning workflow

---

*This plan provides a clear roadmap from the current prototype state to a production-ready CLI tool for AI-assisted project management.* 
