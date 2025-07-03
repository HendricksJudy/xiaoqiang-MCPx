# Deployment Guide

This guide explains how to run the MCP server locally or in a production environment.

## Prerequisites

- Python 3.9 or newer
- Required Python packages from `requirements.txt` (install using `pip install -r requirements.txt` if provided)

## Running Locally

1. Install dependencies:
   ```bash
   pip install structlog pydantic pytest-asyncio
   ```
2. Start the server:
   ```bash
   python -m src.server.mcp_server
   ```
3. Send JSON-RPC requests using the examples from [API_DOCS.md](API_DOCS.md).

The server expects a token supplied via the `MCP_TOKEN` environment variable; it defaults to `testtoken`.

## Production Considerations

- Bind the HTTP transport to `127.0.0.1` or behind a reverse proxy.
- Use HTTPS when exposing the server over the network.
- Configure proper logging and monitoring as described in the README.

