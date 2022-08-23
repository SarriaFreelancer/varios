mi_matriz = [[0,5,4,2],
             [0,2,3,6],
             [0,9,8,5],
             [5,0,0,9]]
 
#Creamos la funcion que recibe una matriz
def entregarSuma(matriz):
    sumaS = int(0) #Variable para almacenar el total

    
    for i in range(len(matriz)): #Con el ciclo for recorremos cada elemento fila
        for j in range(len(matriz)):
            if (i<j):
                sumaS += matriz[i][j] #guardamos cada elemento de la matriz superior sumandolos
    #Retornamos la suma
    return f'La suma de la matriz superior es: {sumaS}'

#llamando a la funcion
print(entregarSuma(mi_matriz))