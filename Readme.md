# AI School Mini

A small multi-agent backend: a Principal (router) sends student questions to
Maths, English, Science and History teacher agents. Built to learn production
AI system design: gateway, memory, cache, tools/MCP, reliability, deployment.

## Run
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    uvicorn app.main:app --reload

## Progress
- [x] Day 1: skeleton and /health