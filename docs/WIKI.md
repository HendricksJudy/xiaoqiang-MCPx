# Project Wiki

## Overview

This project implements an MCP-compliant server built on FastGPT. It offers cancer-focused knowledge bases, multiple RAG-driven assistants, API/webhook integration, and various medical tools. Current capabilities include knowledge sharing for patients, detailed report analysis, and clinical trial information.

## Core Features

- JSON-RPC 2.0 server with token verification and rate limiting
- Tools for knowledge base queries, medical resource lookup, report analysis, clinical trials, travel planning, insurance policy consultation, and drug information
- Webhook integrations for platforms such as WeChat, Feishu and DingTalk

## Key Directories

- **src/** – Server code, tool implementations and supporting modules
- **tests/** – Unit tests validating tool behavior and MCP compliance
- **config/** – Default server configuration and capability declarations

## Environment Variables

- `MCP_TOKEN` – expected token for all `tools/call` requests. Defaults to `testtoken` when unset. Invalid tokens raise error `-32001`.
- `MCP_SESSION_ID` – optional session identifier. If set, incoming requests must supply the same session ID or error `-32003` is returned.

## Compliance

See [MCP_COMPLIANCE.md](MCP_COMPLIANCE.md) for details on how this project meets MCP standard requirements.

