while True:
    User=input("Ingrese su nombre")
    Pass=int(input("Ingrese una contraseña"))

    Verificacion = int(input("Verifique su contraseña"))

    if (Pass == Verificacion):
        print("Ha ingresado con exito")
        break
    else:
        print("Es incorrecta.Vuelva a digitar su contraseña")

#Yaya
while True:
    print("Ingrese credenciales")
    user=input("Ingrese usuario: ")
    pasw=input("Ingrese contraseña: ")

    usr = "UGB"
    psw = "ugb1234"

    if(user==usr):
        if(pasw==psw):
            print("Sesion iniciada")
            break
        else:
            print("La contrseña ingresada incorrectamente")
            continue
    else:
        print("Usuario no registrado")
        continue



   
