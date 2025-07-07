#!/usr/bin/env python3
"""Minimal SimplePlan MCP Server - No stdout output."""

import sys
import os
from pathlib import Path

# Add the src directory to Python path
script_dir = Path(__file__).parent
src_dir = script_dir / "src"
sys.path.insert(0, str(src_dir))

try:
    from simpleplan.mcp_server import mcp
    
    if __name__ == "__main__":
        # NO print statements to avoid interfering with MCP protocol
        mcp.run()
        
except Exception as e:
    # Only log errors to stderr
    print(f"❌ MCP Server Error: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc(file=sys.stderr)
    sys.exit(1) 
