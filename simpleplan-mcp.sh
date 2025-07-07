#!/bin/bash
# SimplePlan MCP Server Wrapper - Poetry Independent
# This script finds the correct Python environment and runs the MCP server

set -e

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Function to find Python with fastmcp
find_python_with_fastmcp() {
    # Try Poetry venv first if available
    if command -v poetry >/dev/null 2>&1; then
        if poetry env info --path >/dev/null 2>&1; then
            POETRY_VENV=$(poetry env info --path 2>/dev/null)
            if [[ -f "$POETRY_VENV/bin/python" ]]; then
                if "$POETRY_VENV/bin/python" -c "import fastmcp" >/dev/null 2>&1; then
                    echo "$POETRY_VENV/bin/python"
                    return 0
                fi
            fi
        fi
    fi
    
    # Try current Python environment
    if python3 -c "import fastmcp" >/dev/null 2>&1; then
        echo "python3"
        return 0
    fi
    
    # Try system Python
    if python -c "import fastmcp" >/dev/null 2>&1; then
        echo "python"
        return 0
    fi
    
    # Not found
    return 1
}

# Find Python interpreter
echo "🔍 Finding Python with fastmcp..." >&2
if PYTHON_CMD=$(find_python_with_fastmcp); then
    echo "✅ Found Python: $PYTHON_CMD" >&2
else
    echo "❌ Error: Cannot find Python with fastmcp installed!" >&2
    echo "💡 Install with: pip install fastmcp rich pydantic click jsonschema" >&2
    exit 1
fi

# Run the MCP server
echo "🚀 Starting SimplePlan MCP Server..." >&2
exec "$PYTHON_CMD" mcp_server_standalone.py 
