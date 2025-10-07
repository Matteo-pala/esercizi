#creazione dizionario

tom = {}

#inserire un elemento nel dizionario

tom["primo"]=2
tom["secondo"] = 4

#creazione di un secondo dizionario con inizializzazione

sam = {"primo":6,"secondo":8}

#accede agli elementi del dizionario
tom["primo"]+sam["primo"]

#scorrere gli elementi di un dizionario
for key, valute in tom.items():
    print("la chiave è :" + key)
    print("il valore corrisopndente è :" +str(valute))