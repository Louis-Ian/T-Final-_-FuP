# -*- coding: utf-8 -*-

def jogadaPlayer(): #Função que recebe a linha e a coluna do player,
	# valida entrada e retorna posição da jogada
	Coords = raw_input("Insira as coordenadas da casa desejada:")
	Coords = list(Coords) #separa todas a letras recebidas, criando uma string

	tamanho = len(Coords)

	if(tamanho >= 2)
		entradaLinha = Coords[0]#variáveis criadas para saber se a entrada é valida
		if((ord(entradaLinha) >= 48 and ord(entradaLinha) <= 57) or not Coords[1]):
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
	else:
		print("Insira posições válidas, letra seguida de número.")
		return jogadaPlayer()

#debug(eu nem preciso disso, pffff)
teste = jogadaPlayer()
print(teste)