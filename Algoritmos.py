#algoritmos py
import math #impprtamos math para la raiz 
def distancia_euclastina( x_1, y_1, x_2, y_2): #se define la funcion distancia con x1 y1 etc
     #por que son las que representan las coordenadas de dos puntos en el plano
    distancia = math.sqrt((x_2-x_1)**2 + (y_2-y_1)**2)#primero es la resta de las cordenasas de x 
    #al cuadrad, luego y al cuadrado y despues la raiz de la suma de estas restas 
    return distancia#nos regresa el resultado 

def puntos_mas_cercanos(puntos_list)->list:
    resultado = []
    for punto_i in puntos_list:
         x1 = punto_i[0]
         y1 = punto_i[1]
         min = 1000
         cercano = (0,0)
         for punto_j in puntos_list:
             if punto_i != punto_j:
                x2 = punto_j[0]
                y2 = punto_j[1]
                d = distancia_euclastina(x1,y1,x2,y2)
                if d < min:
                    min = d
                    cercano = (x2, y2)
            
         resultado.append((punto_i,cercano))
    return resultado

def kruskal(grafo):
    aristas = []

    # Obtener todas las aristas del grafo
    for origen, destinos in grafo.items():
        for destino, distancia in destinos:
            aristas.append((origen, destino, distancia))

    # Ordenar las aristas por distancia
    aristas.sort(key=lambda x: x[2])

    # Conjuntos disjuntos para controlar las componentes conectadas
    conjuntos_disjuntos = {vertice: {vertice} for vertice in grafo.keys()}

    aristas_mst = []  # Aristas del árbol de expansión mínima (Minimum Spanning Tree)

    for arista in aristas:
        origen, destino, distancia = arista

        if conjuntos_disjuntos[origen] != conjuntos_disjuntos[destino]:
            # Agregar la arista al árbol de expansión mínima
            aristas_mst.append(arista)

            # Unir los conjuntos disjuntos de los vértices conectados
            nuevo_conjunto = conjuntos_disjuntos[origen].union(conjuntos_disjuntos[destino])

            for vertice in nuevo_conjunto:
                conjuntos_disjuntos[vertice] = nuevo_conjunto
    print("Funciona")
    return aristas_mst


