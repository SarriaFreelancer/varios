import subprocess

def menu():
    opcion = True
    while opcion:
        opc = int(input("""
                    ========================================================
                    ********Menu de Conversion de Sistemas Numéricos******** 
                    ========================================================
                    Elige la opcion que deseas para convertir\n
                    1. Convertir de binario-decimal.
                    2. Convertir de decimal-binario.
                    3. Convertir de decimal-octal.
                    4. Convertir de octal-decimal.
                    5. Convertir de decimal-hexadecimal.
                    6. Convertir de-hexadecimal-decimal.
                    7. Convertir de octal-hexadecimal.
                    8. Convertir de hexadecimal-octal.
                    9. Convertir de hexadecimal-binario.
                    10. Convertir de octal-binario.
                    11. salir
                    Digite la opcion desea: """
                    
                    ))
        if opc == 1:
            bin = input("Ingresa un número binario: ")
            decimal = binario_a_decimal(bin)
            print(f"El número {bin} es {decimal} en decimal")
         
        elif opc== 2:
            dec = int(input("Ingresa un número decimal: "))
            binario = decimal_a_binario(dec)
            print(f"El número {dec} es {binario} en binario")
           
        elif opc==3:
            decimal = int(input("Ingresa un número decimal: "))
            octal = decimal_a_octal(decimal)
            print(f"El decimal {decimal} es {octal} en octal")
    
        elif opc==4:
            octal = input("Ingresa un número octal: ")
            decimal = octal_a_decimal(octal)
            print(f"El octal {octal} es {decimal} en decimal")
            
        elif opc== 5:
            decimal = int(input("Ingresa un número decimal: "))
            hexadecimal = decimal_a_hexadecimal(decimal)
            print(f"El decimal {decimal} es {hexadecimal} en hexadecimal")
            
        elif opc== 6:
            hexadecimal = input("Ingresa un número hexadecimal: ")
            decimal = hexadecimal_a_decimal(hexadecimal)
            print(f"El hexadecimal {hexadecimal} equivale a {decimal} en decimal")
                
        elif opc== 7:
            octal = input("Ingresa un número octal: ")
            decimal = octal_a_decimal(octal)
            print(f"El octal {octal} es {decimal} en decimal")
            
        elif opc== 8:
            print(hexadecimal_a_octal())
            
        elif opc==9:
            print(hexadecimal_a_binario())

        elif opc ==10:
            octal = input("ingrese un numero octal: ")
            binario = octal_a_binario(octal)
            print(f"El octal {octal} es {binario} en binario")
        elif opc == 11:
            opcion = False
            print(f"""
                                ============================================
                                ========saliendo del programa...============\n""")
            
        else:
            print("\nEl valor digitado no esta entre las opciones, digite un nuevo valor")
            
#Creacion de funciones

#1_ binario a decimal

def binario_a_decimal(numero_binario):
	numero_decimal = 0 

	for posicion, digito_string in enumerate(numero_binario[::-1]):
		numero_decimal += int(digito_string) * 2 ** posicion

	return numero_decimal

#2_ decimal a binario

def decimal_a_binario(dec):
    if dec <= 0:
        return "0"
   
    binario = ""
    
    while dec > 0:
        trash = int(dec % 2)
        dec = int(dec / 2)
        binario = str(trash) + binario
    return binario


#3_ decimal a octal

def decimal_a_octal(decimal):
    octal = ""
    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal / 8)
    return octal

#4_ octal a decimal

def octal_a_decimal(octal):
    print(f"Convirtiendo el octal {octal}...")
    decimal = 0
    posicion = 0
    # Invertir octal, porque debemos recorrerlo de derecha a izquierda
    # pero for in comienza de izquierda a derecha
    octal = octal[::-1]
    for digito in octal:
        print(f"El número decimal es {decimal}")
        valor_entero = int(digito)
        numero_elevado = int(8 ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        print(
            f"Elevamos el 8 a la potencia {posicion} (el resultado es {numero_elevado}) y multiplicamos por el carácter actual: {valor_entero}")
        decimal += equivalencia
        print(f"Sumamos {equivalencia} a decimal.")
        print(f"El numero {octal} en decimal equivale a {decimal}")
        posicion += 1
    return decimal

#5_ decimal a hexadecimal

def obtener_caracter_hexadecimal(valor):
    # Lo necesitamos como cadena
    valor = str(valor)
    equivalencias = {
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor


def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal

#6_ hexadecimal a decimal obtener valor real

def obtener_valor_real(caracter_hexadecimal):
    equivalencias = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10,
    }
    if caracter_hexadecimal in equivalencias:
        return equivalencias[caracter_hexadecimal]
    else:
        return int(caracter_hexadecimal)

#6_ hexadecimal a decimal
def hexadecimal_a_decimal(hexadecimal):
    # Convertir a minúsculas para hacer las cosas más simples
    hexadecimal = hexadecimal.lower()
    # La debemos recorrer del final al principio, así que la invertimos
    hexadecimal = hexadecimal[::-1]
    decimal = 0
    posicion = 0
    for digito in hexadecimal:
        print(f"Decimal es {decimal}")
        # Necesitamos que nos dé un 10 para la A, un 9 para el 9, un 11 para la B, etcétera
        valor = obtener_valor_real(digito)
        print(f"El verdadero valor de {digito} es {valor}")
        elevado = 16 ** posicion
        print(
            f"Elevamos 16 a la potencia {posicion}, el resultado es {elevado}")
        equivalencia = elevado * valor
        print(
            f"Multiplicamos el número elevado por el valor del carácter actual: {equivalencia}")
        decimal += equivalencia
        print(f"\nAhora en decimal es {decimal}")
        posicion += 1
    return decimal


#7_ octal a hexadecimal
def octal_a_decimal(octal):
    print(f"Convirtiendo el octal {octal}...")
    decimal = 0
    posicion = 0
    # Invertir octal, porque debemos recorrerlo de derecha a izquierda
    # pero for in empieza de izquierda a derecha
    octal = octal[::-1]
    for digito in octal:
        print(f"El número decimal es {decimal}")
        valor_entero = int(digito)
        numero_elevado = int(8 ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        print(
            f"Elevamos el 8 a la potencia {posicion} (el resultado es {numero_elevado}) y multiplicamos por el carácter actual: {valor_entero}")
        decimal += equivalencia
        print(f"Sumamos {equivalencia} a decimal. Ahora es {decimal}")
        posicion += 1
    return decimal

#8_ hexadecimal a octal

def hexa_to_octal(x):
    return oct(int(x, 16))
#funcion sin parametros, lo pide dentro de ella
def hexadecimal_a_octal():
    hexa_to_octal('A')
    print("Ingrese el número hexadecimal: ")
    hexa_dec_no = input()
    check = 0
    dec_num = 0
    hexa_dec_no_len = len(hexa_dec_no)
    hexa_dec_no_len = hexa_dec_no_len-1
    i = 0
    while hexa_dec_no_len>=0:
        rem = hexa_dec_no[hexa_dec_no_len]
        if rem>='0' and rem<='9':
            rem = int(rem)
        elif rem>='A' and rem<='F':
            rem = ord(rem)
            rem = rem-55
        elif rem>='a' and rem<='f':
            rem = ord(rem)
            rem = rem-87
        else:
            check = 1
            break
        dec_num = dec_num + (rem * (16 ** i))
        hexa_dec_no_len = hexa_dec_no_len-1
        i = i+1
    if check==0:
        i = 0
        octnum = []
        while dec_num!=0:
            rem = dec_num%8
            octnum.insert(i, rem)
            i = i+1
            dec_num = int(dec_num/8)
            
            
        print("\nValor equivalente en octal es: ")
        i = i-1
        while i>=0:
            print(octnum[i], end="")
            i = i-1
        print()
    else:
        print("\nPlease Enter a Valid Input")

#9 hexadecimal a binario
import subprocess
def ns(c):
        while c!=("s") and c!=("n"):
            print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
        return(c)

def hexadecimal_a_binario():

    lista_hex=['0','1','2','3','4','5','6','7'
            ,'8','9','A','B','C','D','E','F']

    while True:
        print("****************TRADUCTOR HEXADECIMAL-BINARIO****************")
        print("")
        hexa=input("Introduce hexadecimal: ")

        binario=[]

        for i in hexa:
            if i in lista_hex:
                indice=lista_hex.index(i)
                num_binar=(bin(indice)).lstrip("0b")
                longi=(abs(len(num_binar)-4))
                n='0'*longi
                n_cadena=n+num_binar
                binario.append(n_cadena)
            else:
                print("El carater",i,"no es hexadecimal, por lo que ha sido ignorado.")
                print(f"O deebe escribir una de estas en mayusculas /'A','B','C','D','E','F'/")

        binario_final=str(("").join(binario))
        
        print("")
        print("TRADUCCIÓN BINARIA:",binario_final)
        print("")

        conti=ns(input("¿Desea continuar?: "))
        if conti=="n":
            break
        subprocess.call(["cmd.exe","/C","cls"])

#de octal a binario
def octal_a_binario(octal):
    print(f"Convirtiendo el octal {octal}...")
    binarioList = []
    posicion = 0
    # Invertir octal, porque debemos recorrerlo de derecha a izquierda
    # pero for in empieza de izquierda a derecha
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

#Llamado a funcion principal de Menu
print(menu())
       