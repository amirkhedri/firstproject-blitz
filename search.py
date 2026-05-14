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
# -------------------------------------------------------------------
# 4. A* – Optimized with push‑distance + move‑distance heuristic
#    and safe corner deadlock pruning.
# -------------------------------------------------------------------
def astar_solve(game):
    from collections import deque
    import heapq

    height = game.get_grid_height()
    width = game.get_grid_width()
    walls = game.get_walls()
    targets = game.get_targets()
    INF = 10**9

    # ---------- 1. Minimum pushes to any target ----------
    push_dist = [[INF] * width for _ in range(height)]
    q = deque()
    for (tx, ty) in targets:
        if (tx, ty) not in walls:
            push_dist[ty][tx] = 0
            q.append((tx, ty))

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        x, y = q.popleft()
        d = push_dist[y][x]
        for dx, dy in dirs:
            px, py = x - dx, y - dy          # box before push
            player_x, player_y = x + dx, y + dy
            if not (0 <= px < width and 0 <= py < height): continue
            if not (0 <= player_x < width and 0 <= player_y < height): continue
            if (px, py) in walls or (player_x, player_y) in walls: continue
            if push_dist[py][px] > d + 1:
                push_dist[py][px] = d + 1
                q.append((px, py))

    # ---------- 2. Minimum move distance (ignoring boxes) ----------
    move_dist = [[INF] * width for _ in range(height)]
    q = deque()
    for (tx, ty) in targets:
        if (tx, ty) not in walls:
            move_dist[ty][tx] = 0
            q.append((tx, ty))
    while q:
        x, y = q.popleft()
        d = move_dist[y][x]
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in walls:
                if move_dist[ny][nx] > d + 1:
                    move_dist[ny][nx] = d + 1
                    q.append((nx, ny))

    # (To be continued in next commits)
    return None  # temporary
    # ---------- 3. Safe dead cells (only corners) ----------
    dead_cells = set()
    for y in range(height):
        for x in range(width):
            if (x, y) in walls or (x, y) in targets:
                continue
            up = (x, y-1) in walls
            down = (x, y+1) in walls
            left = (x-1, y) in walls
            right = (x+1, y) in walls
            if (up and left) or (up and right) or (down and left) or (down and right):
                dead_cells.add((x, y))

    # ---------- 4. Heuristic (admissible) ----------
    def heuristic(state):
        total = 0
        for bx, by in state.get_boxes():
            pd = push_dist[by][bx]
            if pd >= INF:
                pd = 10000
            md = move_dist[by][bx]
            if md >= INF:
                md = 10000
            total += pd * PUSH_COST + md * MOVE_COST
        return total

    # (Search loop will be added next)
    return None