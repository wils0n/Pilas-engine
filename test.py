import pilas

pilas.iniciar()
mono = pilas.actores.Mono()

pasos = 200

moverse_a_la_derecha = pilas.comportamientos.Avanzar(0, pasos)
moverse_a_la_izquierda = pilas.comportamientos.Avanzar(180, pasos)

mono.hacer_luego(moverse_a_la_derecha)
mono.hacer_luego(moverse_a_la_izquierda)

pilas.ejecutar()