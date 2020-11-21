n=int(input('introdu numarul de zile a lunii'))
if (n>=28) and (n<=31):
    if n==28:
        print('februaire in an simplu')
    if n==29:
        print ('februarie in an bisect')   
    if n==30:
        print ('aprilie,iunie,septembrie,noiembrie')     
    if n==31:
        print ('ianuarie,martie,mai,iulie,august,octombrie,decembrie')    
else:
    print('asa luna nu exista')        