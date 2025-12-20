from langchain.tools import tool

@tool
def research_topic(topic: str) -> str:
    """Research a topic conceptually."""
    return f"Research findings for {topic}: key concepts, best practices, common pitfalls."
