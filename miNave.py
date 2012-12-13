
import pilas
from pilas.actores import Animacion
import math


class MiNave(Animacion):
    def __init__(self, x=0, y=0, velocidad=2):
        self.velocidad = velocidad
        grilla = pilas.imagenes.cargar_grilla("personajes/minave6.png", 1)
        Animacion.__init__(self, grilla, ciclica=True, x=x, y=y)
        self.radio_de_colision = 20
        self.aprender(pilas.habilidades.PuedeExplotar)

        self.municion = pilas.actores.proyectil.Bala
        self.aprender(pilas.habilidades.Disparar,
                       municion=self.municion,
                       angulo_salida_disparo=0,
                       frecuencia_de_disparo=6,
                       offset_disparo=(29,29),
                       escala=0.7)

        self.aprender(pilas.habilidades.MoverseConElTeclado,
                      velocidad_maxima=self.velocidad,
                      aceleracion=1,
                      deceleracion=0.04,
                      con_rotacion=True,
                      velocidad_rotacion=1,
                      marcha_atras=False)

    def actualizar(self):
        Animacion.actualizar(self)

    def definir_enemigos(self, grupo, cuando_elimina_enemigo=None):
        self.cuando_elimina_enemigo = cuando_elimina_enemigo
        self.habilidades.Disparar.definir_colision(grupo, self.hacer_explotar_al_enemigo)

    def hacer_explotar_al_enemigo(self, mi_disparo, el_enemigo):
        mi_disparo.eliminar()
        el_enemigo.eliminar()

        if self.cuando_elimina_enemigo:
            self.cuando_elimina_enemigo()
