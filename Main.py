# declarando objetos
from Laberinto import Game_laberinto as gm
from ventana import Ventana
if __name__ == "__main__":

    lab = [
        [0, 1, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 2]
    ]
    lab1 = [
[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,1],
[1,1,1,1,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,1,1],
[1,0,0,0,0,0,0,0,1,0,1,1,1,0,0,1,0,1,1,1,1,1,0,1,0,1],
[1,0,1,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1],
[1,0,1,0,0,0,0,0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1],
[1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1],
[1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,0,0,0,1,0,0,0,1,0,1],
[1,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,0,1,1,1,1,1,0,1,0,1],
[1,0,0,0,1,0,0,1,1,0,1,0,1,0,0,1,0,0,1,0,0,1,0,1,0,1],
[1,0,0,1,1,0,0,1,1,0,1,0,1,0,0,1,0,0,1,0,1,1,0,1,0,1],
[1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1],
[1,0,0,1,0,1,1,1,1,0,0,0,1,0,0,1,1,1,1,0,1,0,1,0,0,1],
[1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,2]

]
    """obj = gm()
    
    res = obj.tiene_salida(lab)
    print("Tiene salida:", res)
    caminos = obj.encontrar_caminos(lab)
    print("Caminos posibles:")
    for i, camino in enumerate(caminos):
        print("Camino", i+1, ": tamaño: ",str(len(camino)), camino)
        print()
"""
    obj_ventana = Ventana(lab)
    obj_ventana.ejecutar_juego()

    
    

 
