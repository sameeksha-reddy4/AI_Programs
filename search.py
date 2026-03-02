from collections import deque

# Jug capacities
A = 4
B = 3
GOAL = 2


# -------- BFS --------
def bfs():
    visited = set()
    queue = deque([((0, 0), [])])
    nodes = 0

    while queue:
        (x, y), path = queue.popleft()
        nodes += 1

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        if x == GOAL or y == GOAL:
            return path, nodes

        next_states = [
            (A, y), (x, B), (0, y), (x, 0),
            (max(0, x-(B-y)), min(B, y+x)),
            (min(A, x+y), max(0, y-(A-x)))
        ]

        for state in next_states:
            queue.append((state, path))

    return None, nodes


# -------- DFS --------
def dfs():
    visited = set()
    stack = [((0, 0), [])]
    nodes = 0

    while stack:
        (x, y), path = stack.pop()
        nodes += 1

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        if x == GOAL or y == GOAL:
            return path, nodes

        next_states = [
            (A, y), (x, B), (0, y), (x, 0),
            (max(0, x-(B-y)), min(B, y+x)),
            (min(A, x+y), max(0, y-(A-x)))
        ]

        for state in next_states:
            stack.append((state, path))

    return None, nodes


# -------- RUN BOTH --------

bfs_path, bfs_nodes = bfs()
dfs_path, dfs_nodes = dfs()


print("BFS Solution Path:")
for s in bfs_path:
    print(s)

print("\nDFS Solution Path:")
for s in dfs_path:
    print(s)


# -------- COMPARISON --------

print("\n--- PERFORMANCE COMPARISON ---")

print(f"BFS Path Length : {len(bfs_path)}")
print(f"DFS Path Length : {len(dfs_path)}")

print(f"BFS Nodes Explored : {bfs_nodes}")
print(f"DFS Nodes Explored : {dfs_nodes}")

if len(bfs_path) < len(dfs_path):
    print("\nBFS found shorter solution")
elif len(bfs_path) > len(dfs_path):
    print("\nDFS found shorter solution")
else:
    print("\nBoth found equal-length solutions")