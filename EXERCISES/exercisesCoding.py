#Question 1 - missing number  

from array import array


list = array('i', [1, 2, 3, 4, 6, 7, 8, 9, 10]) #array con un numero faltante

def find_missing_number(arr):

    n = len(arr) + 1 #recorremos el array y sumamos 1 para obtener el numero total de elementos que deberia tener
    total = n*(n+1)//2 # aplicamos la formula de la suma de los primeros n numeros naturales
    sum_array = sum(arr) # sumamos los elementos del array
    return total - sum_array #restamos la suma del array a la suma total para obtener el numero faltante

print("Missing number is:", find_missing_number(list))

#Question 1.5 - 3 numbers missing

list2 = array('i', [1, 2, 3, 4, 5, 6, 7, 9, 10]) #array con tres numeros faltantes

def find_missing_numbers(list, n):
    sum1 = 10*(10+1)//2 #suma de los primeros 10 numeros naturales
    sum2 = sum(list) #suma de los elementos del array
    print (sum1 - sum2)

find_missing_numbers(list2, 10)

#conclucion : para encontrar numeros faltantes en un array podemos usar la formula de la suma de los primeros n numeros naturales
#y restar la suma de los elementos del array a la suma total esperada. la formula es : n*(n+1)//2

#Question 2 - Write a program to find all pairs of the integers whose sum is equal to a given number

print ("-------------------------Question 2----------------------------------")

def findpairs (list , target ) : 
    for i in range (len(list)): #recorremos el array y [i] es el indice y el indice se usa para acceder al elemento en esa posicion
        for j in range (len(list)): #recorremos el array nuevamente para comparar cada elemento con los demas
            if list[i] == list [j]:
                continue
            elif list[i] + list[j] == target:
                print ( i ,j)
list3 = [1,2,3,4,5,6,7,8,9]

findpairs (list3 , 8)

#conclusion : recorremos el array con dos ciclos for anidados para comparar cada elemento con los demas y verificar si la suma de dos elementos es igual al numero objetivo.
#si es asi, imprimimos los indices de los elementos que cumplen con la condicion.

#Question 3 - how to check if an array contains a number in python
print ("-------------------------Question 3----------------------------------")
import numpy as np

array4 = np.array([10, 20, 30, 40, 50])

def checknumber (array,target) : 
    for i in range (len(array)): #recorremos el array y [i] es el indice y el indice se usa para acceder al elemento en esa posicion
        if array[i] == target: #comparamos el elemento en la posicion i con el numero objetivo
            print (i)

checknumber (array4,30)

#conclusion : para encontrar un numero dentro de un array primero recorremos el array usando un ciclo for y comparamos cada elemento con el 
#numero objetivo, si encontramos una coincidencia imprimimos el indice del elemento encontrado.

#Question 4 - hallar el producto maximo de dos enteros en un array donde todos los enteros son positivos
print ("-------------------------Question 4----------------------------------")

def maxproduct(arr) : 
    tip11,tip112 = 0 , 0
    

    for num in arr : #aqui estamos recorriendo el array y num toma el valor de cada elemento en cada iteracion
        if num > tip11: #aqui num le esta diciendo a max1 que si el numero es mayor que max1 entonces max1 toma el valor de num
            tip112 = tip11
            tip11 = num 

        elif num > tip112 :
            tip112 = num
    return tip11 * tip112

arr = np.array ([ 1 , 7 , 3 , 4 , 9 , 5])
print (maxproduct(arr))


#Question 5 - Encontrar los dos números más grandes que no sean iguales.
# Ejemplo: en [4, 4, 3, 2] → el segundo mayor es 3.
print ("-------------------------Question 5----------------------------------")

def second_largest(arr):
    max1,max2 = 0 ,0 
    for num in arr : #aqui estamos recorriendo el array y num toma el valor de cada elemento en cada iteracion
        if num > max1 :  #aqui num le esta diciendo a max1 que si el numero es mayor que max1 entonces max1 toma el valor de num
            max1 = num 
        elif num > max2 and num != max1 : #aqui num le esta diciendo a max2 que si el numero es mayor que max2 y diferente a max1 entonces max2 toma el valor de num
            max2 = num 

    return int(max1), int(max2)

arr = np.array([4, 4, 3, 2])
print(second_largest(arr))

#Question 6 - Hallar la suma de los dos números más grandes pares del array.
# Si no hay dos números pares, devolver algo que tú definas.
print ("-------------------------Question 6----------------------------------")

def pairssum (arr) :
     pair1 = 0
     pair2 = 0
     for num in arr :
         if num % 2 == 0:
            if num > pair1:
                pair2 = pair1
                pair1 = num
            elif num > pair2 and num!= pair1 :
                pair2 = num
     return pair1 + pair2
arr = np.array([1,2,3,4,5,6,7,8])
print(pairssum(arr))        

#Question7 - escribe una funcion llamada middle que tome una lista y devuelva una nueva lista que contenga todos los elementos
# excepto el primero y el ultimo de la lista original.
print ("-------------------------Question 7----------------------------------")
def middle(lista):
    return lista [1:-1] # Devuelve una nueva lista que contiene todos los elementos excepto el primero y el último 1 y -1 son los indices que indican el primer y ultimo elemento de la lista
print(middle([1, 2, 3, 4, 5]))  

#Question 8 - dada una lista bidimensional, escribe una funcion llamada mylist2D que devuelva la suma de los elementos de la diagonal.
print ("-------------------------Question 8----------------------------------")

def mylist(arr) :
    suma = 0
    for i in range(len(arr)) : #recorremos el array usando un ciclo for y range para obtener los indices
        suma += arr[i][i]
    return suma
myList2D= [[1,2,3],[4,5,6],[7,8,9]] 

print(mylist(myList2D))

#Question 9 - dada una lista , escribe una funcion para obtener la primera y la segunda mejor puntuacion de la lista
print ("-------------------------Question 9----------------------------------")

def punctuation (arr):
    first_punctuation = 0
    second_puncuation = 0
    for num in arr :
        if num > first_punctuation :
            second_puncuation = first_punctuation
            first_punctuation = num 
        if num > second_puncuation and num != first_punctuation:
            second_puncuation = num 
    return int(first_punctuation) , int(second_puncuation)
miLista = [ 84 , 85 , 86 , 87 , 85 , 90 , 85 , 83 , 23 , 45 , 84 , 1 , 2 , 0 ]
print(punctuation(miLista))

#Question 10 - escribe una funcion para remover los numeros duplicados que estan dentro de un array 
print ("-------------------------Question 10----------------------------------")
def removeduplicate (list) :
    return  set(list)

print(removeduplicate([1, 1, 2, 2, 3, 4, 5]))


#Question 11 - escribe una funcion para encontrar todos los pares de un array de enteros quienes sumando con iguales al numero target , no consideres numeros conmutativos 
print ("-------------------------Question 11----------------------------------")
def sum_pairs (arr,target):
    resultado=[] #creamos una lista vacia para almacenar los pares que cumplen con la condicion
    for i in range(len(arr)):
        for j in range(i+1,len(arr)): #aqui j empieza desde i+1 para evitar numeros conmutativos , usamos i+1 para que j siempre sea mayor que i 
            if arr[i]+arr[j] == target: 
                resultado.append(f"{arr[i]}+{arr[j]}") #si la suma de los dos numeros es igual al target , agregamos el par a la lista resultado
    return resultado
arr=[ 2 , 4 , 3 , 5 , 6 , -2 , 4 , 7 , 8 , 9 ]
target = 7
print (sum_pairs(arr,target) )         

#Question 12 - Dado un array de enteros nums, devuelve verdadero si algún valor aparece al menos dos veces en el array, y devuelve falso si cada elemento es distinto.
print ("-------------------------Question 12----------------------------------")
def entradas_duplicadas (arr):
    for num in arr :
        if arr.count(num) > 1: #usamos el metodo count para contar cuantas veces aparece el numero en el array
            return True
    return False
arr = [1,2,3,4,5,1]
print(entradas_duplicadas(arr))
        

#Question 13 - Permutations 
print ("-------------------------Question 13----------------------------------")

def permutations (list1,list2):
    if len (list1) != len (list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False
    
list1 = [1,2,3,4]
list2 = [4,3,2,1]

print(permutations(list1,list2))

#Question 14 - you are given an n x x 2D matrix representing an image , rotate the image by 90 degrees (clockwise)
#you have to rotate the image in place , which means you have to modify the input 2D matrix directly . DO NOT allocate another 2D matrix and do the rotation.
print ("-------------------------Question 14----------------------------------")

#def rotate_matriz(matriz) :
    # for i in range (len(matriz)) :        #recorremos la matriz usando un ciclo for y range para obtener los indices , i recorre las filas
    #     for j in range (i , len(matriz)): #recorremos la matriz con un for y range y dentro del for usamos i para evitar intercambios dobles , j recorre las columnas
    #         matriz[i][j], matriz[j][i] = matriz[j][i] , matriz[i][j] # intercambiamos los elementos de la matriz
    # for i in matriz : #recorremos cada fila de la matriz
    #      i.reverse() #revertimos cada fila de la matriz para completar la rotacion
    # return matriz



matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])

y= np.rot90(matriz, -1) #usamos la funcion rot90 de numpy para rotar la matriz 90 grados en sentido horario , el -1 indica que es en sentido horario
print(y)
