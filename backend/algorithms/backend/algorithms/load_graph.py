import json
from collections import defaultdict

def load_graph():
    # Load the Surat city graph data
    with open("backend/algorithms/graph_data.json", "r") as f:
        data = json.load(f)

    graph = defaultdict(list)

    for edge in data["edges"]:
        u = edge["from"]
        v = edge["to"]
        w = edge["distance"]

        graph[u].append((v, w))
        graph[v].append((u, w))  # undirected graph

    return graph, data["nodes"]

# Test the loader (optional)
if __name__ == "__main__":
    graph, nodes = load_graph()
    print("\nNodes in the graph:")
    print(nodes)
    print("\nGraph connections:")
    for key in graph:
        print(key, "->", graph[key])
