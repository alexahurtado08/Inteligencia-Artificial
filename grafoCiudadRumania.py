import heapq  # Importa heapq para usar una cola de prioridad (mínimo primero)

# Función para encontrar la ruta más corta usando Dijkstra
def recorrido(grafo, inicio, destino):
    # Cola de prioridad: (distancia acumulada, ciudad actual, camino recorrido)
    cola = [(0, inicio, [inicio])]
    visitados = set()  # Conjunto para evitar visitar nodos repetidos

    while cola:
        distancia, ciudad_actual, camino = heapq.heappop(cola)

        if ciudad_actual in visitados:
            continue
        visitados.add(ciudad_actual)

        # Si llegamos al destino, retornamos la distancia y el camino
        if ciudad_actual == destino:
            return distancia, camino

        # Explora vecinos no visitados y agrega a la cola con la distancia actualizada
        for vecino, peso in grafo.get(ciudad_actual, {}).items():
            if vecino not in visitados:
                heapq.heappush(cola, (distancia + peso, vecino, camino + [vecino]))

    return float("inf"), []  # Si no hay camino, retorna infinito

# Diccionario con las distancias entre ciudades 
distancias = {
    'Arad': {'Sibiu': 140, 'Timisoara': 118, 'Zerind': 75},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80, 'Oradea': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Bucharest': 101, 'Craiova': 138},
    'Craiova': {'Rimnicu Vilcea': 146, 'Drobeta': 120, 'Pitesti': 138},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Craiova': 120, 'Mehadia': 75},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Urziceni': 85, 'Giurgiu': 90},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

# Solicita al usuario las ciudades de origen y destino
input_data = input("Ingrese el origen y destino (separados por coma): ")
origen, destino = input_data.split(',')


# Llama la función y muestra la ruta más corta
distancia, ruta = recorrido(distancias, origen, destino)
print(f"Ruta más corta de {origen} a {destino}: {' -> '.join(ruta)} (Distancia: {distancia} km)")
