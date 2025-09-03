# algorithms.py
import heapq
from math import hypot

def build_graph(data):
    nodes = {n["id"]: {"x": n.get("x", 0), "y": n.get("y", 0), "label": n.get("label", n["id"])}
             for n in data.get("nodes", [])}
    adj = {nid: [] for nid in nodes}
    for e in data.get("edges", []):
        a, b = e["from"], e["to"]
        w = float(e.get("w") or 0)
        if w <= 0:
            ax, ay = nodes[a]["x"], nodes[a]["y"]
            bx, by = nodes[b]["x"], nodes[b]["y"]
            w = hypot(ax - bx, ay - by)
        adj[a].append((b, w))
        adj[b].append((a, w))
    return nodes, adj

def dijkstra(nodes, adj, start, goal):
    dist = {nid: float('inf') for nid in nodes}
    prev = {nid: None for nid in nodes}
    dist[start] = 0.0
    pq = [(0.0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if u == goal: break
        if d != dist[u]: continue
        for v, w in adj.get(u, []):
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))
    if dist[goal] == float('inf'): return []
    path, cur = [], goal
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    return path[::-1]

def astar(nodes, adj, start, goal):
    def h(a, b):
        ax, ay = nodes[a]["x"], nodes[a]["y"]
        bx, by = nodes[b]["x"], nodes[b]["y"]
        return hypot(ax - bx, ay - by)

    g = {nid: float('inf') for nid in nodes}
    f = {nid: float('inf') for nid in nodes}
    came = {nid: None for nid in nodes}

    g[start] = 0.0
    f[start] = h(start, goal)
    pq = [(f[start], start)]
    opened = {start}

    while pq:
        _, u = heapq.heappop(pq)
        opened.discard(u)
        if u == goal:
            path, cur = [], goal
            while cur is not None:
                path.append(cur)
                cur = came[cur]
            return path[::-1]
        for v, w in adj.get(u, []):
            tentative = g[u] + w
            if tentative < g[v]:
                g[v] = tentative
                came[v] = u
                f[v] = tentative + h(v, goal)
                if v not in opened:
                    heapq.heappush(pq, (f[v], v))
                    opened.add(v)
    return []
