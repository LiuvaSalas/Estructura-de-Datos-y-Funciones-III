from pizza import (
    elegir_masa,
    elegir_salsa,
    agregar_ingredientes,
    eliminar_ingredientes,
    mostrar_ingredientes,
    confirmar_pedido,
)
from opciones import mostrar_menu


def main():
    masa = ""
    salsa = ""
    ingredientes = []
    while True:
        mostrar_menu()
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            masa = elegir_masa()
        elif opcion == 2:
            salsa = elegir_salsa()
        elif opcion == 3:
            ingredientes = agregar_ingredientes(ingredientes)
        elif opcion == 4:
            ingredientes = eliminar_ingredientes(ingredientes)
        elif opcion == 5:
            mostrar_ingredientes(ingredientes)
        elif opcion == 6:
            confirmar_pedido(masa, salsa, ingredientes)
        elif opcion == 7:
            print("Gracias por usar el sistema de pedidos de Pizza JAT. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")


if __name__ == "__main__":
    main()
