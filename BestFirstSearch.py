import heapq

# Costos de las acciones
action_costs = {
    ('A', 'B'): 1,
    ('A', 'C'): 4,
    ('B', 'D'): 3,
    ('C', 'D'): 2,
    ('D', 'E'): 2,
    ('B', 'A'): 1,
    ('C', 'A'): 4,
    ('D', 'B'): 3,
    ('D', 'C'): 2,
    ('E', 'D'): 2
}

# Función para obtener vecinos (acciones posibles)
def get_actions(state):
    return [ (dest, cost) for (src, dest), cost in action_costs.items() if src == state ]

# Búsqueda de costo uniforme
def uniform_cost_search(start, goal):
    frontier = [(0, start, [start])]  # (costo_acumulado, estado_actual, camino)
    explored = set()

    while frontier:
        cost, state, path = heapq.heappop(frontier)

        if state == goal:
            print(" -> ".join(path))
            print(f"Costos: {' + '.join(str(action_costs[(path[i], path[i+1])]) for i in range(len(path)-1))} = {cost}")
            return

        if state in explored:
            continue

        explored.add(state)

        for neighbor, step_cost in get_actions(state):
            if neighbor not in explored:
                heapq.heappush(frontier, (cost + step_cost, neighbor, path + [neighbor]))

# Estado inicial y meta
initial = 'A'
goal = 'E'


uniform_cost_search(initial, goal)