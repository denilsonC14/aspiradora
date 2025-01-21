import time

# Datos de entrada
estados = [[4, 0, 1], [3, 0, 1], [6, 2, 3], [3, 2, 3], [4, 4, 5], [7, 4, 5], [6, 6, 7], [7, 6, 7]]
terminar = [6, 7]
acciones = ["Limpiar", "Izquierda", "Derecha", "Apagar"]
estadoInicial = 4

def formular(estados, terminar, acciones, estado1):
    propositos = []  # Caminos para recorrer
    estado = estado1
    propositos.append(estado)

    # Mapeo de acciones a índices
    accion_a_indice = {"Limpiar": 0, "Izquierda": 1, "Derecha": 2}
    visitados = set()  # Para rastrear los estados ya visitados y evitar repeticiones

    while True:  # Continuar hasta alcanzar un estado terminal o repetir un estado
        if estado in terminar:
            propositos.append("Apagar")
            break
        visitados.add(estado)
        cambios = False  # Para rastrear si el estado ha cambiado en este ciclo

        for accion in acciones[:-1]:  # Excluir "Apagar" de las acciones directas
            accion_idx = accion_a_indice[accion]  # Convertir acción a índice
            nestado = estados[estado][accion_idx]
            if nestado != estado and nestado not in visitados:  # Cambiar si el nuevo estado no es repetido
                propositos.append(accion)
                propositos.append(nestado)
                estado = nestado  # Actualizar al nuevo estado
                cambios = True
                break
        if not cambios:  # Si no hubo cambios, evitar un bucle infinito
            break
    return propositos

def busqueda(propon):
    resultado = []
    for elem in propon:
        if elem == "Apagar":
            break
        resultado.append(elem)
    return resultado

# Medición de tiempo
start_time = time.time()

# Ejecutar la simulación
propon = formular(estados, terminar, acciones, estadoInicial)

# Medición de tiempo al final de la ejecución de formular
end_time = time.time()
formular_time = end_time - start_time

# Guardar las proposiciones y acciones
acciones_guardadas = busqueda(propon)

# Mostrar las acciones guardadas y filtradas
print("Proposiciones***")
print(propon)
print("Acciones a realizar****")
print(acciones_guardadas)

# Tiempo de ejecución
print(f"Tiempo de ejecución de formular: {formular_time:.6f} segundos")
