# Examples of different types of lists in Python
print ("INTEGERS LIST")
integers = [1, 2, 3, 4, 5] 
print(integers)

print ("FLOATS LIST")
strings = ["apple", "banana", "cherry"]
print(strings)

print ("STRINGS LIST")
mixed = [1, "apple", 3.14, True]
print(mixed)

print("NESTED LIST")
nested = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print(nested)

#OPERTIONS ON LISTS
print("--------------------------OPERATIONS ON LISTS--------------------------")
ShoppingList = ["eggs", "milk", "bread"]
for i in ShoppingList:   #Recorriendo la lista
    print(i)
#print("Original Shopping List:", ShoppingList)        #Mostrando la lista original
#print(ShoppingList[-2])          #Accediendo al segundo elemento desde el final
print ('milk' in ShoppingList) #Comprobando si un elemento existe en la lista

#Update / inserting elements in a list
print("-----------Update / inserting elements in a list--------------------------")
myList = [10, 20, 30, 40, 50]
print("Original List:", myList)
#myList[3] = 100 #indicamos la posicion y el nuevo valor , la complejida temporal es O(1)
#myList.insert(0,14 ) #insertamos en la posicion 0 el valor 14, la complejida temporal es O(n)
#myList.append(60) #agregamos al final el valor 60 la complejida temporal es O(1) "este es el mas eficiente" 
newList = [70, 80, 90] 
myList.extend(newList) #extendemos myList con newList con este metodo , la complejidad temporal es de O(k) donde k es el tamaño de newList 
print("Updated List:", myList)

#slice / delete elements in a list
print("-----------slice / delete elements in a list--------------------------")
myList2 = [100, 200, 300, 400, 500]
print("Original List:", myList2)
#print(myList2.pop(2)) #eliminamos el elemento en la posicion 2 y lo retornamos , la complejidad temporal es O(n) 
#del myList2[1] #eliminamos el elemento en la posicion 1 , la complejidad temporal es O(n)
myList2.remove(400) #eliminamos el elemento con valor 400 , la complejidad temporal es O(n)
print(myList2)

#searching for an elements in a list
print("-----------searching for an elements in a list--------------------------")
myList3 = [5, 10, 15, 20, 25, 30]
#operator 
target = 20
# if target in myList3:   #la complejidad temporal es O(n), por que buscara el elemento en cada posicion hasta encontrarlo
#     print(f"{target} found in the list")
# else:
#     print(f"{target} not found in the list")

#linear search
def linear_search(p_lst, target):
    for i , value in enumerate(p_lst):
        if value == target:   #la complejidad temporal es O(n), por que buscara el elemento en cada posicion hasta encontrarlo
            return i
    return ("not found")
print(linear_search(myList3, 25))

#list operations/functions
print("-----------list operations/functions--------------------------")

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b  #concatenacion de listas, la complejidad temporal es 0(n+m) y la complejidad espacial es O(n+m)
print("Concatenated List:", c)

d = [1]
d = d * 3  #repeticion de listas, la complejidad temporal es O(k*n) y la complejidad espacial es O(k*n)
print("Repeated List:", d)

e = [3, 1, 4, 2, 5]
print(len(e))  #indica cuanto elementos tiene la lista, la complejidad temporal es O(1)
print(max(e))  #indica el valor maximo de la lista, la complejidad temporal es O(n)
print(min(e))  #indica el valor minimo de la lista, la complejidad temporal es O(n)
print(sum(e)/len(e)) #calcula el promedio de los elementos de la lista, la complejidad temporal es O(n)

#function 
# print("-----------average of a list--------------------------")
# mylist = list( ) #creamos la lista vacia 
# while True:
#     #inp = input ("ingresa tu numero")
#     if inp == "done": #definis la palabra para romper el ciclo
#         break
#     value = float (inp) #definimos el valor float
#     mylist.append(value)
# avg = sum (mylist) / len (mylist)
# #print("average:", avg)

#strings and lists
print("-----------strings and lists--------------------------")
a = 'spam spam spam'  #cadena de texto
b = list(a)  #convertimos la cadena en una lista de caracteres, la complejidad temporal es O(n) y la complejidad espacial es O(n)
print(b)

c = a.split()  #dividimos la cadena en una lista usando 'a' como separador, la complejidad temporal es O(n) y la complejidad espacial es O(n)
print(c)

#ARRAYS VS LISTS
print("-----------ARRAYS VS LISTS--------------------------")
import numpy as np

myArray =np.array([1, 2, 3, 4, 5,'a'])  #lista de enteros
myList = [1, 2, 3, 4, 5,'a']   #lista de enteros
print("Array:", myArray)
print("List:", myList)

#List comprehension 

#FORMULA PARA GENERAR UNA LIST COMPREHENSION
# new_list = [new item for item in firslist]]

print("-----------List comprehension --------------------------")
prev_list = [1, 2, 3, 4, 5]
new_list = [i*2 for i in prev_list] #creamos una nueva lista multiplicando por 2 cada elemento de la lista anterior
print("Previous List:", prev_list)
print("New List:", new_list)


languages = 'Python'
new_languages = [letter for letter in languages]
print("Languages List:", languages)
print("New Languages List:", new_languages)

#conditional list comprehension
print("-----------conditional list comprehension --------------------------")

first_list = [1, 2, 3, 4, -5, 6, -7, 8, 9, -10]
evenlist = [number for number in first_list if number >0 and number % 2 == 0] #condicionamos para que solo agreguen los numeros mayores a 0
print("First List:", first_list)
print("Even List:", evenlist)

newList = [number if number >0 else 0 for number in first_list] #condicionamos para que los numeros menores a 0 se conviertan en 0
print("First List:", newList)

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]
 
    for row in m:
        for element in row:
            if v < element: v = element
 
    return v
print(fun(data[0]))