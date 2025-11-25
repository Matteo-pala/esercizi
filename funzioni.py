# funzioni: bloccco generico che viene eseguito al variare dei parametri

def sommaLista (lista):
    somma = 0
    for element in lista:
        somma = somma + element
    print(somma)

    
lista = [1,2,3,4]
sommaLista(lista)



# scrivere una funzione data una lista stampi a video il numero degli elementi pari

def nPari(lista):
    contatore = 0
    for element in lista:
        if element % 2 == 0:
            contatore = contatore + 1 
    print(contatore)
    
lista = [1,2,3,4]
nPari(lista)