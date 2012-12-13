import pilas
from miNave import MiNave
from enemigo2 import Enemigo

pilas.iniciar(titulo="No al Software Privativo")
#pilas.fondos("mapas/espacio.jpg")
pilas.fondos.Espacio()
nave=MiNave()
e0=Enemigo("personajes/mocosoft.png",0,200,dx=0,dy=0)
e1=Enemigo("personajes/enemigo3.png",0,260,dx=1,dy=2)
e2=Enemigo("personajes/enemigo3.png",100,260,dx=0,dy=1)
e3=Enemigo("personajes/enemigo3.png",-100,260,dx=1.2,dy=1)
e4=Enemigo("personajes/enemigo3.png",-200,260,dx=-0.3,dy=1.2)
e5=Enemigo("personajes/enemigo3.png",-300,260,dx=-0.5,dy=1.3)
enemigos=[e0]
enemigos.append(e1)
enemigos.append(e2)
enemigos.append(e3)
enemigos.append(e4)
enemigos.append(e5)

def explotar(nave,enemigos):
    nave.eliminar()
    
pilas.escena_actual().colisiones.agregar(nave,enemigos,explotar)
nave.definir_enemigos(enemigos)
mensaje1 = pilas.actores.Texto("NO al software\n   PRIVATIVO")
mensaje1.x=-230
mensaje1.y=230

pilas.ejecutar()
