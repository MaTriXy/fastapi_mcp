"""
FastAPI-MCP: Automatic MCP server generator for FastAPI applications.

Created by Tadata Inc. (https://github.com/tadata-org)
"""

try:
    from importlib.metadata import version

    __version__ = version("fastapi-mcp")
except Exception:
    # Fallback for local development
    __version__ = "0.0.0.dev0"

from .server import FastApiMCP


__all__ = [
    "FastApiMCP",
]
