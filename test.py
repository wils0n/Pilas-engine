import pilas
from miNave import MiNave

pilas.iniciar()
b=MiNave()
naves=pilas.atajos.fabricar(pilas.actores.Dinamita,10)
b.definir_enemigos(naves)

pilas.ejecutar()