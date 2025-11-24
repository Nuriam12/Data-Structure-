import array

from numpy import indices

my_Array = array.array('i', [1, 2, 3, 4, 5])
print(my_Array)

my_Array.insert(0, 8) #INSERTAMOS ELEMENTOS EN EL ARRAY 
print(my_Array)



from array import *

arr1 = array('i', [11, 22, 33, 44, 55])
arr2 = array('i', [6, 7, 8, 9, 10]) 

#arr1.insert (2, 9) #INSERTAMOS ELEMENTOS EN EL ARRAY
#print (arr1)

def traverseArray(array): #RECORRER EL ARRAY
    for i in array:
        print(i)

traverseArray(arr1)



#accediendo a elementos de un array 

from array import *

arr1 = array('i', [11, 12, 13, 14, 15])

def accessElement(array, *indices):
    for index in indices:
        if index >= len(array):
            print("Index out of bound")
        else:
            print (array[index])
accessElement(arr1, 1, 4, 2)        


#busqueda por elementos dentro de un array 

from array import *

arr1 = array('i', [21, 22, 23, 24, 25])

def linear_search (array, target):
    for i in range (len(array)):
        if array[i] == target:
            return i
    return -1

print (linear_search(arr1, 21))


#eliminar elementos de un array

from array import *

arr1 = array('i', [31, 32, 33, 34, 35])

def deleteElement(array, index):
    if index >= len(array):
        print("Index out of bound")
    else:
        array.pop(index)

deleteElement(arr1, 2)
print (arr1)
