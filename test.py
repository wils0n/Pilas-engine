import pilas
from tanque import MiTanque
def main():
    pilas.iniciar()
    pilas.fondos.Pasto()
    
    grilla = pilas.imagenes.cargar_grilla("mapas/muros1.png", 3, 3)
    mapa = pilas.actores.Mapa(grilla)
    
    mapa.pintar_bloque(14, 19, 1)
    mapa.pintar_bloque(14, 18, 1)
    mapa.pintar_bloque(14, 17, 1)
    mapa.pintar_bloque(14, 16, 1)
    
    for columna in range(20):
        mapa.pintar_bloque(2, columna, 1,es_bloque_solido=True)
    
    for columna in range(10):
        mapa.pintar_bloque(14, columna, 1,es_bloque_solido=False)
    
    #objetos=pilas.atajos.fabricar(pilas.actores.Pelota,20)
    
    MiTanque()
    pilas.ejecutar()
    
main()

#debe disparar cuando se mueve, por el momento tiene que parar para que dispare