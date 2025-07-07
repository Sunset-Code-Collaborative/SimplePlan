# 🔌 Claude Desktop Setup for SimplePlan MCP

## 📍 Configuration File Location

The `claude_desktop_config.json` file needs to be placed in Claude Desktop's configuration directory:

**macOS Location:**
```bash
~/Library/Application Support/Claude/claude_desktop_config.json
```

## 🚀 Setup Steps

### 1. Copy Configuration File
```bash
# Create the Claude config directory if it doesn't exist
mkdir -p ~/Library/Application\ Support/Claude/

# Copy our configuration file to Claude's config location
cp claude_desktop_config.json ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

### 2. Verify Configuration
```bash
# Check that the file was copied correctly
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

### 3. Restart Claude Desktop
- Quit Claude Desktop completely (Cmd+Q)
- Reopen Claude Desktop
- Look for SimplePlan in the available tools/integrations

## 🔧 Configuration Explained

```json
{
  "mcpServers": {
    "simpleplan": {
      "command": "poetry",                    // Use Poetry to run in virtual env
      "args": [
        "run",
        "python", 
        "-m",
        "src.simpleplan.mcp_server"           // Our MCP server module
      ],
      "cwd": "/Users/bjornjohnson/dev/SimplePlan",  // Project directory
      "env": {}                               // Environment variables (if needed)
    }
  }
}
```

## ✅ Testing the Integration

Once configured, you should be able to:

1. **Create Projects**: Ask Claude to create a new project plan
2. **Check Status**: Ask Claude about project progress
3. **Add Steps**: Ask Claude to add new steps to your project
4. **Complete Steps**: Tell Claude when you've finished a step
5. **Get Next Tasks**: Ask Claude what to work on next

## 🎯 Example Commands to Try

Once connected, try these with Claude:

- *"Create a new project called 'Website Redesign' with description 'Modern responsive website'"*
- *"What's the status of my current project?"*
- *"Add a step to implement user authentication"*
- *"Mark STEP-001 as complete"*
- *"What should I work on next?"*
- *"Show me all the steps in my project"*

## 🐛 Troubleshooting

### Claude Can't Find SimplePlan
1. Check file location: `~/Library/Application Support/Claude/claude_desktop_config.json`
2. Verify JSON syntax is valid
3. Restart Claude Desktop completely
4. Check that Poetry and SimplePlan work in terminal

### MCP Server Won't Start
1. Test manually: `poetry run python -m src.simpleplan.mcp_server`
2. Ensure you're in the correct directory: `/Users/bjornjohnson/dev/SimplePlan`
3. Check Poetry virtual environment is working: `poetry shell`

### Path Issues
- Make sure the `cwd` path points to your actual SimplePlan directory
- Update the path in `claude_desktop_config.json` if you moved the project

## 🚀 Success!

When working correctly, Claude will be able to:
- See SimplePlan as an available tool
- Create and manage project plans in real-time
- Provide intelligent project planning assistance
- Keep track of your progress automatically

**You'll have transformed SimplePlan from a CLI tool into a universal AI-accessible project management system!** 🎉 
