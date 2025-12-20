from graph.task_graph import build_graph

if __name__ == "__main__":
    graph = build_graph()

    result = graph.invoke({
        "input": "Create a 30-day roadmap to learn Spring Boot"
    })

    print("\nFINAL OUTPUT:\n")
    print(result)
