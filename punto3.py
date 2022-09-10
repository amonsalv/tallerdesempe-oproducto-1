

productos=[]

opcion= 100

while opcion != 0:
    print("--------------------BIENVENIDO A TU TIENDA EL CHIGUIRO FELIZ--------------------")
    print("DIGITE UNA OPCION VALIDA")
    print("1.INGRESE UN NUEVO PRODUCTO")
    print("2.MOSTRAR TODOS LOS PRODUCTOS")
    print("3.BUSCAR/EDITAR PRODUCTO")
    print("4.BUSCAR/ELIMINAR PRODUCTO")
    print("0.SALIR")

    opcion= int(input("Seleccione una opcion: "))
    producto={}

    if(opcion == 1):
        codigo=input("Digite el codigo: ")
        nombre=input("Digite el nombre: ")
        precio=int(input("DIgite el precio"))
        producto['codigo']=codigo
        producto['nombre']=nombre
        producto['precio']=precio

        productos.append(producto)

    elif(opcion == 2):
        if(len(productos) == 0):
            print("No hay productos digitados")
        else:
            print(productos)
    elif(opcion == 3):
        buscar=input("Digite el Codigo: ")
        for i in productos:
            if i["codigo"] == buscar:
                nuevoPrecio=int(input("Digite el nuevo Precio: "))
                i["precio"] = nuevoPrecio
                print("Modificado correctamente")

    elif(opcion == 4):
        eliminar=input("Digite el Codigo: ")
        for i in productos:
            if i["codigo"] == eliminar:
                i.pop(eliminar)
                print("Borrado correctamente")
    elif(opcion == 0):
        print("GRACIAS POR PREFERIRNOS")
        
else:
    print("DIGITE UNA OPCION VALIDA")