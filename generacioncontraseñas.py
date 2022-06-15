import random

listacaracteres=["a","b","c","d","e","f","g","h","i","j"]
l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","@","#","$","%","&","*","(",")","-","_","+","=","[","]","{","}",":",";",",",".","<",">","?","/"]

def generadorcontras(lista):
    c=0
    while c<10:
        random.shuffle(lista)
        for i in lista:
            print(i,end="")
        print("\n")
        c+=1

#generadorcontras(listacaracteres)

def generadorcontras2(largo,lista):
    aux=[]
    c=0
    while c<largo:
        aux.append(random.choice(lista))
        c+=1
        for i in aux:
            print(i,end="")
        c+=1

#generadorcontras2(10,l)

def generadorcontras3(largo,lista):
    c=0
    while c<10:
        generadorcontras2(largo,lista)
        print("\n")
        c+=1

generadorcontras3(8,l)
