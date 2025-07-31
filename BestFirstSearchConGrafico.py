import networkx as nx
import matplotlib.pyplot as plt

# Diccionario de rutas
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

# Crear grafo dirigido
G = nx.DiGraph()

# Agregar aristas con peso
for origen, destinos in rutas_colombia.items():
    for destino, peso in destinos.items():
        G.add_edge(origen, destino, weight=peso)

# Posiciones automáticas
pos = nx.spring_layout(G, seed=42)

# Dibujar nodos y aristas
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color='skyblue')
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)
nx.draw_networkx_labels(G, pos, font_size=10)

# Dibujar pesos (distancias)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.title("Grafo de Rutas entre Ciudades de Colombia")
plt.axis('off')
plt.tight_layout()
plt.show()