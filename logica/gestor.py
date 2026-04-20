from personajes.clases import JugadorDelJuego


class GestorPartida:
    def __init__(self):
        self.jugadores = []

    def anadir_jugador(self, nombre, tipo_rol):
        self.jugadores.append(JugadorDelJuego(nombre, tipo_rol))

    def votacion_dia(self, nombre_votado):
        for j in self.jugadores:
            if j.nombre == nombre_votado:
                if j.esta_vivo:
                    j.esta_vivo = False
                    return (
                        "El pueblo ha linchado a " + nombre_votado + " en la hoguera."
                    )
        return "Nadie fue linchado."

    def comprobar_victoria(self):
        lobos_vivos = 0
        otros_vivos = 0

        for j in self.jugadores:
            if j.esta_vivo:
                if j.rol == "lobo":
                    lobos_vivos += 1
                else:
                    otros_vivos += 1

        if lobos_vivos >= otros_vivos:
            return "Victoria de los Lobos"
        elif lobos_vivos == 0:
            return "Victoria de los Aldeanos"
        return "La partida debe continuar..."
