# Proyecto Final POO - Grupo 2: Agencia de viajes
# Integrantes:
# 1. [Alvarado Garcia Jonathan]
# 2. [Gonzalez Cevallos Elkin]
# 3. [Gonzalez Cevallos Walter]
# 4. [Holguin Ureta Luis]
# 5. [Leon Chiluiza Mayra]

from paquete_turistico import PaqueteTuristico


class PaqueteAventura(PaqueteTuristico):
    """Subclase para paquetes turisticos de aventura."""

    def __init__(
        self,
        codigo: str,
        destino: str,
        precio_base: float,
        duracion_dias: int,
        nivel_riesgo: str,
        costo_equipo: float,
    ):
        super().__init__(codigo, destino, precio_base, duracion_dias)
        self.__nivel_riesgo = ""
        self.__costo_equipo = 0.0

        self.nivel_riesgo = nivel_riesgo
        self.costo_equipo = costo_equipo

    @property
    def nivel_riesgo(self) -> str:
        return self.__nivel_riesgo

    @nivel_riesgo.setter
    def nivel_riesgo(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nivel de riesgo no puede estar vacio.")
        self.__nivel_riesgo = valor.strip().capitalize()

    @property
    def costo_equipo(self) -> float:
        return self.__costo_equipo

    @costo_equipo.setter
    def costo_equipo(self, valor: float) -> None:
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("El costo del equipo no puede ser negativo.")
        self.__costo_equipo = float(valor)

    def calcular_precio_final(self) -> float:
        """Suma el costo de equipo especializado y un recargo por dia de aventura."""
        recargo_por_dia = 15.0 * self.duracion_dias
        total = self.precio_base + self.__costo_equipo + recargo_por_dia
        return round(total, 2)

    def __str__(self) -> str:
        return (
            f"{super().__str__()} | Aventura (Riesgo: {self.__nivel_riesgo}, "
            f"Equipo: ${self.__costo_equipo:.2f})"
        )


if __name__ == "__main__":
    ave = PaqueteAventura("ave-301", "Banos", 150.0, 2, "Alto", 40.0)
    print(ave)