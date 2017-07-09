# -*- coding: utf-8 -*-

#Esses dois vetores a seguir(v1 e v2) são referências para comparar as coordenadas entradas pelos jogadores e, assim, identificar a posição(linha e coluna) em que o X ou 0 devem ser colocados.
def linha(v): #Função que retorna o valor de i, o qual é o número da linha da figura do jogo.
	v1=['1','2','3']  #Vetor das coordenadas das linhas.
	i=0
	while v[1]!=v1[i]:
		i+=1
	return i
	
def coluna(v): #Função que retorna o valor de j, o qual é o número da coluna da figura do jogo.
	v2=['A','B','C'] #Vetor das coordenadas da colunas.
	j=0
	while v[0]!=v2[j]:
		j+=1
	return j

#'i' e 'j' serão usados na 'matriz' coord para identificar a posição em que será inserido o símbolo(X ou O).

coord = [[' ', ' ', ' '],[' ', ' ', ' '],[' ',' ', ' ']] #Vetor que receberá os X's e O's para aplicá-los na figura do jogo da velha.

def tabela(vetor, simb): #Função que recebe o símbolo como parâmetro e, ao chamar as funções linha e coluna, define onde ele deve ser inserido na figura e a retorna atualizada.
	
	coluna = ord(vetor[0])-65
	linha = int(vetor[1])-1

	coord[linha][coluna] = simb
	
	print  "  A   B   C"
	print "1 %s | %s | %s 1" %( coord[0][0], coord[0][1], coord[0][2]) 
	print " ---+---+---"
	print "2 %s | %s | %s 2" %( coord[1][0], coord[1][1], coord[1][2])  
	print " ---+---+---"
	print "3 %s | %s | %s 3" %( coord[2][0], coord[2][1], coord[2][2])  
	print "  A   B   C"
	#Os prints's acima imprimem a figura sendo que as posições da "matriz" coord já estão identificadas com os seus lugares na figura.


rotacionadorX=[0,0,1,2,1,2,1,2,0,0,-1,-2,-1,-2,-1,-2,0,0,1,-1,1,-1,-1,1]
rotacionadorY=[1,2,1,2,0,0,-1,-2,-1,-2,-1,-2,0,0,1,2,1,-1,1,-1,0,0,1,-1]


def ganhou(matriz,posicaoX,posicaoY, simbPi): #Função que verifica se um jogador ganhou a partida através da verificação de uma sequência de três símbolos iguais. SimbPi é X ou O.
	k=-2				
	while(k<=21):		
		k+=2			
		posicaoU1=posicaoX + rotacionadorX[k]   
		posicaoV1=posicaoY + rotacionadorY[k]	
		posicaoU2=posicaoX + rotacionadorX[k+1]	
		posicaoV2=posicaoY + rotacionadorY[k+1]	
		if (posicaoU1>=0 and posicaoU1<=2 and posicaoV1>=0 and posicaoV1<=2 and posicaoU2>=0 and posicaoU2<=2 and posicaoV2>=0 and posicaoV2<=2):
			if (matriz[posicaoV1][posicaoU1]==simbPi and matriz[posicaoV2][posicaoU2]==simbPi): 
				return 1
	return 0

def previsao(matriz,posicaoX,posicaoY, simbPi): #Função que prevê a vitória iminente do último jogador que inseriu um símbolo, ou seja, ela vai verificar se  ao redor do útlimo símbolo inserido existem duas maneiras de o jogo ser vencido pelo último que jogou.
	k=-2				
	while(k<=21):		
		k+=2			
		posicaoU1=posicaoX + rotacionadorX[k]   
		posicaoV1=posicaoY + rotacionadorY[k]	
		posicaoU2=posicaoX + rotacionadorX[k+1]	
		posicaoV2=posicaoY + rotacionadorY[k+1]	
		if (posicaoU1>=0 and posicaoU1<=2 and posicaoV1>=0 and posicaoV1<=2 and posicaoU2>=0 and posicaoU2<=2 and posicaoV2>=0 and posicaoV2<=2):
		  	if ((matriz[posicaoV1][posicaoU1]==simbPi and matriz[posicaoV2][posicaoU2]==' ') or (matriz[posicaoV1][posicaoU1]==' ' and   matriz[posicaoV2][posicaoU2]==simbPi)): 
	  	  		while(k<=21):
	  	 			k+=2
	  				posicaoU01=posicaoX + rotacionadorX[k]   
	  				posicaoV01=posicaoY + rotacionadorY[k]	
	  				posicaoU02=posicaoX + rotacionadorX[k+1]	
	  				posicaoV02=posicaoY + rotacionadorY[k+1]
	  				if (posicaoU01>=0 and posicaoU01<=2 and posicaoV01>=0 and posicaoV01<=2 and posicaoU02>=0 and posicaoU02<=2 and posicaoV02>=0 and posicaoV02<=2):
		  				if ((matriz[posicaoV01][posicaoU01]==simbPi and matriz[posicaoV02][posicaoU02]==' ') or (matriz[posicaoV01][posicaoU01]==' ' and matriz[posicaoV02][posicaoU02]==simbPi)):
		  					return 1 
	return 0

def jogadaPlayer(): #Função que recebe a linha e a coluna do player,
	# valida entrada e retorna posição da jogada
	Coords = raw_input("Insira as coordenadas da casa desejada:")
	Coords = list(Coords) #separa todas a letras recebidas, criando uma string

	entradaLinha = Coords[0]#variáveis criadas para saber se a entrada é valida
	entradaColuna = Coords[1]

	if(ord(entradaLinha) >= 48 and ord(entradaLinha) <= 57):
		print("Insira posições válidas, letra seguida de número.")
		return jogadaPlayer()
	else:
		if(Coords[1] != "1" and Coords[1] != "2" and Coords[1] != "3"):#Se a segunda letra não for um numero valido
			if(ord(entradaColuna) >= 48 and ord(entradaColuna) <= 57):#mas era um numero(erro so usuario)
				print("Insira posições válidas.")
				return jogadaPlayer()
			else:#Nem era um numero
				Coords.pop(1)#retirasse,possibilidade de ser só um sinal
				if(Coords[1] != "1" and Coords[1] != "2" and Coords[1] != "3"):#se mesmo assim a entrada não for valida
					print("Insira posições válidas.")
					return jogadaPlayer()

	if(ord(entradaLinha) >= 65 and ord(entradaLinha) <=67):#Se for uma letra maiúscula
	#Valida a primeira letra inserida	
		return Coords
	elif(ord(entradaLinha) >= 97 and ord(entradaLinha) <=99):
		Coords[0]=chr((ord(entradaLinha))-32)
		return Coords
	else:
	#caso não fosse uma entrada valida
		print("Insira posições válidas.")
		return jogadaPlayer()

def validadorDeCoord(vetorComCoordenas):
	
	Linha = linha(vetorComCoordenas)
	Coluna = coluna(vetorComCoordenas)

	if (coord[Linha][Coluna] != " "):
		print("Insira coordenadas que ainda não utilizadas:")
		return False
	else:
		return True

def simbolo():
	Simb = raw_input("Símbolo do jogador 1: ")

	SimbReturn = []

	if Simb == "X":
		SimbReturn += Simb
		SimbReturn += "O"
		return SimbReturn
	elif Simb == "O":
		SimbReturn += Simb
		SimbReturn += "X"
		return SimbReturn
	else:
		print("Insira símbolos válidos 'X' ou 'O':")
		return simbolo()

vitoriasP1=0 #Contador de vitórias do Jogador 1.
vitoriasP2=0 #Contador de vitórias do Jogador 2.
empate=0 #Contador de empates.
partida=1 #Indica o número da partida atual.
inicio=1 #Serve para saber se uma partida deve ser recomeçada ou não. Ver linhas 101 a 103
g=0
p=0

while (inicio!=0): #0 significa: "Não recomeçar um partida". Por isso um While foi usado.
	
	coord = [[' ', ' ', ' '],[' ', ' ', ' '],[' ',' ', ' ']]

	print "PARTIDA ", partida,":"
	simbolos = simbolo()
	SimbP1 = simbolos[0]
	SimbP2 = simbolos[1]

	rodada=0 #Contador do número da rodada dentro de uma determinada partida.
	vencedor = 0 #Indica se já existe um vencedor.
	while(rodada<=10 and vencedor==0):
	
		rodada+=1
		
		if rodada%2!=0 and rodada<10: #Se a rodada for ímpar o Jogador1 deve jogar. p1
			print("JOGADOR 1: ")
			
			SituacaoDasCoordenadas = False
			while(SituacaoDasCoordenadas==False):
				entrada = jogadaPlayer()
				SituacaoDasCoordenadas = validadorDeCoord(entrada)

			posicaox=coluna(entrada) #Coordenadas do símbolo inserido por último.
			posicaoy=linha(entrada) #Coordenadas do símbolo inserido por último.

			tabela(entrada,SimbP1) #Chama a tabela para ser atualizada e mostrada aos jogadores.
			
			if (rodada>=5):
				g=ganhou(coord,posicaox,posicaoy,SimbP1)
				if (g==1):
					vitoriasP1+=1
			  		vencedor=1
					print "JOGADOR 1 VENCEU O JOGO ", partida
			if (rodada>=3):
				for m in range(3):
					for n in range(3):
						if (coord[n][m]==SimbP1 and p!=1):
						  p=previsao(coord,m,n,SimbP1)
						  if (p==1):
						  	vitoriasP1+=1
			  		  		vencedor=1
						  	print "JOGADOR 1 JÁ VENCEU O JOGO ", partida

		if rodada%2==0 and rodada<10:
			print("JOGADOR 2: ")
			entrada2 = jogadaPlayer()

			posicaox=coluna(entrada2)
			posicaoy=linha(entrada2)

			tabela(entrada2,SimbP2)

			if (rodada>=5):
				g=ganhou(coord,posicaox,posicaoy,SimbP2)
				if (g==1):
					vitoriasP2+=1
				  	vencedor=1
					print "JOGADOR 2 VENCEU O JOGO ", partida
			if (rodada>=3):
				for m in range(3):
					for n in range(3):
						if (coord[n][m]==SimbP2 and p!=1):
						  p=previsao(coord,m,n,SimbP2)
						  if (p==1):
						  	vitoriasP2+=1
			  		  		vencedor=1
						  	print "JOGADOR 2 JÁ VENCEU O JOGO ", partida

		if rodada==10: #Verifica se houve empate.
			print "NINGUEM VENCEU O JOGO ", partida
			empate+=1

	partida+=1
	vencedor=0
	p = 0
	g = 0
	print "Usuario 1 ", vitoriasP1, " x ", vitoriasP2, " Usuario 2" #Mostra o placar.
	print "Empates: ", empate
	print "Digite 0 para acabar o jogo"
	print "Digite 1 para continuar jogando"
	inicio=input()
