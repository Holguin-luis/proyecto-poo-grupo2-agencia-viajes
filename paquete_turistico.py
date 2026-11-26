# Proyecto Final POO - Grupo 2: Agencia de viajes
# Integrantes:
# 1. [Alvarado Garcia Jonathan]
# 2. [Gonzalez Cevallos Elkin]
# 3. [Gonzalez Cevallos Walter]
# 4. [Holguin Ureta Luis]
# 5. [Leon Chiluiza Mayra]

class PaqueteTuristico:
    """Clase base que representa un paquete turistico generico."""

    def __init__(
        self, codigo: str, destino: str, precio_base: float, duracion_dias: int
    ):
        self.__codigo = ""
        self.__destino = ""
        self.__precio_base = 0.0
        self.__duracion_dias = 1

        self.codigo = codigo
        self.destino = destino
        self.precio_base = precio_base
        self.duracion_dias = duracion_dias

    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El codigo del paquete no puede estar vacio.")
        self.__codigo = valor.strip().upper()

    @property
    def destino(self) -> str:
        return self.__destino

    @destino.setter
    def destino(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El destino no puede estar vacio.")
        self.__destino = valor.strip()

    @property
    def precio_base(self) -> float:
        return self.__precio_base

    @precio_base.setter
    def precio_base(self, valor: float) -> None:
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El precio base debe ser un numero mayor que 0.")
        self.__precio_base = float(valor)

    @property
    def duracion_dias(self) -> int:
        return self.__duracion_dias

    @duracion_dias.setter
    def duracion_dias(self, valor: int) -> None:
        if not isinstance(valor, int) or isinstance(valor, bool) or valor <= 0:
            raise ValueError("La duracion en dias debe ser un entero mayor que 0.")
        self.__duracion_dias = valor

    def calcular_precio_final(self) -> float:
        """Calcula el precio final del paquete.

        Las subclases deben sobrescribir este metodo para aplicar sus propias
        reglas, impuestos o recargos.
        """
        return round(self.__precio_base, 2)

    def obtener_resumen(self) -> str:
        """Devuelve un resumen legible del paquete."""
        return (
            f"[{self.__codigo}] {self.__destino} ({self.__duracion_dias} dias) "
            f"- Precio base: ${self.__precio_base:.2f} | "
            f"Precio final: ${self.calcular_precio_final():.2f}"
        )

    def __str__(self) -> str:
        return self.obtener_resumen()


if __name__ == "__main__":
    paquete_prueba = PaqueteTuristico(
        codigo="pkg-001",
        destino="Salinas",
        precio_base=250.0,
        duracion_dias=3,
    )
    print(paquete_prueba)
    print("Acceso mediante @property -> Destino:", paquete_prueba.destino)