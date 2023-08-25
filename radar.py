# Encontrar a velocidade que o radar pode multar o infrator
# Se velocidade for menor ou igual a 107, poderá atingir no máximo a sua velocidade mais 7
# Se velocidade for maior que 107, poderá atingir a sua velocidade mais 7% de seu valor(velocidade + ((velocidade x 7)/100))

#Entrada: 
    # linha - velocidade nominal     Ex: 80

#Saída:
    # linha - velocidade maxima      Ex: 87

arqE = open("./input.txt","r")
linhasArq = arqE.readlines()

velocidadeNom = int(linhasArq[0])

if(velocidadeNom <= 107):
    velocidadeMaxima = velocidadeNom + 7
else:
    velocidadeMaxima = velocidadeNom + (round((velocidadeNom * 7) / 100))

arqS = open("output.txt","w")

arqS.write(str(velocidadeMaxima))
arqS.close()