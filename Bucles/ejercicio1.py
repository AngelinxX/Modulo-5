lista = [1,2,3,4,5, "Antony", "Pedro",1,2,3,4,8,7,7,"Antony"] 

elemento = "Antony"

for i in lista:
    #print(i, end = (","))
    if elemento == i:
        print(f"El elemento {elemento} esta dentro de la lista")
