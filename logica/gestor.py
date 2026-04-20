from personajes.clases import JugadorDelJuego


class GestorPartida:
    """Clase que gestiona la partida de "Hombres Lobo de Castronegro".
    Se encarga de mantener la lista de jugadores, gestionar las votaciones y comprobar las condiciones de victoria.
    """

    def __init__(self):
        """Inicializa el gestor de partida con una lista vacía de jugadores."""
        self.jugadores = []

    def anadir_jugador(self, nombre, tipo_rol):
        """Añade un nuevo jugador a la partida con su nombre y tipo de rol."""
        self.jugadores.append(JugadorDelJuego(nombre, tipo_rol))

    def votacion_dia(self, nombre_votado):
        """Realiza la votación del día para linchar a un jugador."""
        for j in self.jugadores:
            if j.nombre == nombre_votado:
                if j.esta_vivo:
                    j.esta_vivo = False
                    return (
                        "El pueblo ha linchado a " + nombre_votado + " en la hoguera."
                    )
        return "Nadie fue linchado."

    def comprobar_victoria(self):
        """Comprueba las condiciones de victoria para determinar si los lobos o los aldeanos han ganado."""
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
