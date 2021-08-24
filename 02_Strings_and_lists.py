#Strings and Lists
#Marlon Aldair Arciniega sanchez

#Given: A string s of length at most 200 letters and four integers a, b, c and d.
#Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

#Sample Dataset
##HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
##22 27 97 102

#Sample Output
##Humpty Dumpty

txt=[]
txt= str(input("introduc tu cadena de texto: "))

a= int(input("introduce tu subindice a: "))
b= int(input("introduce tu subindice b: "))
c= int(input("introduce tu subindice c: "))
d= int(input("introduce tu subindice d: "))

texto_1= txt[a:b+1] + txt[c:d+1]
print(texto_1)


