#actividad del dia viernes 25 de julio
#crear un numero
products=[]

while True:
    print("1.Agregar un producto a la lista")
    print("2.Modificar un producto existente")
    print("3.Eliminar un producto existente")
    print("4.Ver todos los productos")
    print("5. salir del programa")

    opcions= input("Eliga una opción 1-5: ")

    match opcions:
        case "1":
            nuevo= input("Digite el nueveo elemento: ")
            products.append(nuevo)
            print("Nuevo elemento guardado")

        case "2":
            print(f"lista actual:{products} ")
            indice =int(input("Ingrese la posicion del elemntos que desea modificar: "))
            new_value= input("Ingrese nuevo valor para modificar: ")
            products[indice]=new_value
            print("Elemento modificado con exito")

        case "3":
            print(f"Mostrando lista actual: {products}")
            value= input("ingrese el elemento a eliminar del listado: ")
            products.remove(value)
            print("Elemento eliminado con exito")

        case "4":
            print(f"mostrando todo el listado: {products}")

        case "5":
            print("_____Saliendo del menú______")
            break

        case _:
            print("opcion no valida :) ")





