
# Algoritmo de Dijkstra = Caminos mínimos

sin_visitar = {'A', 'B', 'C', 'D', 'E', 'C'}  

distancias = {('A', 'B'): 6, ('A', 'D'): 1, ('B', 'C'): 5, ('B', 'D'): 2, ('B', 'E'):2, ('D', 'E'): 1, ('E','C'): 5,
             ('B', 'A'): 6, ('D', 'A'): 1, ('C', 'B'): 5, ('D', 'B'): 2, ('E', 'B'):2, ('E', 'D'): 1, ('C','E'): 5}

vecinos = {
                'A': ['B', 'D'],
                'B': ['A', 'D', 'C'],
                'C': ['B', 'E'],
                'D': ['A', 'B', 'E'],
                'E': ['D', 'B', 'C']
              }


def dijkstra(sin_visitar, distancias, vecinos, inicio):

    # Distancia desde el vértice inicial = 0. Distancia de los otros vértices = infinito.
    # key: value for value in iterable for condition
    # Se lee así: "Para cada elemento en el iterable, esa llave y ese valor, solo si se cumple la condición" 
    conocido = {vertice: 0 if vertice == inicio else float('inf') for vertice in sin_visitar}

    # El nodo anterior es desconocido para cada vertex
    anterior = {vertice: None for vertice in sin_visitar}

    # Repetir hasta que no queden vértices para visitar
    while len(sin_visitar) > 0:

        # Visitar los no_vistados con la menor distancia desde el vértice inicial
        distancia, visitar = min([(conocido[candidato], candidato) for candidato in sin_visitar])
        # Para el vértice actual, calcular la distancia desde el vértice visitado hasta cada uno de sus vecinos.
        calculado = {vecino: distancia + distancias[visitar, vecino] for vecino in vecinos[visitar]}

        # Actualizar las distancias anteriores y conocidas si la distancia calculada es menor que la distancia conocida.
        anterior.update( {vertice: visitar if calculado[vertice] < conocido[vertice] else anterior[vertice] for vertice in vecinos[visitar]} )
        conocido.update( {vertice: calculado[vertice] if calculado[vertice] < conocido[vertice] else conocido[vertice] for vertice in vecinos[visitar]})

        # Remover el vertice actual visitado del ocnjunto de los visitados:
        sin_visitar.remove(visitar)

    # Return las mejores distancias ocnocidas y sus correspondientes nodos previos
    return conocido, anterior


minimas, predecesores = dijkstra(sin_visitar, distancias, vecinos, 'A')
minimas, predecesores = sorted(minimas.items()), sorted(predecesores.items())
print('Distancias minimas: \n {} \nPredecesores: \n {}'.format(minimas, predecesores))