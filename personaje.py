from myBasePersonajeRPG import BasePersonajeRPG
class Zerox(BasePersonajeRPG):

    def __init__(self, mapa, x=0, y=0):
        BasePersonajeRPG.__init__(self, mapa, x=x, y=y, imagen="personajes/personaje.png", velocidad=2)
