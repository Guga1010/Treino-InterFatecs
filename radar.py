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