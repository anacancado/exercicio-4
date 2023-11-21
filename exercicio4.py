listacompras=[]
continua = True
while continua == True :
    item= (input("Insira o item a lista de compras ou digite 'pare' para parar: "))
    if item =='pare' :
        continua = False
    else:
        listacompras.append(item)
print (listacompras)