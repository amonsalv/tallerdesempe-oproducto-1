

frutas=[]

fruta={}

for i in range(2):
    nombre=input("Digite el nombre de la fruta: ")
    color=input("Digite el color de la fruta: ")
    precio=int(input("Digite el precio de la fruta: "))

    fruta['nombre']=nombre
    fruta['color']=color
    fruta['precio']=precio
    print("---------------------------------------------")
    frutas.append(fruta)

reverse= list(reversed(frutas))
print(reverse)

    


