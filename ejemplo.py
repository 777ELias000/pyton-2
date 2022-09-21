cant = 0
while cant < 2:
    print("hola mundo")
    cant += 1

#  while sirve para ejecutar un bloque de codigo


num1 = int(input())
num2 = int(input())
while True:
    print("""opciones:
    1) Suma
    2) Resta
    3) Division
    4) salir""")
    opcion = int(input("ingresa la operacion a realizar"))
    if opcion == 1:
        print("la suma es:", num1 + num2)
        print("¿Desea realizar otra operacion? s/n")
        rpta = input()
        if rpta == "s":
            continue
        else:
            break

    elif opcion == 2:
        print("la resta es:", num1 - num2)
        print("¿Desea realizar otra operacion? s/n")
        rpta = input()
        if rpta == "s":
            continue
        else:
            break

    elif opcion == 3:
        print("la division es: ", num1 / num2)
        print("¿Desea realizar otra operacion? s/n")
        rpta = input()
        if rpta == "s":
            continue
        else:
            break
    else:
        break

    
