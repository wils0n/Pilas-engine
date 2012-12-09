'''
Falta ordenar y mucho mas, este archivo esta mas desordenado que me de roxe XD
'''

import pilas
from personaje import Zerox
from enemigo import Enemigo
pilas.iniciar(titulo="Juego en 4 horas sin saber NADA")
sonido = pilas.sonidos.cargar('sonidos/photosintesis.m4a')
sonido.reproducir()

def dibujar_mapa():
    grilla=pilas.imagenes.cargar_grilla("grillas/tileset.png", 15, 33)
    mapa=pilas.actores.Mapa(grilla)
    
    
    #mapa.pintar_bloque(8, 11, 465)#grass
    for i in range(18):
        for j in range(20):
            mapa.pintar_bloque(i, j, 465,es_bloque_solido=False)
    for i in range(2,20):        
        mapa.pintar_bloque(13,i, 450)# fila, columna, [muro]
    
    for i in range(18):
        mapa.pintar_bloque(16, i, 467)#muro fila, columna, [arbol]
    for i in range(14):
        mapa.pintar_bloque(11, i, 450)#muro fila, columna, [muro]
    for i in range(15,20):
        mapa.pintar_bloque(11, i, 450)#muro fila, columna, [muro]
        
    for i in range(2,20):
        mapa.pintar_bloque(9, i, 450)#muro fila, columna, [muro]
            
    for i in range(19):
        mapa.pintar_bloque(7, i, 450)#muro fila, columna, [muro]
    for i in range(10,20):
        mapa.pintar_bloque(5, i, 450)#muro fila, columna, [muro]
    for i in range(9):
        mapa.pintar_bloque(5, i, 450)#muro fila, columna, [muro]
            
    for i in range(13):
        mapa.pintar_bloque(1, i, 467)#muro fila, columna, [arbol]
        mapa.pintar_bloque(2, i, 467)#muro fila, columna, [arbol]
        mapa.pintar_bloque(3, i, 467)#muro fila, columna, [arbol]
    
    for i in range(13,19):
        mapa.pintar_bloque(1, i, 291)#muro fila, columna, [flores]
        mapa.pintar_bloque(2, i, 291)#muro fila, columna, [flores]
        mapa.pintar_bloque(3, i, 291)#muro fila, columna, [flores]
    mapa.pintar_bloque(1, 19, 461,es_bloque_solido=False)#muro fila, columna, [flores]
    mapa.pintar_bloque(2, 19, 461,es_bloque_solido=False)#muro fila, columna, [flores]
    mapa.pintar_bloque(3, 19, 461,es_bloque_solido=False)#muro fila, columna, [flores]
    
    return mapa

mapa=dibujar_mapa()

actor=Zerox(mapa)
actor.radio_de_colision=15
actor.x=280
actor.y=-230
actor.aprender(pilas.habilidades.PuedeExplotar)
actor.aprender(pilas.habilidades.Disparar)

enemigo1=Enemigo(0,0)
enemigo2=Enemigo(125,125)
enemigo3=Enemigo(240,-60)
enemigos=[]
enemigos.append(enemigo1)
enemigos.append(enemigo2)
enemigos.append(enemigo3)

def perdiste(actor,enemigos):
    actor.eliminar()

pilas.escena_actual().colisiones.agregar(actor, enemigos, perdiste)

pilas.ejecutar()