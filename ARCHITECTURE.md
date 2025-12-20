## Architecture Overview

This project implements a real agentic system using
LangChain and LangGraph.

### Core Principles
- LLM-driven decision making
- Tool-based reasoning
- Graph-based orchestration
- Fully structured JSON output

### Components
- LangChain OpenAI Tools Agent
- Tools: Planner, Research, Formatter
- LangGraph StateGraph for execution flow
- Centralized prompt templates
- Pydantic output schema

### Execution Flow
User Input →
LangGraph →
LangChain Agent →
Tool Selection →
Tool Execution →
Observation →
Final JSON Output

### Why LangChain + LangGraph
- LangChain provides production-ready agents
- LangGraph enables deterministic orchestration
- Clean separation of reasoning and execution
- Easily extensible to multi-agent workflows
