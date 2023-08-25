# Spins que abre/fecha quantum gates. Caso o número do quantum gate dividido pelo número do spin tiver resto 0, o quantum gate é aberto.
# O número de spins é igual ao número de quantum gates.

#Entrada: 
    # n linhas - quantidade de spins.                                       Ex: 2
    # última linha - deve ser 0 para indicar o fim da entrada de spins.     Ex: 0

#Saída:
    # n linhas - indica o número do quantum gates que ficou aberto          Ex: 1

arqE = open("./input.txt","r")
linhasArq = arqE.readlines()
linhaDimensao = linhasArq[1].split()

forcaSilas = int(linhasArq[0].strip())
qtdLinhas = int(linhaDimensao[0].strip())
qtdColunas = int(linhaDimensao[1].strip())

vetorBidi = []
i = 2
while(i <= qtdLinhas+1):
    vetorBidi.append(linhasArq[i].split())
    i+=1


posXKey = 0
posYKey = 0
for linha in range(0,qtdLinhas):
    for coluna in range(0,qtdColunas):
        if(vetorBidi[linha][coluna] == 'K'):
            posXKey = linha
            posYKey = coluna

def verificarPos(alvoX,alvoY):
    valorPosicao = vetorBidi[alvoX][alvoY]
    if(valorPosicao == "."):
        return True
    elif(valorPosicao == 'K'):
        return True
    elif(valorPosicao == "#"):
        return False
    else:
        if(forcaSilas >= int(valorPosicao)):
            return True
        else:
            return False
    


posXSilas = 0
posYSilas = 0
countMoviment = 0
while(posXSilas != posXKey or posYSilas != posYKey):
    print(str(posXSilas)+":"+str(posYSilas))
    if(posYSilas < posYKey):
        if(verificarPos(posXSilas,posYSilas+1)):
            posYSilas+=1
            countMoviment+=1
            continue
        elif(verificarPos(posXSilas+1,posYSilas)):
            posXSilas+=1
            countMoviment+=1
            continue
        elif((posXSilas+1 == qtdLinhas-1) and (posYSilas+1 == qtdColunas-1)):
            countMoviment = 'N'
            break
        while(True):
            posYSilas-=1
            print(str(posXSilas)+":"+str(posYSilas))
            if(verificarPos(posXSilas+1,posYSilas)):
                posXSilas+=1
                break
    elif(posXSilas < posXKey):
        if(verificarPos(posXSilas+1,posYSilas)):
            posXSilas+=1
            countMoviment+=1
        else:
            verificarPos(posXSilas,posYSilas-1)
        
arqS = open("output.txt","w")
arqS.write(str(countMoviment))
arqS.close()