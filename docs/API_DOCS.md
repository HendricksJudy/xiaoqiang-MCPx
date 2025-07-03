# API Documentation

This document describes the JSON-RPC 2.0 methods exposed by the MCP server.

## Authentication

All `tools/call` requests must include a valid token via the `token` field. The expected token can be set with the `MCP_TOKEN` environment variable (defaults to `testtoken`).

## Available Methods

### `tools/list`
Returns the list of available tool names.

```
{"jsonrpc": "2.0", "id": "1", "method": "tools/list", "params": {}}
```

### `server/get_capabilities`
Retrieves the server capability declaration loaded from `config/capabilities.json`.

```
{"jsonrpc": "2.0", "id": "2", "method": "server/get_capabilities", "params": {}}
```

### `tools/call`
Invokes a specific tool by name. Example payload for the `query_knowledge_base` tool:

```
{
  "jsonrpc": "2.0",
  "id": "3",
  "method": "tools/call",
  "params": {
    "token": "testtoken",
    "name": "query_knowledge_base",
    "arguments": {
      "cancer_type": "肺癌",
      "query": "靶向治疗药物有哪些"
    }
  }
}
```

The exact input schema for each tool is defined in `src/schemas.py`.

