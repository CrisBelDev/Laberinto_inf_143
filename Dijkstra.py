import heapq

class Laberinto_Dijkstra:
    def encontrar_caminos(self, lab):
        # Convertir el laberinto en un grafo ponderado
        grafo = self.crear_grafo(lab)

        # Definir el nodo de inicio y las distancias iniciales
        inicio = (0, 0)
        distancias = {nodo: float('inf') for nodo in grafo}
        distancias[inicio] = 0

        # Implementar el algoritmo de Dijkstra
        cola_prioridad = [(0, inicio)]
        while cola_prioridad:
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

            if distancia_actual > distancias[nodo_actual]:
                continue

            if nodo_actual == self.meta:
                break

            for vecino, peso in grafo[nodo_actual]:
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(cola_prioridad, (distancia, vecino))

        # Obtener los caminos de menor longitud
        caminos = self.obtener_caminos_menores(distancias, lab)
        return caminos

    def crear_grafo(self, lab):
        grafo = {}
        filas = len(lab)
        columnas = len(lab[0])

        for i in range(filas):
            for j in range(columnas):
                if lab[i][j] != 1:
                    nodo_actual = (i, j)
                    vecinos = []

                    if i > 0 and lab[i-1][j] != 1:
                        vecinos.append(((i-1, j), 1))
                    if i < filas-1 and lab[i+1][j] != 1:
                        vecinos.append(((i+1, j), 1))
                    if j > 0 and lab[i][j-1] != 1:
                        vecinos.append(((i, j-1), 1))
                    if j < columnas-1 and lab[i][j+1] != 1:
                        vecinos.append(((i, j+1), 1))

                    grafo[nodo_actual] = vecinos
        
        return grafo

    def obtener_caminos_menores(self, distancias, lab):
        filas = len(lab)
        columnas = len(lab[0])
        menor_distancia = distancias.get(self.meta, float('inf'))

        caminos = []
        if menor_distancia < float('inf'):
            self.dfs_obtener_caminos(self.meta, lab, [], caminos, distancias, menor_distancia)

        return caminos

    def dfs_obtener_caminos(self, nodo, lab, camino_actual, caminos, distancias, menor_distancia):
        if nodo == (0, 0):
            camino_actual.append(nodo)
            caminos.append(camino_actual[::-1])
            camino_actual.pop()
            return

        camino_actual.append(nodo)

        for vecino, _ in self.obtener_vecinos_validos(nodo, lab):
            if distancias[vecino] == menor_distancia - 1:
                self.dfs_obtener_caminos(vecino, lab, camino_actual, caminos, distancias, menor_distancia - 1)

        camino_actual.pop()

    def obtener_vecinos_validos(self, nodo, lab):
        filas = len(lab)
        columnas = len(lab[0])
        i, j = nodo

        vecinos = []
        if i > 0 and lab[i-1][j] != 1:
            vecinos.append(((i-1, j), 1))
        if i < filas-1 and lab[i+1][j] != 1:
            vecinos.append(((i+1, j), 1))
        if j > 0 and lab[i][j-1] != 1:
            vecinos.append(((i, j-1), 1))
        if j < columnas-1 and lab[i][j+1] != 1:
            vecinos.append(((i, j+1), 1))

        return vecinos

"""
# Crear una instancia de la clase Laberinto
laberinto = Laberinto_Dijkstra()

# Definir el laberinto como una matriz bidimensional
lab = [
    [0, 1, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 2]
]

# Obtener la posición de la meta en el laberinto
filas = len(lab)
columnas = len(lab[0])
meta = None
for i in range(filas):
    for j in range(columnas):
        if lab[i][j] == 2:
            meta = (i, j)
            break
    if meta is not None:
        break

laberinto.meta = meta

# Llamar a la función encontrar_caminos de la instancia laberinto
caminos = laberinto.encontrar_caminos(lab)

# Imprimir los caminos encontrados
contador = 1
for camino in caminos:
    print(contador, "tamaño:", len(camino) - 1, ":", camino)
    contador += 1
    print()
"""