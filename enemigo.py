'''
al enemigo le un movimiento mas bonito, ya qur ahora solo se va a un lado XD
'''

import pilas
import random
#pilas.iniciar()
class Enemigo(pilas.actores.Actor):
    def __init__(self,x,y):
        pilas.actores.Actor.__init__(self)
        self.imagen = pilas.imagenes.cargar("personajes/enemigo2.png")
        #enemigo = pilas.actores.Actor(imagen)
        self.aprender(pilas.habilidades.SeMantieneEnPantalla)
        self.aprender(pilas.habilidades.PuedeExplotar)
        #self.dy = random.choice(posibles_velocidades) / 10.0
        self.posicionX = random.randint(-240,240)
        #self.dy=random.randint(1,2)
        self.x=x
        self.y=y
    def actualizar(self):
        self.x+=1
        
#e=Enemigo(0,0)
#pilas.ejecutar()