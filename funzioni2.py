# scricrivere una funzione che dati due numeri interi restituisca il maggiore

def nMaggiore (numUno,numDue):
    if numUno > numDue:
        return numUno
    else:
        return numDue
#scrivere una procedura che dato un numero intero stampia video se è pari o dispari
    
def nPariDsiapari(numero1):
    if numero1%2==0:
        print("il numero è pari")
    else:
        print("il numero è dispari")


uno=input("inserire il primo numero")
uno=int(uno)
due=input("inserisci il secondo numero")
due=int(due)

risultato = nMaggiore(uno,due)
print(risultato)
nPariDispari(risultato)

#con questo esercizio ho creato un programma che dati due interi stampi a video
#se il maggiore è pari o dispari

#risultato2=nMaggiore(uno)
#nPariDispari(uno,due)