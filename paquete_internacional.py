# Proyecto Final POO - Grupo 2: Agencia de viajes
# Integrantes:
# 1. [Alvarado Garcia Jonathan]
# 2. [Gonzalez Cevallos Elkin]
# 3. [Gonzalez Cevallos Walter]
# 4. [Holguin Ureta Luis]
# 5. [Leon Chiluiza Mayra]

from paquete_turistico import PaqueteTuristico


class PaqueteInternacional(PaqueteTuristico):
    """Subclase para paquetes turisticos internacionales."""

    def __init__(
        self,
        codigo: str,
        destino: str,
        precio_base: float,
        duracion_dias: int,
        pais: str,
        seguro_viaje: float,
    ):
        super().__init__(codigo, destino, precio_base, duracion_dias)
        self.__pais = ""
        self.__seguro_viaje = 0.0

        self.pais = pais
        self.seguro_viaje = seguro_viaje

    @property
    def pais(self) -> str:
        return self.__pais

    @pais.setter
    def pais(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El pais no puede estar vacio.")
        self.__pais = valor.strip()

    @property
    def seguro_viaje(self) -> float:
        return self.__seguro_viaje

    @seguro_viaje.setter
    def seguro_viaje(self, valor: float) -> None:
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("El seguro de viaje no puede ser negativo.")
        self.__seguro_viaje = float(valor)

    def calcular_precio_final(self) -> float:
        """Suma tasa aeroportuaria fija ($45) y el seguro de viaje."""
        tasa_aeroportuaria = 45.0
        total = self.precio_base + tasa_aeroportuaria + self.__seguro_viaje
        return round(total, 2)

    def __str__(self) -> str:
        return (
            f"{super().__str__()} | Internacional ({self.__pais}, "
            f"Seguro: ${self.__seguro_viaje:.2f})"
        )


if __name__ == "__main__":
    inter = PaqueteInternacional("int-201", "Madrid", 900.0, 7, "Espana", 80.0)
    print(inter)