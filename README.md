# CLUSY MCP

Scientific orchestration MCP server for CLUSY.

## Architecture

GPT Scientific Director
-> Human Approval
-> CLUSY Runtime
-> Canonical Job Manager
-> Execution Gate
-> Executor
-> Result
-> Evidence / Memory
-> GPT

## Safety

This repository contains only the MCP deployment layer.

Scientific project data, QE files, credentials, API tokens,
ModelScope secrets, and local CLUSY state are not included.

Human approval remains required before execution.

Approval does not itself execute a scientific job.

## Local development

Install dependencies:

    pip install -r requirements.txt

Run:

    python clusy_mcp_server.py
