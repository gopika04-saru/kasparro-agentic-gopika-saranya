from langgraph.graph import StateGraph, END
from typing import TypedDict, Any

from agents.agent_factory import create_agent


class AgentState(TypedDict):
    input: str
    output: Any


agent_runnable = create_agent()


def agent_node(state: AgentState):
    return agent_runnable.invoke(state)


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("agent", agent_node)
    graph.set_entry_point("agent")
    graph.add_edge("agent", END)

    return graph.compile()
