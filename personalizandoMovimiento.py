import pilas
def avanzar():

    pilas.iniciar()
    
    class MiActor(pilas.actores.Actor):
    
        def __init__(self):
            pilas.actores.Actor.__init__(self)
            self.imagen = pilas.imagenes.cargar("grillas/3.png")
    
        def actualizar(self):
            if pilas.escena_actual().control.izquierda:
                self.x -= 10
    
            if pilas.escena_actual().control.derecha:
                self.x += 10
    
    MiActor()
    pilas.ejecutar()

avanzar()