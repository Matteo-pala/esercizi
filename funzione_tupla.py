#scrivere un programma che dati due punti in un piano cartesiano
#scrive l'equazone della retta associata e mandi in output il messaggio con
#con la positività la negativita del coefficiente angolare

import random

def calcolo_coefficiente (tuplaUno,tuplaDue):
    m = (tuplaDue[1]-tuplaUno[1]) / (tuplaDue[0]-tuplaUno[0])
    return (m)

def equazione(m, tuplaDue):
    eq= "y-"+str(tuplaDue[1])+"="+str(m)+"(x-"+str(tuplaDue[0])+")"
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
    puntoUno=(random.randint (-20,20),random.randint (-20,20))
    puntoDue=(random.randint (-20,20),random.randint (-20,20))

    
    coefficiente_angolare = calcolo_coefficiente (puntoUno,puntoDue)
    print ( coefficiente_angolare )
    
    equazione(coefficiente_angolare, puntoDue)
    
    contollo_m(coefficiente_angolare)
    
    #incremento_uno(xUno)