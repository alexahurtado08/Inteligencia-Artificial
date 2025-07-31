import heapq

# Diccionario de rutas entre ciudades con costos (distancias en km)
rutas_colombia = {
    "Medellín": {"Manizales": 190, "Pereira": 215, "Bogotá": 415},
    "Bogotá": {"Medellín": 415, "Ibagué": 195, "Neiva": 310, "Bucaramanga": 400},
    "Cali": {"Pereira": 210, "Ibagué": 240, "Neiva": 250},
    "Barranquilla": {"Cartagena": 110, "Bucaramanga": 680},
    "Cartagena": {"Barranquilla": 110},
    "Bucaramanga": {"Bogotá": 400, "Barranquilla": 680},
    "Pereira": {"Medellín": 215, "Cali": 210, "Manizales": 55},
    "Manizales": {"Medellín": 190, "Pereira": 55, "Ibagué": 130},
    "Ibagué": {"Bogotá": 195, "Cali": 240, "Manizales": 130, "Neiva": 140},
    "Neiva": {"Bogotá": 310, "Cali": 250, "Ibagué": 140}
}

# Algoritmo de búsqueda de costo uniforme
def uniform_cost_search(grafo, inicio, objetivo):
    frontera = [(0, inicio, [inicio])]  # (costo acumulado, ciudad actual, camino)
    visitados = set()

    while frontera:
        costo, ciudad_actual, camino = heapq.heappop(frontera)

        if ciudad_actual == objetivo:
            print("\nRuta encontrada:")
            print(" -> ".join(camino))
            print(f"Distancia total: {costo} km")
            return

        if ciudad_actual in visitados:
            continue

        visitados.add(ciudad_actual)

        for vecino, costo_vecino in grafo.get(ciudad_actual, {}).items():
            if vecino not in visitados:
                heapq.heappush(frontera, (costo + costo_vecino, vecino, camino + [vecino]))

    print("No se encontró una ruta.")


uniform_cost_search(rutas_colombia, ""Medellín")
uniform_cost_search(rutas_colombia, "Medellín",  "Ibagué")