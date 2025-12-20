from langchain.tools import tool

@tool
def plan_task(task: str) -> list:
    """Break a task into actionable steps."""
    return [
        "Understand the task requirements",
        "Identify required knowledge or resources",
        "Execute each step sequentially",
        "Validate and summarize results"
    ]
