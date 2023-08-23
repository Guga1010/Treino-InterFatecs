# Spins que abre/fecha quantum gates. Caso o número do quantum gate dividido pelo número do spin tiver resto 0, o quantum gate é aberto.
# O número de spins é igual ao número de quantum gates.

#Entrada: 
    # n linhas - quantidade de spins.                                       Ex: 2
    # última linha - deve ser 0 para indicar o fim da entrada de spins.     Ex: 0

#Saída:
    # n linhas - indica o número do quantum gates que ficou aberto          Ex: 1

arqE = open("./input.txt","r")
linhas = arqE.readlines()

arqS = open("output.txt","w")
for linha in linhas:
    if(int((linha.strip())) == 0):
        break

    qtd = int(linha.strip())
    quantumGates = ['C'] * qtd
    i = 1
    opened = 0
    while(i <= qtd):
        vetor = 0
        while(vetor <= (qtd-1)):
            if(((vetor+1) % i) == 0):
                if(quantumGates[vetor] == 'C'):
                    quantumGates[vetor] = 'O'
                else:
                    quantumGates[vetor] = 'C'

            if(i == qtd and quantumGates[vetor] == 'O'):
                arqS.write(str(vetor+1)+" ")
            
            vetor+=1
        i+=1
    arqS.write("\n")
        
arqS.close()