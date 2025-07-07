#!/usr/bin/env python3
"""Standalone SimplePlan MCP Server - No Poetry dependency required."""

import sys
import os
from pathlib import Path

# Add the src directory to Python path so we can import our modules
script_dir = Path(__file__).parent
src_dir = script_dir / "src"
sys.path.insert(0, str(src_dir))

# Now import and run the MCP server
try:
    from simpleplan.mcp_server import mcp
    
    if __name__ == "__main__":
        print("🚀 Starting SimplePlan MCP Server (Standalone)...", file=sys.stderr)
        print("📋 Available tools:", file=sys.stderr)
        print("  • create_project_plan - Create new projects", file=sys.stderr)
        print("  • get_project_status - Check project progress", file=sys.stderr)
        print("  • add_project_step - Add new steps", file=sys.stderr)
        print("  • complete_step - Mark steps as done", file=sys.stderr)
        print("  • get_next_steps - Show available work", file=sys.stderr)
        print("  • list_all_steps - Display all steps", file=sys.stderr)
        print("  • validate_project_plan - Check for errors", file=sys.stderr)
        print("\n📡 Server ready for MCP connections...", file=sys.stderr)
        
        try:
            mcp.run()
        except Exception as e:
            print(f"❌ Error during MCP server execution: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc(file=sys.stderr)
            sys.exit(1)
        
except ImportError as e:
    print(f"❌ Error importing SimplePlan modules: {e}", file=sys.stderr)
    print("💡 Make sure fastmcp and dependencies are installed:", file=sys.stderr)
    print("   pip install fastmcp rich pydantic click jsonschema", file=sys.stderr)
    print(f"Current working directory: {os.getcwd()}", file=sys.stderr)
    print(f"Python path: {sys.path}", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"❌ Error starting MCP server: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc(file=sys.stderr)
    sys.exit(1) 
