import pilas
from  pilas.actores import Bomba

class BombaConMovimiento(Bomba):
    def __init__(self,x=0,y=0):
        Bomba.__init__(self,x,y)
    def actualizar(self):
        self.x+=0.5
        self.y+=0.5
        
        if self.x>320:
            self.x=-320
        if self.y>240:
            self.y=-240
            
def main():
    pilas.iniciar()
    protagonista=pilas.actores.Aceituna()
    protagonista.aprender(pilas.habilidades.SeguirAlMouse)
    bomba_1=BombaConMovimiento()
    bomba_2=BombaConMovimiento(x=200,y=0)
    bomba_3=BombaConMovimiento(x=0,y=200)
    
    pilas.ejecutar()
main()