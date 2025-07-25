#actividad del dia viernes 25 de julio
#crear un numero
products=[]

while True:
    print("1.Agregar un producto a la lista")
    print("2.Modificar un producto existente")
    print("3.Eliminar un producto existente")
    print("4.Ver todos los productos")
    print("4. salir del programa")

    opcions= input("Eliga una opción 1-5: ")

    match opciones:
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




