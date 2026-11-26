# Proyecto Final POO - Grupo 2: Agencia de viajes
# Integrantes:
# 1. [Alvarado Garcia Jonathan]
# 2. [Gonzalez Cevallos Elkin]
# 3. [Gonzalez Cevallos Walter]
# 4. [Holguin Ureta Luis]
# 5. [Leon Chiluiza Mayra]

from paquete_aventura import PaqueteAventura
from paquete_internacional import PaqueteInternacional
from paquete_nacional import PaqueteNacional


def main() -> None:
    paquetes = [
        PaqueteNacional("nac-101", "Cuenca", 180.0, 5, "Sierra", True),
        PaqueteInternacional("int-201", "Madrid", 900.0, 7, "Espana", 80.0),
        PaqueteAventura("ave-301", "Banos", 150.0, 2, "Alto", 40.0),
    ]

    print("=== CATALOGO Y CALCULO POLIMORFICO DE PRECIOS ===")
    for paquete in paquetes:
        print(paquete)
        print(f"   -> Precio final calculado: ${paquete.calcular_precio_final():.2f}")


if __name__ == "__main__":
    main()