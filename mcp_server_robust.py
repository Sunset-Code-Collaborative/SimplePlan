#!/usr/bin/env python3
"""Robust SimplePlan MCP Server - Follows MCP debugging best practices.

Copyright (c) 2025 Sunset Code Collaborative, LLC
Licensed under the MIT License - see LICENSE file for details.
"""

import sys
import os
from pathlib import Path

def setup_environment():
    """Set up the environment correctly for MCP server operation."""
    # Get the script directory and set working directory
    script_dir = Path(__file__).parent.absolute()
    os.chdir(script_dir)
    
    # Add the src directory to Python path
    src_dir = script_dir / "src"
    sys.path.insert(0, str(src_dir))
    
    # Log setup to stderr (safe for MCP)
    print(f"🔧 Working directory: {os.getcwd()}", file=sys.stderr)
    print(f"🔧 Script directory: {script_dir}", file=sys.stderr)
    print(f"🔧 Source directory: {src_dir}", file=sys.stderr)

def main():
    """Main entry point for the MCP server."""
    try:
        setup_environment()
        
        # Import after environment setup
        from simpleplan.mcp_server import mcp
        
        # Log to stderr only (MCP requirement)
        print("🚀 SimplePlan MCP Server starting...", file=sys.stderr)
        
        # Start the server (this will handle stdout/stdin for MCP protocol)
        mcp.run()
        
    except ImportError as e:
        print(f"❌ Import Error: {e}", file=sys.stderr)
        print(f"📂 Current working directory: {os.getcwd()}", file=sys.stderr)
        print(f"🐍 Python path: {sys.path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Server Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 
