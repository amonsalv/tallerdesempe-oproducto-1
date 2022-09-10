cantidadnumeros = int(input("Digite la cantidad de numeros que desea ingresar:"))
numeros = []
multiplos2 =[]
multiplos3 = []

for i in range (cantidadnumeros):
    numero = int(input("Digite un numero entero: "))
    numeros.append(numero)
    if(numero%2 == 0):
        multiplos2.append(numero)
    elif(numero%2==0 and numero%3 == 0):
        multiplos2.append(numero)
        multiplos3.append(numero)
    elif(numero%3 == 0):
        multiplos3.append(numero)

print(f'la lista {numeros} contiene {len(multiplos2)} multiplos de 2 y {len(multiplos3)} de multiplos de 3')



