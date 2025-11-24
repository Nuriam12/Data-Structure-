from array import *

#1.-create an array and traverse it
print("Step 1")
array1 = array('i', [10, 20, 30, 40, 50])
def traverseArray(arr):
    for i in arr:
        print(i)
traverseArray(array1)


#2.-access individual elements throught indexes
print("Step 2") 
array2 = array('i', [100, 200, 300, 400, 500])
def accessElement(arr,*indices):
    for index in indices :
        if index >= len(arr):
            print("Index out of bound")
        else:
            print(arr[index])
accessElement(array2, 0, 3, 4)


#3.-append any value to the array using append() method
print("Step 3")
array3 = array('i', [1, 2, 3, 4, 5])
#podemos usar tambien un for "x" in ["insertar elementos"] para agregar mas valores
array3.append(6)
print(array3)

#4.-insert value to the array using insert() method
print("Step 4")
array4 = array('i', [10, 20, 30, 40, 50])
for x in [60, 70, 80]: #lo usamos para agregar mas valores al index
    array4.insert(0,x)
    print(array4)

#5.-extend an array using extend() method
print("Step 5")
array5 = array('i', [1, 2, 3, 4, 5])
array4.extend(array5)
print(array4)

#6.-add items from list to array using fromlist() method
print("Step 6")
exampleList = [7, 8]
array3.fromlist(exampleList) #agrega los elementos de la lista al array
print(array3)

#7.-remove any array element using remove() method
print("Step 7")
array6 = array('i', [10, 20, 30, 40, 50])
array6.remove(10)
print(array6)

#8.-remove last array element using pop() method
print("Step 8")
array7 = array('i', [100, 200, 300, 400, 500])
array7.pop() #elimina el ultimo elemento del array
print(array7)

#9.-fetch any element through its index using index() method
print("Step 9")
array9 = array('i', [11, 22, 33, 44, 55])
print(array9.index(22)) #muestra el index del elemento 22

#10.-reverse a python array using reverse() method
print("Step 10")
array10 = array('i', [1, 2, 3, 4, 5])
array10.reverse() 
print(array10)

#11.-get array buffer information using buffer_info() method
print("Step 11")
array11 =array('L', [6, 7, 8, 9, 10])
print(array11.buffer_info()) #el metodo buffer nos muestra la direccion de memoria y el numero de elementos del array

#12.-check for number of occurrences of an element using count() method
print("Step 12")
array12 = array('i', [1, 2, 3, 2, 4, 2, 5])
array12.append(2)
print(array12.count(2)) #el metodo count nos muestra cuantas veces se repite el numero 2 en el array (concurrencia)

#14.-convert array to a python list using tolist() method
print("Step 14")
array14 = array('i', [10, 20, 30, 40, 50])
print(array14.tolist())

#16.-slice elements from an array
print("Step 16")
array16 = array('i', [11, 22, 33, 44, 55, 66, 77, 88, 99])
slicedArray = array16[1:3] #muestra los elementos desde el index 1 hasta el index 3 (sin incluir el 3)
print(slicedArray)