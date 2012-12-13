import pilas
import random
#pilas.iniciar()
class Enemigo(pilas.actores.Actor):
    def __init__(self,imagen,x,y,dy=1,dx=1):
        pilas.actores.Actor.__init__(self,imagen)
        #self.imagen = pilas.imagenes.cargar("personajes/enemigo3.png")
        self.aprender(pilas.habilidades.SeMantieneEnPantalla)
        self.aprender(pilas.habilidades.SeMantieneEnPantalla)
        self.aprender(pilas.habilidades.PuedeExplotar)
        self.radio_de_colision=38
        self.x=x
        self.y=y
        self.dy=dy
        self.dx=dx
    def actualizar(self):
        self.y-=self.dy
        self.x+=self.dx