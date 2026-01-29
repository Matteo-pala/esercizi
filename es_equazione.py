#scrivere un programma che dati due punti in un piano cartesiano
#scrive l'equazone della retta associata e mandi in output il messaggio con
#con la positività la negativita del coefficiente angolare

import random

def calcolo_coefficiente (xUno,xDue,yUno,yDue):
    m = (yUno-yDue) / (xUno-xDue)
    return (m)

def equazione(m, x, y):
    eq= "y-"+str(y)+"="+str(m)+"(x-"+str(x)+")"
    print(eq)

def contollo_m (m):
    if m > 0:
        print("m ha segno positivo")
    elif m==0 :
        print("m è nullo")
    else:
        print ("m è negativo")
def incremento_uno(a):
    a=a+1
    prin(a)
    
    
if __name__ == "__main__":
    xUno = random.randint (-20,20)
    xDue = random.randint (-20,20)
    yUno = random.randint (-20,20)
    yDue = random.randint (-20,20)
    
    coefficiente_angolare = calcolo_coefficiente (xUno,xDue,yUno,yDue)
    print ( coefficiente_angolare )
    
    equazione(coefficiente_angolare, xDue, yDue)
    
    contollo_m(coefficiente_angolare)
    
    incremento_uno(xUno)