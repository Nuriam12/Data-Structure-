myDict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
myDict['age'] = 26  # Actualiza el valor asociado a la clave 'age'
myDict['city'] = 'Los Angeles'  # Actualiza el valor asociado a la clave 'city'
print(myDict)


#traversing a dictionary
print ("-------------------------traversing a dictionary----------------------------------")
myDict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

def traverseDict(dict):
    for key in dict:
        print(f"{key}: {dict[key]}") #lo hacemos asi para acceder a los valores del diccionario usando las claves
traverseDict(myDict)

#linear search in a dictionary
print ("-------------------------linear search in a dictionary----------------------------------")
myDict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

def linearSearchDict(dict, value):
    for key in dict: #recorremos las claves del diccionario , su complejidad temporal es de o(n)
        if dict[key] == value : #comparamos el valor asociado a la clave con el valor objetivo , su complejidad temporal es de o(1)
                return key , value #si encontramos una coincidencia devolvemos la clave y el valor, su complejidad temporal es de o(1)
    return 'el valor no existe'

print(linearSearchDict(myDict, 25))

#delete/remove elements from a dictionary
print ("-------------------------delete/remove elements from a dictionary----------------------------------")
myDict = {'name': 'Alice', 'age': 25, 'city': 'New York', 'profession': 'Engineer'}
#del myDict ['profession'] #eliminamos el par clave-valor asociado a la clave 'profession'
removed_element = myDict.pop('profession') #eliminamos el par clave-valor 
print(removed_element)
print(myDict)

#dictionary methods
print ("-------------------------dictionary methods----------------------------------")
myDict = {'name': 'Alice', 'age': 25, 'city': 'New York', 'profession': 'Engineer'}

#myDict.clear() #elimina todos los elementos del diccionario
#dict=myDict.copy() #devuelve una copia superficial del diccionario
#newdict = {}.fromkeys ([1,2,3],0) #esto crea un nuevo diccionario con las claves dadas y el valor None por defecto , el valor ira para todas las claves
#print(myDict.get('name')) #devuelve el valor asociado a la clase name , tambien podemos especificar el valor .
#print(myDict.items()) #devuelve una vista de objetos de pares clave-valor
#print(myDict.keys()) #esto nos devuelve las keys del diccionario
#print(myDict.popitem()) # este metdo elimina y devuelve un par clave-valor aleatorio del diccionario
#print(myDict.setdefault('city'))#devuelve el valor de la clave especificada , si la clave no existe , inserta la clave con el valor None , si no se encuentra en en el diccionario se agregara.
#print(myDict.values()) #devuelve una vista de los valores del diccionario
#------------------------------------
# newDict = {'country': 'USA', 'hobby': 'painting'}
# myDict.update(newDict) #agrega los pares clave-valor de newDict a myDict
# print(myDict) #actualiza el diccionario con los pares clave-valor de newDict
#------------------------------------


#DICTIONARY OPERATIONS
print ("-------------------------DICTIONARY OPERATIONS----------------------------------")
my_dict = {
     3: 'three',
     1: 'one',
     4: 'four',
     5: 'five',
     8: 'eight',
}
print(3 in my_dict) 
print(len(my_dict)) #esto devolvera el numero de pares clave-valor en el diccionario , el resultador sera 5
print(all(my_dict)) #esto devolvera True si todas las claves del diccionario son verdaderas o si el diccionario esta vacio
print(sorted(my_dict)) #esto devolvera una lista de las claves del diccionario ordenadas

#DICTIONARY COMPREHENSIONS
import random
print ("-------------------------DICTIONARY COMPREHENSIONS----------------------------------")

food_names = ['leche', 'pan', 'cafe', 'Huevos', 'mantequilla']

new_list = { food:random.randint(10,20)for food in food_names} #utilizamos la comprension de diccionarios para crear un nuevo diccionario donde las claves son los nombres de los alimentos y los valores son numeros aleatorios entre 1 y 2
print(new_list) 

numbers = [1, 2, 3, 4, 5]

new_numbers = {number * 2 for number in numbers} #utilizamos la comprension de diccionarios para crear un nuevo conjunto donde cada numero en la lista original se multiplica por 2 
print(new_numbers)  

new_food = { }
