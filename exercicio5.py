num=[]
continua = True
while continua == True :
    numero=int(input("Insira um numero ou digite 0 para parar: "))
    if numero == 0:
        continua = False
    else:
        num.append(numero)
print(str(sum(num)))