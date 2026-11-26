# Proyecto Final POO - Grupo 2: Agencia de viajes
# Integrantes:
# 1. [Alvarado Garcia Jonathan]
# 2. [Gonzalez Cevallos Elkin]
# 3. [Gonzalez Cevallos Walter]
# 4. [Holguin Ureta Luis]
# 5. [Leon Chiluiza Mayra]

from paquete_turistico import PaqueteTuristico


class PaqueteNacional(PaqueteTuristico):
    """Subclase para paquetes turisticos nacionales."""

    def __init__(
        self,
        codigo: str,
        destino: str,
        precio_base: float,
        duracion_dias: int,
        region: str,
        incluye_transporte: bool = True,
    ):
        super().__init__(codigo, destino, precio_base, duracion_dias)
        self.__region = ""
        self.__incluye_transporte = True

        self.region = region
        self.incluye_transporte = incluye_transporte

    @property
    def region(self) -> str:
        return self.__region

    @region.setter
    def region(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La region no puede estar vacia.")
        self.__region = valor.strip()

    @property
    def incluye_transporte(self) -> bool:
        return self.__incluye_transporte

    @incluye_transporte.setter
    def incluye_transporte(self, valor: bool) -> None:
        if not isinstance(valor, bool):
            raise ValueError("incluye_transporte debe ser verdadero o falso.")
        self.__incluye_transporte = valor

    def calcular_precio_final(self) -> float:
        """Aplica un 10% de descuento si el viaje dura 5 dias o mas."""
        total = self.precio_base
        if self.duracion_dias >= 5:
            total *= 0.90
        if self.__incluye_transporte:
            total += 25.0
        return round(total, 2)

    def __str__(self) -> str:
        transporte_txt = "Con transporte" if self.__incluye_transporte else "Sin transporte"
        return (
            f"{super().__str__()} | Nacional ({self.__region}, {transporte_txt})"
        )


if __name__ == "__main__":
    nac = PaqueteNacional("nac-101", "Cuenca", 180.0, 5, "Sierra", True)
    print(nac)