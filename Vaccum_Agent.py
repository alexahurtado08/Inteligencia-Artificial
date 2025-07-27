import random

# Función que decide la acción del agente según su ubicación y si la celda está sucia
def action_vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"  # Si el lugar está sucio, lo limpia
    elif location == "A":
        return "Right"  # Si está limpio y está en A, se mueve a la derecha (B)
    elif location == "B":
        return "Down"   # Si está limpio y está en B, baja a D
    elif location == "C":
        return "Up"     # Si está limpio y está en C, sube a A
    elif location == "D":
        return "Left"   # Si está limpio y está en D, va a la izquierda (C)

# Función que define cómo responde el entorno al movimiento del agente
def move(location, action):
    # Diccionario que representa las conexiones válidas entre celdas
    movement = {
        "A": {"Right": "B", "Down": "C"},
        "B": {"Left": "A", "Down": "D"},
        "C": {"Right": "D", "Up": "A"},
        "D": {"Left": "C", "Up": "B"}
    }
    # Retorna la nueva ubicación del agente si la acción es válida desde esa celda
    return movement.get(location, {}).get(action, location)

# Función que evalúa si ya todas las celdas del mundo están limpias
def is_world_clean(world):
    return all(state == "Clean" for state in world.values())

# Función principal que simula el comportamiento del agente en el entorno
def simulate_vacuum_agent():
    # Generar estado inicial aleatorio: cada celda puede estar "Dirty" o "Clean"
    world = {loc: random.choice(["Dirty", "Clean"]) for loc in ["A", "B", "C", "D"]}

    
    # Posición inicial del agente
    location = "A"

    # Lista para guardar las acciones realizadas
    actions = []

    # Contador de pasos
    steps = 0

    # El bucle continúa hasta que todas las celdas estén limpias
    while not is_world_clean(world):
        # Obtener el estado (sucio/limpio) de la celda actual
        status = world[location]

        # Decidir qué hacer: limpiar o moverse
        action = action_vacuum_agent(location, status)

        # Guardar la acción tomada en la lista
        actions.append((location, action))

        # Contar el paso
        steps += 1

        # Ejecutar la acción: si limpia, cambia el estado a "Clean"
        if action == "Suck":
            world[location] = "Clean"
        else:
            # Si se mueve, actualizar la ubicación según la acción
            location = move(location, action)

    # Retornar lista de acciones, estado final del mundo y número de pasos
    return actions, world, steps


# Ejecutar la simulación
actions, final_world_state, steps = simulate_vacuum_agent()

# Mostrar las acciones realizadas paso a paso
print("Actions taken by the agent:")
for loc, act in actions:
    print(f"In location {loc} -> Action: {act}")

# Mostrar el estado final del mundo después de que el agente termina
print(" Final world state:", final_world_state)

# Mostrar cuántos pasos se necesitaron
print(f" Total steps taken: {steps}")
