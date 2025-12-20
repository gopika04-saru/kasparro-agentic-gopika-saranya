### How to RUN the project
#### Prerequisites

#### 🔹 Step 1: Create virtual environment (recommended)
```
  python -m venv venv
```

#### Activate it:

```
venv\Scripts\activate
```

#### 🔹 Step 2: Install dependencies
```
pip install langchain langchain-openai langgraph pydantic
 ```

#### 🔹 Step 3: Set API Key
#### Windows 
```
setx OPENAI_API_KEY "your_api_key_here"
 ```

#### 🔹 Step 4: Run the project

```
python main.py
```

### What OUTPUT you will see (REAL example)
```
> Entering new AgentExecutor chain...

Thought: I need to plan the task first
Action: plan_task
Action Input: Create a 30-day roadmap to learn Spring Boot
Observation: ['Understand the task requirements', 'Identify required knowledge or resources', 'Execute each step sequentially', 'Validate and summarize results']

Thought: I should research Spring Boot
Action: research_topic
Action Input: Spring Boot
Observation: Research findings for Spring Boot: key concepts, best practices, common pitfalls.

Thought: I should format the final output
Action: format_output
Action Input:
{
  steps: [...],
  result: "30-day roadmap created..."
}

> Finished chain.
```

### 🔹 FINAL JSON OUTPUT
```
{
  "status": "completed",
  "execution_steps": [
    "Understand the task requirements",
    "Identify required knowledge or resources",
    "Execute each step sequentially",
    "Validate and summarize results"
  ],
  "final_result": "Research findings for Spring Boot: key concepts, best practices, common pitfalls."
}
```
