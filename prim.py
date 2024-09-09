import heapq


def prim(graph, start):
    mst = []  # 儲存最小生成樹中的邊
    visited = set()
    min_heap = [(0, start, None)]
    total_weight = 0

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        if parent is not None:
            mst.append((parent, node, weight))
            total_weight += weight

        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, node))

    return mst, total_weight


graph = {
    'A': [('B', 7), ('D', 5)],
    'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
    'C': [('B', 8), ('E', 5)],
    'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
    'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8)],
    'F': [('D', 6), ('E', 8)]
}

mst, total_weight = prim(graph, 'A')
print("最小生成樹:", mst)
print("總權重:", total_weight)