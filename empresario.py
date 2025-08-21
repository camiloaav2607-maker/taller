import os
os.system("clear")

menulogin="""bienvenid al programa de venta de productos
      1. registrarse
      2. iniciar sesion
      3. salir
      4. menuhome"""
menuhome="""bienvenido al menu de inicio
1. comprar
2. inventario
3. vender
4. utilidades
5. salir"""

isActive=True



while isActive:
    os.system("clear")
    print(menulogin)
    opcion=int(input("seleccione una opcion: "))

match opcion:
    case 1:
        os.system("clear")
        print("registre su usuario")
        userR=input("ingrese su usuario: ")
        os.system("clear")   
        paswordR=input("ingrese su contraseña: ")
        os.system("clear") 
    case 2:
        os.system("clear")
        print("inicia sesion")
        userLogin=input("ingrese su nombre de usuario: ")
        paswordLogin=input("ingrese su contraseña: ") 
        if userR == userLoginn:
            os.system("clear")
            print("usuario correcto")
        else:
            print("usuario incorrecto") 
        paswordLogin=input("ingrese su contraseña") 
        if paswordR == paswordLogin:
            print("iniciaste sesion correctamente")
            os.system("pause")
            print(menuhome)

        else:
            print("contraseña incorrecta")    
    case 3:
        print("gracias por usar el programa")     

    case _:
        print("opcion no valida")     

 
   
