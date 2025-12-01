from flask import Flask, request, jsonify
from algorithms.load_graph import load_graph
from algorithms.dijkstra import dijkstra

app = Flask(__name__)

# Load the Surat city graph
graph, nodes = load_graph()

@app.route("/nodes")
def get_nodes():
    return jsonify({"nodes": nodes})


@app.route("/route")
def get_route():
    start = request.args.get("start")
    end = request.args.get("end")

    if not start or not end:
        return jsonify({"error": "start and end parameters are required"}), 400

    if start not in nodes or end not in nodes:
        return jsonify({"error": "Invalid node name"}), 400

    # Run Dijkstra
    path, distance = dijkstra(graph, start, end)

    return jsonify({
        "start": start,
        "end": end,
        "path": path,
        "distance_km": distance
    })


@app.route("/")
def home():
    return jsonify({
        "message": "SUMOS API is working!",
        "routes_available": ["/nodes", "/route?start=A&end=B"]
    })


if __name__ == "__main__":
    app.run(debug=True)
