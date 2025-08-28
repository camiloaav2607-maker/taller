import os
os.system("clear")
print("numero mayor")

primernumero=int(input("ingresa el primer numero: "))
segundonumero=int(input("ingresa el segundo numero: "))
tercernumero=int(input("ingresa el tercer numero: "))

if primernumero>segundonumero and tercernumero:
    print("el numero mayor es:",primernumero)

elif segundonumero>primernumero and tercernumero:
    print("el numero mayor es:",segundonumero)

elif tercernumero>primernumero and segundonumero:
    print("el numero mayo es: ",tercernumero)

else:
    print("opcion no valida")    