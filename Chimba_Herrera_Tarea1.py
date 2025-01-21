# Libreria para calcular el tiempo
import time

# Datos de entrada
estados = [
    [3, 0, 1, 2], [4, 0, 1, 2], [5, 0, 1, 2], [3, 3, 19, 8],
    [4, 6, 4, 13], [5, 12, 7, 5], [9, 6, 4, 13], [16, 12, 7, 5],
    [11, 3, 19, 8], [9, 9, 10, 21], [10, 9, 10, 21], [11, 14, 20, 11],
    [14, 12, 7, 5], [15, 6, 4, 13], [14, 14, 20, 11], [15, 18, 16, 15],
    [16, 18, 16, 15], [17, 17, 23, 22], [17, 18, 16, 15], [10, 3, 19, 8],
    [23, 14, 20, 11], [22, 9, 10, 21], [22, 17, 23, 22], [23, 17, 23, 22]
]
terminar = [17, 22, 23]
acciones = ["Limpiar", "Izquierda", "Derecha", "Abajo", "Apagar"]
estadoInicial = 0

# Guardar las proposiciones y las acciones en una variable
acciones_guardadas = []

# Función para formular las proposiciones
def formular(estados, terminar, acciones, estado1):
    propositos = []  # caminos para recorrer
    estado = estado1
    propositos.append(estado)

    # Mapeo de acciones a índices
    accion_a_indice = {"Limpiar": 0, "Izquierda": 1, "Derecha": 2, "Abajo": 3}
    visitados = set()  # para rastrear los estados ya visitados y evitar repeticiones

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

# Función para guardar las acciones hasta "Apagar"
def busqueda(propon):
    resultado = []
    for elem in propon:
        if elem == "Apagar":
            break
        resultado.append(elem)
    return resultado

# Función para optimizar el trabajo
def eliminar_acciones_invalidas(acciones_guardadas):
    resultado = []  # Lista para almacenar las acciones válidas
    i = 0
    while i < len(acciones_guardadas):
        # Verificamos si encontramos el patrón: 'Limpiar', número, movimiento, número, movimiento
        if (i + 4 < len(acciones_guardadas) and
            acciones_guardadas[i] == 'Limpiar' and
            isinstance(acciones_guardadas[i + 1], int) and
            acciones_guardadas[i + 2] in ['Izquierda', 'Derecha', 'Abajo'] and
            isinstance(acciones_guardadas[i + 3], int) and
            acciones_guardadas[i + 4] in ['Izquierda', 'Derecha', 'Abajo']):
            
            # Agregar 'Limpiar', número y el segundo movimiento (sin el primer movimiento)
            resultado.append(acciones_guardadas[i])  # Mantener 'Limpiar'
            resultado.append(acciones_guardadas[i + 1])  # Mantener el número
            resultado.append(acciones_guardadas[i + 4])  # Mantener el segundo movimiento (y su número)
            
            # Avanzar 5 pasos (eliminamos el primer movimiento y su número)
            i += 5
        else:
            # Si no encontramos el patrón, agregar la acción tal como está
            resultado.append(acciones_guardadas[i])
            i += 1  

    return resultado

# Medir el tiempo de ejecución
start_time = time.time()
propon = formular(estados, terminar, acciones, estadoInicial)

# Guardar las proposiciones y acciones
acciones_guardadas = busqueda(propon)

# Filtramos las acciones inválidas
acciones_filtradas = eliminar_acciones_invalidas(acciones_guardadas)

# Mostrar las acciones guardadas y filtradas
print("Acciones guardadas****")
print(acciones_guardadas)
print("Acciones a realizar****")
print(acciones_filtradas)

# Calcular y mostrar el tiempo de ejecución
end_time = time.time()
execution_time = end_time - start_time
print(f"Tiempo de ejecución: {execution_time:.5f} segundos")
