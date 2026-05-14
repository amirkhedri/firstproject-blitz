from collections import deque
import heapq
from env.sokoban import PUSH_COST, MOVE_COST

# -------------------------------------------------------------------
# 1. BFS – Breadth‑First Search (shortest action sequence)
# -------------------------------------------------------------------
def bfs_solve(game):
    start_state = game.get_initial_state()
    if game.is_goal(start_state):
        return []

    frontier = deque()
    frontier.append((start_state, []))
    visited = {start_state}

    while frontier:
        state, actions = frontier.popleft()
        for action, next_state, _ in game.get_successors(state):
            if next_state in visited:
                continue
            if game.is_goal(next_state):
                return actions + [action]
            visited.add(next_state)
            frontier.append((next_state, actions + [action]))
    return None
# -------------------------------------------------------------------
# 2. IDS – Iterative Deepening Search (depth‑limited DFS)
# -------------------------------------------------------------------
def ids_solve(game):
    def dls(state, depth, path, visited_depth, limit):
        if game.is_goal(state):
            return path
        if depth >= limit:
            return None
        if state in visited_depth and visited_depth[state] <= depth:
            return None
        visited_depth[state] = depth

        for action, next_state, _ in game.get_successors(state):
            result = dls(next_state, depth + 1, path + [action], visited_depth, limit)
            if result is not None:
                return result
        return None

    start_state = game.get_initial_state()
    for depth_limit in range(0, 10000):
        visited_depth = {}
        result = dls(start_state, 0, [], visited_depth, depth_limit)
        if result is not None:
            return result
    return None
# -------------------------------------------------------------------
# 3. UCS – Uniform Cost Search (minimizes total cost)
# -------------------------------------------------------------------
def ucs_solve(game):
    start_state = game.get_initial_state()
    if game.is_goal(start_state):
        return []

    frontier = []                     # (cost, tie_breaker, state, actions)
    counter = 0
    heapq.heappush(frontier, (0, counter, start_state, []))
    best_cost = {start_state: 0}
    visited = set()                   # closed set

    while frontier:
        cost, _, state, actions = heapq.heappop(frontier)
        if state in visited:
            continue
        if best_cost.get(state, float('inf')) < cost:
            continue
        if game.is_goal(state):
            return actions

        visited.add(state)

        for action, next_state, step_cost in game.get_successors(state):
            new_cost = cost + step_cost
            if new_cost < best_cost.get(next_state, float('inf')):
                best_cost[next_state] = new_cost
                counter += 1
                heapq.heappush(frontier, (new_cost, counter, next_state, actions + [action]))
    return None