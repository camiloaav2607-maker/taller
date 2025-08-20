peso=float(input("ingrese su peso: "))
altura=float(input("ingrese su altura: "))
imc=peso/(altura**2)#imc es el indice de masa corporal

if imc<18.5:
    print(f"usted tiene bajo peso y su imc es: {imc:.2f}")
elif imc>=18.5 and imc<24.9:
    print(f"usted tiene un peso normal y su imc es: {imc:.2f}")
elif imc>=25 and imc<29.9:
    print(f"usted tiene sobrepeso y su imc es: {imc:.2f}") 
else:
    print(f"usted tieneobesidad y su imc es:{imc:.2f}")       

