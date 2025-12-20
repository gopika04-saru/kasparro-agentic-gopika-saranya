from langchain.tools import tool

@tool
def format_output(steps: list, result: str) -> dict:
    """Format final output as structured JSON."""
    return {
        "status": "completed",
        "execution_steps": steps,
        "final_result": result
    }
