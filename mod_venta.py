lista_productos = []
def cantidad():
    while True:
        
        nombre_producto = input("ingrese el nombre del producto: ")
        lista_productos.append(nombre_producto)

        print(lista_productos)

        pregunta = int(input("quieres continuar marca 1/2 no: "))
        if pregunta ==1:
            continue
        else:
            print("fuera del sistema: ")
            break


cantidad()

