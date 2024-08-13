while True:
    num = int(input("Escriba el numero de la tabla a multiplicar"))
    c= 1
    while c <=10:
        print((f"{c} X {num} = {num*c}"))
        c +=1 
    op=(int(input("Selecciona una opcion: \n"+
                    "1- Pedir otro numero\n"+
                    "2- Salir\n")))
    if (op == 1):
        continue
    elif(op == 2):
        break
    else:
        print("Op X")
       
    
