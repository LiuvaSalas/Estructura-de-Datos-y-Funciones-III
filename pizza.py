def mostrar_menu():

    """
    Muestra las opciones para escoger los ingredientes de la pizza.
    """

    print("Bienvenido a Pizza JAT")
    print("1. Elegir tipo de masa")
    print("2. Elegir tipo de salsa")
    print("3. Agregar ingredientes")
    print("4. Eliminar ingredientes")
    print("5. Mostrar ingredientes actuales")
    print("6. Confirmar pedido")
    print("7. Salir")

def elegir_masa():

    """
    Se elige el tipo de masa para la pizza.

    Parámetros:
    - masas (list): Listado de las masas disponibles.
    - eleccion (str): Variable que almacena la masa seleccionada.

    Return: masa seleccionada
    """

    masas = ["Masa Tradicional", "Masa Delgada", "Masa con Bordes de Queso"]
    print("Tipos de masa disponibles:")
    for i, masa in enumerate(masas, 1):
        print(f"{i}. {masa}")
    eleccion = int(input("Elige el tipo de masa: "))
    return masas[eleccion - 1]

def elegir_salsa():

    """
    Se elige el tipo de salsa para la pizza.

    Parámetros:
    - salsas (list): Listado de las salsas disponibles.
    - eleccion (str): Variable que almacena la salsa seleccionada.

    Return: salsa seleccionada
    """

    salsas = ["Salsa de Tomate", "Salsa Alfredo", "Salsa Barbecue", "Salsa Pesto"]
    print("Tipos de salsa disponibles:")
    for i, salsa in enumerate(salsas, 1):
        print(f"{i}. {salsa}")
    eleccion = int(input("Elige el tipo de salsa: "))
    return salsas[eleccion - 1]

def agregar_ingredientes(ingredientes_actuales):
    """
    Se agregan los ingredientes solidos para la pizza.

    Parámetros:
    - Ingredientes_disponibles (list): Listado de los ingredientes disponibles.
    - eleccion (str): Variable que almacena el ingrediente seleccionado por el usuario.

    Return: ingredientes_actuales, que almacena los ingredientes seleccionados.
    """

    ingredientes_disponibles = ["Tomate", "Champiñones", "Aceituna", "Cebolla", "Pollo", "Jamón", "Carne", "Tocino", "Queso"]
    print("Ingredientes disponibles:")
    for i, ingrediente in enumerate(ingredientes_disponibles, 1):
        print(f"{i}. {ingrediente}")
    eleccion = int(input("Elige el ingrediente a agregar: "))
    ingrediente_seleccionado = ingredientes_disponibles[eleccion - 1]
    if ingrediente_seleccionado not in ingredientes_actuales:
        ingredientes_actuales.append(ingrediente_seleccionado)
    return ingredientes_actuales

def eliminar_ingredientes(ingredientes_actuales):
    
    """
    Se agregan los ingredientes solidos agregados en la pizza anteriormente, pero que ya no se quieren.

    Parámetros:
    - Ingrediente_seleccionado (list): almacena los ingredientes selecionados para eliminar de los ingredientes agregados en la pizza.
    - eleccion (str): Variable que almacena el ingrediente seleccionado por el usuario para eliminar.
    - ingredientes_actuales (list): Listado que almacena los ingredientes actualizados luego de eliminar el seleccionado anteriormente.

    Return: ingredientes_actuales, que almacena los ingredientes actualizados despues de eliminar los que no se quieren.
    """

    print("Ingredientes actuales:")
    for i, ingrediente in enumerate(ingredientes_actuales, 1):
        print(f"{i}. {ingrediente}")
    eleccion = int(input("Elige el ingrediente a eliminar: "))
    ingrediente_seleccionado = ingredientes_actuales[eleccion - 1]
    ingredientes_actuales.remove(ingrediente_seleccionado)
    return ingredientes_actuales

def mostrar_ingredientes(ingredientes_actuales):
    """
    Se muestran los ingredientes solidos agregados en la pizza anteriormente.

    Return: Listado de ingredientes seleccionados.
    """
    print("Ingredientes actuales en la pizza:")
    for ingrediente in ingredientes_actuales:
        print(f"- {ingrediente}")

def confirmar_pedido(masa, salsa, ingredientes):
    """
    Se muestran los detalles finales del pedido, la masa seleccionada, la salsa seleccionada, y los ingredientes seleccionados, ademas del tiempo de espera.

    Parámetros:
    - tiempo_estimado (int): Variable que almacena la operacion del tiempo que demorara el pedido.
    - confirmacion (str): variable que almacena la decision de confirmar el pedido como esta.

    Return: Estado del pedido.
    """
    tiempo_estimado = 20 + 2 * len(ingredientes)
    print(f"Tu pizza con {masa}, {salsa} y los siguientes ingredientes: {', '.join(ingredientes)} estará lista en {tiempo_estimado} minutos.")
    confirmacion = input("¿Deseas confirmar el pedido? (si/no): ")
    if confirmacion.lower() == "si":
        print("Pedido confirmado. ¡Gracias por tu compra!")
    else:
        print("Pedido cancelado.")

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