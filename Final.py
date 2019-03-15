# -*- coding: utf-8 -*-
#

#Integrantes da equipe:
#Adaías Abner Brito Silva - 400657
#Hélio Matheus Sales Silva - 400800
#Louis Ian Silva dos Santos - 402525

#As duas funções a seguir comparam as coordenadas entradas pelos jogadores 
# e identificam a posição(linha e coluna) em que o símbolo deve ser colocado
def linha(v): #Função que recebe um vetor e retorna o índice da linha
	v1=['1','2','3'] #Vetor das linhas.
	i=0
	while v[1]!=v1[i]:
		i+=1
	return i
	
def coluna(v): #Função que recebe um vetor e retorna o índice da coluna
	v2=['A','B','C'] #Vetor das coordenadas da colunas.
	j=0
	while v[0]!=v2[j]:
		j+=1
	return j

#Os valores retornados pelas funções serão usados na 'matriz' para identificar os índices em que será inserido o símbolo.

Matriz = [[' ', ' ', ' '],[' ', ' ', ' '],[' ',' ', ' ']] #Vetor que receberá os X's e O's para aplicá-los na figura do jogo da velha.

def tabela(vetor = ["A","1"], simb = " "): #Função que recebe o símbolo como parâmetro e, ao chamar as funções linha e coluna, define onde ele deve ser inserido na figura e a retorna atualizada.
	
	coluna = ord(vetor[0])-65
	linha = int(vetor[1])-1

	Matriz[linha][coluna] = simb
	
	print ( "\n  A   B   C")
	print ("1 %s | %s | %s 1" %( Matriz[0][0], Matriz[0][1], Matriz[0][2]) )
	print (" ---+---+---")
	print ("2 %s | %s | %s 2" %( Matriz[1][0], Matriz[1][1], Matriz[1][2])  )
	print (" ---+---+---")
	print ("3 %s | %s | %s 3" %( Matriz[2][0], Matriz[2][1], Matriz[2][2])  )
	print ("  A   B   C\n")
	#Os prints's acima imprimem a figura sendo que as posições da "matriz" coord já estão identificadas com os seus lugares na figura.

#rotacionadorx e rotacionadory, sao vetores que formaram as possiveis posicoes u1,u2,v1,v2
#de 1 em 1, ela busca a proxima para formar uma sequencia 
#de 2 em 2, ela vira de posicao

rotacionadorX=[0,0,1,2,1,2,1,2,0,0,-1,-2,-1,-2,-1,-2,0,0,1,-1,1,-1,-1,1]
rotacionadorY=[1,2,1,2,0,0,-1,-2,-1,-2,-1,-2,0,0,1,2,1,-1,1,-1,0,0,1,-1]

#funcao ganhou verifica se existe uma sequencia de  3 simbolos iguais 
#posicao x e posicao y, sao as coordenadas que estamos verificando e simbPi eh o simbolo que ela carrega
#posicao u1,v1,u2,v2 sao as possiveis posicao da matriz verificaremos seus simbolos para sinalizar a sequencia
#uma matriz 3x3, varias posicoes de 0 a 2, portanto sao os limites das possiveis posicoes

def ganhou(matriz,posicaoX,posicaoY, simbPi):  #Função que verifica se um jogador ganhou a partida através da verificação de uma sequência de três símbolos iguais. SimbPi é X ou O.
	k=-2				
	while(k<=20):		
		k+=2			
		posicaoU1=posicaoX + rotacionadorX[k]   
		posicaoV1=posicaoY + rotacionadorY[k]	
		posicaoU2=posicaoX + rotacionadorX[k+1]	
		posicaoV2=posicaoY + rotacionadorY[k+1]	
		if (posicaoU1>=0 and posicaoU1<=2 and posicaoV1>=0 and posicaoV1<=2 and posicaoU2>=0 and posicaoU2<=2 and posicaoV2>=0 and posicaoV2<=2):
			if (matriz[posicaoV1][posicaoU1]==simbPi and matriz[posicaoV2][posicaoU2]==simbPi): 
				return 1
	return 0

#funcao previsao verifica se existe duas sequencias possiveis com ' ' e um simbolo determinado por simbPi
#mesmo funcionamento da funcao ganhou

def previsao(matriz,posicaoX,posicaoY, simbPi): 
	k=-2				
	while(k<=20):		
		k+=2			
		posicaoU1=posicaoX + rotacionadorX[k]   
		posicaoV1=posicaoY + rotacionadorY[k]	
		posicaoU2=posicaoX + rotacionadorX[k+1]	
		posicaoV2=posicaoY + rotacionadorY[k+1]	
		if (posicaoU1>=0 and posicaoU1<=2 and posicaoV1>=0 and posicaoV1<=2 and posicaoU2>=0 and posicaoU2<=2 and posicaoV2>=0 and posicaoV2<=2):
			if ((matriz[posicaoV1][posicaoU1]==simbPi and matriz[posicaoV2][posicaoU2]==' ') or (matriz[posicaoV1][posicaoU1]==' ' and   matriz[posicaoV2][posicaoU2]==simbPi)): 
				while(k<=20):
					k+=2
					posicaoU01=posicaoX + rotacionadorX[k]   
					posicaoV01=posicaoY + rotacionadorY[k]
					posicaoU02=posicaoX + rotacionadorX[k+1]
					posicaoV02=posicaoY + rotacionadorY[k+1]
					if (posicaoU01>=0 and posicaoU01<=2 and posicaoV01>=0 and posicaoV01<=2 and posicaoU02>=0 and posicaoU02<=2 and posicaoV02>=0 and posicaoV02<=2):
						if ((matriz[posicaoV01][posicaoU01]==simbPi and matriz[posicaoV02][posicaoU02]==' ') or (matriz[posicaoV01][posicaoU01]==' ' and matriz[posicaoV02][posicaoU02]==simbPi)):
							return 1
	return 0

def jogadaPlayer(): #Função que solicita as coordenadas ao player,
	# valida entrada e retorna posição da jogada
	Coords = input("Insira as coordenadas da casa desejada: ")
	Coords = list(Coords) #separa todas a letras recebidas, criando uma string

	tamanho = len(Coords)

	if tamanho==1: #Se a coordenada for muito curta, solicita uma nova coodenada
		print("Insira posições válidas, letra seguida de número.")
		return jogadaPlayer()

	else: #Se tiver pelo menos dois caracteres nas coordenadas
		
		entradaLinha = Coords[0]
		entradaColuna = Coords[1]
		
		if(ord(entradaLinha) >= 48 and ord(entradaLinha) <= 57): #Se a primeira letra for um número, solicita uma nova coordenada
			print("Insira posições válidas, letra seguida de número.")
			return jogadaPlayer()

		else:
			if(Coords[1] != "1" and Coords[1] != "2" and Coords[1] != "3"):#Se a segunda letra não for um numero valido

				if(ord(entradaColuna) >= 48 and ord(entradaColuna) <= 57):#mas era um numero(o usuario errou a coordenada)
					print("Insira posições válidas.")
					return jogadaPlayer()

				else:#Nem era um numero
					Coords.pop(1)#retirasse, pois há a possibilidade de ser só um sinal

					if(Coords[1] != "1" and Coords[1] != "2" and Coords[1] != "3"):#se mesmo assim a entrada não for valida
						print("Insira posições válidas.")
						return jogadaPlayer()

		if(ord(entradaLinha) >= 65 and ord(entradaLinha) <=67):#Se for uma letra maiúscula, será exatamente como queremos
			return Coords

		elif(ord(entradaLinha) >= 97 and ord(entradaLinha) <=99):#Se for uma letra minúscula, transformasse em uma letra maiúscula
			Coords[0]=chr((ord(entradaLinha))-32) #Transformando e letra maiúscula usando ascii
			return Coords
		
		else: #caso não fosse uma entrada valida
			print("Insira posições válidas.")
			return jogadaPlayer()

def validadorDeCoord(vetorComCoordenas): #Função que checa se a coordenada inserida já está sendo utilizada e retorna falso0 caso o local
	# seja inválido, e verdadeiro caso contrário
	
	#Transformasse as variáveis linha e coluna em indices para serem utilizados na matriz coord
	Linha = linha(vetorComCoordenas)
	Coluna = coluna(vetorComCoordenas)

	if (Matriz[Linha][Coluna] != " "): #Se a posição inserida não possui um espaço, ela já está sendo usada
		print("Insira coordenadas ainda não utilizadas.")
		return False 
	
	else:
		return True

def simbolo(): #Função validadora do Símbolo (X ou O), que recebe uma letra e retorna um vetor
	Simb = input("Símbolo do jogador 1: ") 
	print("")
	SimbReturn = [] 

	if Simb == "X": #Caso o símbolo inserido seja um X, retorna um vetor ["X","O"]
		SimbReturn += Simb
		SimbReturn += "O"
		return SimbReturn

	elif Simb == "O": #Caso o símbolo inserido seja um O, retorna um vetor ["O","X"]
		SimbReturn += Simb
		SimbReturn += "X"
		return SimbReturn

	else: #Caso o símbolo inserido nem seja um X nem um O
		print("Insira símbolos válidos 'X' ou 'O':")
		return simbolo()

vitoriasP1=0 #Contador de vitórias do Jogador 1.
vitoriasP2=0 #Contador de vitórias do Jogador 2.
empate=0 #Contador de empates.
partida=1 #Indica o número da partida atual.
inicio=1 #Serve para saber se uma partida deve ser recomeçada ou não.
g=0 
previsao2=0
previsao1=0

while (inicio!=0): #0 significa: "Não recomeçar um partida"
	
	Matriz = [[' ', ' ', ' '],[' ', ' ', ' '],[' ',' ', ' ']] #Inicializando a matriz

	print ("\nPARTIDA ", partida,":\n")
	simbolos = simbolo()
	SimbP1 = simbolos[0] #Atribuindo os símbolos do jogador 1 do jogador 2
	SimbP2 = simbolos[1]

	rodada=0 #Contador do número da rodada dentro da partida.
	vencedor = False #Indica se já existe um vencedor.

	tabela()

	while(rodada<=10 and vencedor==False):
		
		rodada+=1
		
		if rodada%2!=0 and rodada<10: #Se a rodada for ímpar o Jogador1 deve jogar.
			print("JOGADOR 1: ")
			
			SituacaoDasCoordenadas = False #Inicializando a variável
			while(SituacaoDasCoordenadas==False): #Enquanto as coordenadas forem invalidas, solicita novas coordenadas
				entrada = jogadaPlayer()
				SituacaoDasCoordenadas = validadorDeCoord(entrada)

			posicaox=coluna(entrada) #Coordenadas do símbolo inserido por último.
			posicaoy=linha(entrada) #Coordenadas do símbolo inserido por último.

			tabela(entrada,SimbP1) #Chama a tabela para ser atualizada e mostrada aos jogadores.
			
			if (rodada>=5):
				g=ganhou(Matriz,posicaox,posicaoy,SimbP1)
				if (g==1):
					vitoriasP1+=1
					vencedor=1
					print ("JOGADOR 1 VENCEU O JOGO ", partida)
				if (g==0 and previsao2==1):
					vitoriasP2+=1
					vencedor=1
					print ("JOGADOR 2 JÁ VENCEU O JOGO ", partida)
				for m in range(3):
					for n in range(3):
						if (Matriz[n][m]==SimbP1 and previsao1==0):
						 	previsao1=previsao(Matriz,m,n,SimbP1)

		if rodada%2==0 and rodada<10: #Se a rodada for par o jogador 2 deve jogar.
			print("JOGADOR 2: ")

			SituacaoDasCoordenadas = False #Inicializando a variável
			while(SituacaoDasCoordenadas==False):  #Enquanto as coordenadas forem invalidas, solicita novas coordenadas
				entrada2 = jogadaPlayer()
				SituacaoDasCoordenadas = validadorDeCoord(entrada2)

			posicaox=coluna(entrada2) #Coordenadas do símbolo inserido por último.
			posicaoy=linha(entrada2) #Coordenadas do símbolo inserido por último.

			tabela(entrada2,SimbP2)#Chama a tabela para ser atualizada e mostrada aos jogadores.
			
			if (rodada>=5):
				g=ganhou(Matriz,posicaox,posicaoy,SimbP2)
				if (g==1):
					vitoriasP2+=1
					vencedor=1
					print ("JOGADOR 2 VENCEU O JOGO ", partida)
				if (g==0 and previsao1==1):
					vitoriasP1+=1
					vencedor=1
					print ("JOGADOR 1 JÁ VENCEU O JOGO ", partida)
				for m in range(3):
					for n in range(3):
						if (Matriz[n][m]==SimbP2 and previsao2==0):
						  	previsao2=previsao(Matriz,m,n,SimbP2)

		if rodada==10: #caso seja a rodada 10,o empate é declarado e o placar é alterado.
			print ("NINGUEM VENCEU O JOGO ", partida, ".\n")
			empate+=1

	partida+=1
	vencedor=False #Vencedor é reinicializado
	g = 0
	previsao1=0
	previsao2=0
	print ("Usuario 1: ", vitoriasP1, "\nUsuario 2: ",vitoriasP2) #placar.
	print ("Empates: ", empate)
	inicio=input("\nDigite 0 para acabar o jogo\nou 1 para continuar jogando:")
	 #O jogador escolhe se vai continuar jogando ou não
