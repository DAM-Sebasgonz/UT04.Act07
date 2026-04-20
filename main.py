from logica.gestor import GestorPartida

juego = GestorPartida()
juego.anadir_jugador("Nacho", "lobo")
juego.anadir_jugador("Elena", "vidente")
juego.anadir_jugador("Carlos", "aldeano")

print(juego.jugadores[0].accion_nocturna(juego.jugadores[2]))

print(f"Estado de Carlos: {'Vivo' if juego.jugadores[2].esta_vivo else 'Muerto'}")

print(juego.votacion_dia("Nacho"))

print(juego.comprobar_victoria())
