n=int(input('introdu anul '))
n=n-2000
if (n%12==1):
    print('zodia sarpe')
elif (n%12==2):
    print('zodia cal')
elif (n%12==3) :
    print('zodia oaie')   
elif (n%12==4):
    print ('zodia maimuta')
elif (n%12==5):
    print('zodia cocos')  
elif (n%12==6) :
    print('zodia caine')     
elif (n%12==7)  :
    print('zodia porc')  
elif (n%12==8) :
    print ('zodia sobolan')  
elif (n%12==9):
    print ('zoodia bou')   
elif (n%12==10) :
    print('zodia tigru') 
elif (n%12==11) :
    print('zodia iepure')   
elif (n%12==0)  :
    print ('zodia dragon')  

else:
    print ('nu exista asa zodie')    
