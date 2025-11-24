#day 1 - 11, 15, 10, 6
#day 2 - 9, 8, 7, 4
#day 3 - 5, 3, 2, 1
#day 4 - 15, 14, 13, 12

import numpy as np
print("TWO DIMENSIONAL ARRAY OPERATIONS")

twoDArray = np.array([[11,15,10,6],[9,8,7,4],[5,3,2,1],[15,14,13,12]])
print(twoDArray)

newTwoDArray = np.insert(twoDArray,3, [[8,8,8,8]], axis=0) #insertamos una nueva fila en la posicion 3 , el 0 indica que es una fila
print(newTwoDArray)

newTwoDArray2 = np.insert(twoDArray,2, [20,20,20,20], axis=1) #insertamos una nueva columna en la posicion 2 , el 1 indica que es una columna
print(newTwoDArray2)

#axis define si se trabaja con filas o columnas, axis=0 filas, axis=1 columnas
#mientras que la posicion define en que fila o columna se va a insertar el nuevo valor

newAppendTwoDArray = np.append(twoDArray, [[9,9,9,9]], axis=0) #con append se agrega al final, en este caso una nueva fila 
print(newAppendTwoDArray)


#ACCESSING AN ELEMENT OF TWO DIMENSIONAL ARRAY
print("ACCESSING AN ELEMENT OF TWO DIMENSIONAL ARRAY")
twoDArrayAccess = np.array([[11,15,10,6],[9,8,7,4],[5,3,2,1],[15,14,13,12]])
print(twoDArrayAccess)

def accessElement2D(array, row, col):
    if row >= len(array) or col >= len(array[0]):
        print("Index out of bound")
    else:
        print(array[row][col])

accessElement2D(twoDArrayAccess, 2, 3) #este proceso tiene una complejidad temporal de O(1) y una complejidad espacial de O(1) 

#TRAVERSAL - TWO DIMENSIONAL ARRAY
print("TRAVERSAL - TWO DIMENSIONAL ARRAY")

twoDArrayTraversal = np.array([[11,15,10,6],[9,8,7,4],[5,3,2,1],[15,14,13,12]])
print(twoDArrayTraversal)

def traverse2DArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])): #este proceso tiene una complejidad temporal de O(n*m) y una complejidad espacial de O(1)
            print(array[i][j])
        print()

traverse2DArray(twoDArrayTraversal)

#SEARCHING AN ELEMENT IN TWO DIMENSIONAL ARRAY
print("SEARCHING AN ELEMENT IN TWO DIMENSIONAL ARRAY")

twoDArraySearch = np.array([[11,15,10,6],[9,8,7,4],[5,3,2,1],[15,14,13,12]])
print(twoDArraySearch)

def searchDArray(array, value):
    for i in range (len(array)):
        for j in range (len(array[0])):
            if array[i][j] == value: #este proceso tiene una complejidad temporal de O(n*m) y una complejidad espacial de O(1)
                return (i, j)
print(searchDArray(twoDArraySearch, 7)) 

#DELETE AN ELEMENT IN TWO DIMENSIONAL ARRAY
print("DELETE AN ELEMENT IN TWO DIMENSIONAL ARRAY")

twoDArrayDelete = np.array([[11,15,10,6],[9,8,7,4],[5,3,2,1],[15,14,13,12]])
print(twoDArrayDelete)

newTwoDArrayDelete = np.delete(twoDArrayDelete, 1, axis=0) #eliminamos la fila en la posicion 1
print(newTwoDArrayDelete)


