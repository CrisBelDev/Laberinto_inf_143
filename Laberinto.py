class Game_laberinto:
    def tiene_salida(self, lab):
        memo = [[-1] * len(lab[0]) for _ in range(len(lab))]
        return self.tiene_salida_recursiva(lab, 0, 0, memo)
    
    def tiene_salida_recursiva(self, lab, i, j, memo):
        if 0 <= i < len(lab) and 0 <= j < len(lab[i]):
            if lab[i][j] == 2:
                return True
            elif lab[i][j] == 1:
                return False
            elif memo[i][j] != -1:
                return memo[i][j]
            else:
                lab[i][j] = 1  # marcado
                res = self.tiene_salida_recursiva(lab, i - 1, j, memo) or self.tiene_salida_recursiva(lab, i + 1, j, memo) or \
                      self.tiene_salida_recursiva(lab, i, j - 1, memo) or self.tiene_salida_recursiva(lab, i, j + 1, memo)
                lab[i][j] = 0  # desmarcado
                memo[i][j] = res
                return res
        else:
            return False
    
    def encontrar_caminos(self, lab):
        memo = [[[] for _ in range(len(lab[0]))] for _ in range(len(lab))]
        caminos = []
        self.encontrar_caminos_recursiva(lab, 0, 0, [], caminos, memo)
        return caminos
    
    def encontrar_caminos_recursiva(self, lab, i, j, camino_actual, caminos, memo):
        if 0 <= i < len(lab) and 0 <= j < len(lab[i]):
            if len(caminos) > 10:
                return

            if lab[i][j] == 2:
                camino_actual.append((i, j))
                caminos.append(camino_actual.copy())
                camino_actual.pop()
            elif lab[i][j] == 0:
                if memo[i][j]:
                    for camino in memo[i][j]:
                        caminos.append(camino_actual + camino)
                else:
                    lab[i][j] = 1  # marcado
                    camino_actual.append((i, j))
                    self.encontrar_caminos_recursiva(lab, i - 1, j, camino_actual, caminos, memo)  # ir arriba
                    self.encontrar_caminos_recursiva(lab, i + 1, j, camino_actual, caminos, memo)  # ir abajo
                    self.encontrar_caminos_recursiva(lab, i, j + 1, camino_actual, caminos, memo)  # ir derecha
                    self.encontrar_caminos_recursiva(lab, i, j - 1, camino_actual, caminos, memo)  # ir izquierda
                    camino_actual.pop()
                    lab[i][j] = 0  # desmarcado
                    memo[i][j] = caminos[len(caminos) - len(memo[i][j]):]
    
"""    def main(self):
        obj = Game_laberinto()
        lab = [
            [0, 1, 0, 1, 1],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 2]
        ]
        lab1 = [
           
            [0,0,1,0,0,0,0,0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1],
            [1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1],
            [1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,0,0,0,1,0,0,0,1,0,1],
            [1,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,0,1,1,1,1,1,0,1,0,1],
            [1,0,0,0,1,0,0,1,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1],
            [1,0,0,1,1,0,0,1,1,0,1,0,1,0,0,1,0,0,1,0,1,1,0,1,0,1],
            [1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,1,0,1,1,1,1,0,0,0,1,0,0,1,1,1,1,0,1,0,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,2]

        ]
        res = obj.tiene_salida(lab)
        print("Tiene salida:", res)
        
        caminos = obj.encontrar_caminos(lab)
        print("Caminos posibles:")
        for i, camino in enumerate(caminos):
            print("Camino", i+1, ":", camino)
    
    
if __name__ == "__main__":
    obj = Game_laberinto()
    obj.main()
"""