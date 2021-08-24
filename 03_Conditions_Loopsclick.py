####Conditions and Loopsclick to expand
#Marlon Aldair Arciniega sanchez

#Given: Two positive integers a and b (a<b<10000).
#Return: The sum of all odd integers from a through b, inclusively.

a=int(input("introduce a: "))
b=int(input("introduce b: "))

suma=0

for i in range (a, b+1):
    if i%2==1: #elige a los numeros impares
        suma+=i
    else:
        continue

print(suma)
