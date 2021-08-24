#Marlon Aldair Arciniega sanchez

txt = str(open('texto_04.txt', 'r'))


linea=0
for linea in txt:
    
    if ((linea%2)==0): #las lineas pares(las que no deseamos)
        continue
    if ((linea % 2)!=0): #lineas impares
        print(linea)

txt.close()
