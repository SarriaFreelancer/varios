

#7_ octal a hexadecimal
def octal_a_binario(octal):
    print(f"Convirtiendo el octal {octal}...")
    binarioList = []
    posicion = 0
    # Invertir octal, porque debemos recorrerlo de derecha a izquierda
    # pero for in empieza de izquierda a derecha
    #octal = octal[::-1]

    for i in octal:
        if i == '0':
            i = '000'
        elif i == '1':
            i = '001'
        elif i == '2':
            i = '010'
        elif i == '3':
            i = '011'
        elif i == '4':
            i = '100'
        elif i == '5':
            i = '101'
        elif i == '6':
            i = '110'
        elif i == '7':
            i = '111'
        else:
            print("El numero digitado no es un octal")
        binarioList.append(i)
        
    
    sentencia = ""
    for i in binarioList:
        sentencia += str(i) + ""
    return(sentencia)

octal = input("ingrese un numero octal: ")
binario = octal_a_binario(octal)
print(f"El octal {octal} es {binario} en binario")