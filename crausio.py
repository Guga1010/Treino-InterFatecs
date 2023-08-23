# Robô de limpeza que anda pela casa através de sua rotina indicada

#Entrada: 
    # primeira linha - número de linhas, colunas e a bateria.                            Ex: 7 5 10
    # segunda linha  - x inicial, y inicial.                                             Ex: 1 1
    # terceira linha - rotina a ser realizada, cima(C),baixo(B),esquerda(E),direita(D).  Ex: CBCDECBDEB

#Saída:
    # posição final do x, y, e a quantidade de vezes que ele bateu                         Ex: 3 1 2

arqE = open("./input.txt","r")
linhas = arqE.readlines()
linha1Arq = linhas[0].split()
posicaoI = linhas[1].split()
rotina = linhas[2]

limL = int(linha1Arq[0])
limC = int(linha1Arq[1])
bateria = int(linha1Arq[2])
posL = int(posicaoI[0])
posC = int(posicaoI[1])

rotinaAtual = 0
batidas = 0

while(bateria > 0):
    if(rotina[rotinaAtual] == 'C'):
        if(posL == 1):
            batidas+=1
        else:
            posL-=1
    elif(rotina[rotinaAtual] == 'B'):
        if(posL == limL):
            batidas+=1
        else:
            posL+=1
    elif(rotina[rotinaAtual] == 'E'):
        if(posC == 1):
            batidas+=1
        else:
            posC-=1
    elif(rotina[rotinaAtual] == 'D'):
        if(posC == limC):
            batidas+=1
        else:
            posC+=1
    bateria-=1
    rotinaAtual+=1

arqS = open("output.txt","w")
arqS.write(str(posL)+" "+str(posC)+" "+str(batidas))

arqS.close()