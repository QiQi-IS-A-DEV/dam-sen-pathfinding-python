# app.py
import json
import os
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from algorithms import build_graph, dijkstra, astar

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app, resources={r"/api/*": {"origins": "*"}})  # không bắt buộc nếu cùng origin

# Load graph khi khởi động
with open(os.path.join(app.root_path, "graph.json"), "r", encoding="utf-8") as f:
    GRAPH_DATA = json.load(f)

# Nếu bạn cần server-side pathfind thì giữ lại NODES/ADJ:
NODES, ADJ = build_graph(GRAPH_DATA)

@app.route("/")
def index():
    return render_template("index.html")

# API: trả graph.json (một route duy nhất, không trùng)
@app.get("/api/graph")
def api_graph():
    return jsonify(GRAPH_DATA)

# (Tuỳ chọn) API tính đường server-side — nếu muốn dùng thay vì client-side
@app.post("/api/route")
def api_route():
    data = request.get_json(force=True)
    start = data.get("start")
    goal  = data.get("end")
    algo  = (data.get("algo") or "astar").lower()

    if not start or not goal:
        return jsonify({"error": "Missing start or goal"}), 400
    if start not in NODES or goal not in NODES:
        return jsonify({"error": "Invalid start/goal id"}), 400

    if algo == "dijkstra":
        path = dijkstra(NODES, ADJ, start, goal)
    else:
        path = astar(NODES, ADJ, start, goal)

    # tính length (fallback theo khoảng cách Euclid nếu không có weight)
    length = 0.0
    for i in range(1, len(path)):
        u, v = path[i-1], path[i]
        w = next((w for (nid, w) in ADJ[u] if nid == v), None)
        if w is None:
            from math import hypot
            ax, ay = NODES[u]["x"], NODES[u]["y"]
            bx, by = NODES[v]["x"], NODES[v]["y"]
            w = hypot(ax - bx, ay - by)
        length += w

    return jsonify({"path": path, "length": length})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
