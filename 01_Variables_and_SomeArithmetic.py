#Variables and Some Arithmetic
#Marlon Aldair Arciniega sanchez

#Given: Two positive integers a and b, each less than 1000.
#Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.

a= int(input("introduzca el valor del cateto a: " ))
b= int(input("introduzca el valor del cateto  b: "))

c= (a**2) + (b**2)
print("el valor del cuadrado de la hipotenusa es: ", c) 