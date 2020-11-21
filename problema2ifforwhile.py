import math 
n=int(input('introdu numarul'))
suma=0
for x in range (1,n+1):
    suma+=math.factorial (x)
print('suma este' , suma )

