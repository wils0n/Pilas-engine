import pilas

#pilas.iniciar()
class MiTanque(pilas.actores.Actor):
        def __init__(self,x=0,y=0):
            pilas.actores.Actor.__init__(self)
            self.imagen = pilas.imagenes.cargar("personajes/arriba.png")
            #self.municion=pilas.actores.proyectil.Misil
            self.municion=pilas.actores.proyectil.Bala

            #self.aprender(pilas.habilidades.Disparar)
        def actualizar(self):
            if pilas.escena_actual().control.arriba:
                self.y += 1
                self.imagen = pilas.imagenes.cargar("personajes/arriba.png")
                self._calibrar_disparo(0,(0,0))
            if pilas.escena_actual().control.abajo:
                self.y -= 1
                self.imagen = pilas.imagenes.cargar("personajes/abajo.png")
                self._calibrar_disparo(180,(0,-60))
            if pilas.escena_actual().control.izquierda:
                self.x -= 1
                self.imagen = pilas.imagenes.cargar("personajes/izquierda.png")
                self._calibrar_disparo(90,(-30,-30))
            if pilas.escena_actual().control.derecha:
                self.x += 1
                self.imagen = pilas.imagenes.cargar("personajes/derecha.png")
                self._calibrar_disparo(-90,(30,-30))

        def _calibrar_disparo(self,direc,ori):
                self.aprender(pilas.habilidades.Disparar,municion=self.municion,angulo_salida_disparo=direc,frecuencia_de_disparo=6,escala=0.7,offset_disparo=(29,29),offset_origen_actor=ori)

MiTanque()
pilas.ejecutar()        