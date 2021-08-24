#Dictionaries
#Marlon Aldair Arciniega sanchez


texto= input("introduce tu texto: ")
count={}


for palabra in texto.split(' '):
    if palabra in count:
        count[palabra]+=1
    else:
        count[palabra]=1

for key, value in count.items():
    print(key,value)