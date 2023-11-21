numeros=[1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]
numMaior=0
numMenor=numeros[0]
for x in numeros:
    if x>numMaior:
        numMaior=x
print("O maior numero da lista é "+str(numMaior))
for x in numeros:
    if x<numMenor:
        numMenor=x
print("O menor numero da lista é "+str(numMenor))