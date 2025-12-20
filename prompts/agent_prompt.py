from langchain.prompts import ChatPromptTemplate

agent_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an autonomous task execution agent. "
     "You must reason step-by-step, select tools when needed, "
     "and produce structured JSON output."),
    ("human", "{input}")
])
