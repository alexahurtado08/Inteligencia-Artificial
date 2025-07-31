import heapq

class Node:
    def __init__(self, position, parent=None, action=None, path_cost=0): #agregar action
        self.position = position
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost

class Problem:
    def __init__(self, initial, goal, actions, action_cost=1):
        self.initial = initial #Estado inicial
        self.goal = goal #Estado objetivo
        self.actions = actions #acciones disponibles desde un estado.
        self.action_cost = action_cost #costo de una acción

def find_exit(maze):
    start = (1, 1)  # Posición inicial (basado en el ejemplo)
    end = (1, 6)    # Posición de la salida (basado en el ejemplo)

    actions={(-1,0):"Up",
             (1,0):"Down",
             (0,1):"Right",
             (0,-1):"Left"}

    problem=Problem(start, end, actions)

    def manhatan_distance(pos, goal):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])  # Distancia de Manhattan

    def get_neighbors(pos):
        neighbors = [] #lista de vecinos
        moves=[] #agrego lista para tecking de movimientos
        for move in [x for x in problem.actions.keys()]:  # Movimientos: arriba, abajo, izquierda, derecha          for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Movimientos: arriba, abajo, izquierda, derecha
            neighbor = (pos[0] + move[0], pos[1] + move[1])
            if maze[neighbor[0]][neighbor[1]] != "#": #si el vecino es diferente a "#" pared agregarlo a la lista de vecinos                neighbors.append(neighbor)
              neighbors.append(neighbor)
              moves.append(actions[move])
        return neighbors, moves

    start_node = Node(problem.initial, path_cost=0)
    frontier = [(manhatan_distance(problem.initial, problem.goal), start_node)]
    heapq.heapify(frontier)
    reached = {problem.initial: start_node}

    while frontier:
        #print("Frontier before pop:", [(manhatan_distance(n.position,end), n.position) for _, n in frontier])  # Imprime el contenido de frontier antes de pop
        _, node = heapq.heappop(frontier)
        if node.position == end:
            return reconstruct_path(node)

        neighbors, move=get_neighbors(node.position)
        for i,neighbor in enumerate(neighbors): #obtener vecinos posibles a partir de la posición del nodo
            new_cost = node.path_cost + problem.action_cost #todos los movimientos tienen costo de 1
            if neighbor not in reached or new_cost < reached[neighbor].path_cost:
                reached[neighbor] = Node(neighbor, parent=node, action=move[i], path_cost=new_cost)
                heapq.heappush(frontier, (manhatan_distance(neighbor, end), reached[neighbor]))

    return None  # No se encontró salida

def reconstruct_path(node):
    path_actions = []
    path=[]
    while node:
        path_actions.append(node.action)
        path.append(node.position)
        node = node.parent
    path.reverse()
    path_actions.reverse()
    return path, path_actions

maze = [
    ["#", "#", "#", "#", "#", "#", "#","#"],
    ["#", "S", "#", " ", "#", " ", "E","#"],
    ["#", " ", " ", " ", "#", " ", " ","#"],
    ["#", " ", "#", " ", " ", " ", "#","#"],
    ["#", "#", "#", "#", "#", "#", "#","#"],
    ["#", "#", "#", "#", "#", "#", "#","#"]
]

path, path_act = find_exit(maze)
print("Path to exit:", path)
print("Path actions to exit:", path_act)