#calculate average temperature from a list of temperatures

numberOfDays = int(input("Enter number of days Temperature: "))
total = 0 #esta variable sirve para almacenar la suma de las temperaturas
temp=[] #lista vacia para almacenar las temperaturas

for i in range (numberOfDays):
    nextDay = input("Enter temperature for day " + str(i) + ": ") #lee la temperatura del dia i
    temp.append(float(nextDay)) #agrega la temperatura a la lista
    total += temp[i] #suma la temperatura del dia i al total
average = total / numberOfDays
print("Average temperature over " + str(numberOfDays) + " days is: " + str(average))

aboveAverage = 0
for i in temp:
    if i > average:
        aboveAverage += 1

print(str(aboveAverage) + " days were above average temperature.")