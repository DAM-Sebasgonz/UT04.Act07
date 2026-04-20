class JugadorDelJuego:
    """Clase que representa a un jugador en la partida de "Hombres Lobo de Castronegro". Contiene su nombre, rol y estado de vida."""
    def __init__(self, nombre, rol):
        """Inicializa un jugador con su nombre, rol y estado de vida (vivo por defecto)."""
        self.nombre = nombre
        self.rol = rol
        self.esta_vivo = True

    def accion_nocturna(self, objetivo=None):
        """Realiza la acción nocturna del jugador según su rol. El objetivo es otro jugador que puede ser afectado por la acción."""
        if not self.esta_vivo:
            return f"{self.nombre} está muerto."

        if self.rol == "lobo":
            if objetivo:
                objetivo.esta_vivo = False
                return f"El lobo {self.nombre} ha eliminado a {objetivo.nombre}."
        elif self.rol == "vidente":
            if objetivo:
                return f"La vidente {self.nombre} ve que {objetivo.nombre} es {objetivo.rol}."
        elif self.rol == "aldeano":
            return f"El aldeano {self.nombre} duerme profundamente."
        return "Rol desconocido."
