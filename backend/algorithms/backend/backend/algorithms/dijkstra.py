import heapq
from load_graph import load_graph

def dijkstra(graph, start, end):
    # Distance to nodes (infinity initially)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Parent dictionary to reconstruct path
    parent = {node: None for node in graph}

    # Min-heap priority queue
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Stop if we reach the destination
        if current_node == end:
            break

        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    # Reconstruct path
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = parent[current]

    return path[::-1], distances[end]


if __name__ == "__main__":
    graph, nodes = load_graph()
    route, dist = dijkstra(graph, "Adajan", "Varachha")

    print("\nShortest Route:", route)
    print("Total Distance:", dist, "km")
