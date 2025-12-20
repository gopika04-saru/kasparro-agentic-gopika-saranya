from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableLambda

from tools.planner_tool import plan_task
from tools.research_tool import research_topic
from tools.formatter_tool import format_output


def create_agent():
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )

    tools = {
        "plan_task": plan_task,
        "research_topic": research_topic,
        "format_output": format_output
    }

    def agent_logic(state):
        user_input = state["input"]

        # LLM decides what to do
        response = llm.invoke([
            HumanMessage(
                content=f"""
You are an autonomous agent.
Decide which tool to use and why.

Available tools:
- plan_task(task)
- research_topic(topic)
- format_output(steps, result)

User task: {user_input}

Respond in JSON with:
tool_name
tool_input
"""
            )
        ])

        decision = response.content

        # Simple tool execution based on LLM decision
        if "plan_task" in decision:
            steps = tools["plan_task"](user_input)
            result = tools["research_topic"](user_input)
            final = tools["format_output"](steps, result)
        else:
            final = {"status": "completed", "result": decision}

        return {"output": final}

    return RunnableLambda(agent_logic)
