import math

def distancia_euclidiana(origenX, origenY, destinoX, destinoY):
    valor1=math.pow((destinoX-origenX),2)
    valor2=math.pow((destinoY-origenY),2)
    distancia=round(math.sqrt(valor1+valor2),2)
    return distancia

def puntos_mas_cercanos(puntos_lista) -> list:
    resultado = []
    for punto1 in puntos_lista:
        x1 = punto1[0]
        y1 = punto1[1]
        distancia_min = 1000
        cercano = (0,0)
        for punto_2 in puntos_lista:
            if punto1 != punto_2:
                x2 = punto_2[0] 
                y2 = punto_2[1] 
                distancia = distancia_euclidiana(x1, y1, x2, y2)
                if distancia < distancia_min:
                    distancia_min = distancia
                    cercano = (x2, y2)
        resultado.append((punto1, cercano))
    return resultado