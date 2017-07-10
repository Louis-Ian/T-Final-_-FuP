# -*- coding: utf-8 -* 

def validadorDeCoord(vetorComCoordenas):
	
	linha = linha(vetorComCoordenas[0])
	coluna = coluna(vetorComCoordenas[1])

	if (coord[linha][coluna] != " "):
		print("Insira coordenadas que ainda não utilizadas:")
		return False
	else:
		True

SituacaoDasCoordenadas = validadorDeCoord(entrada)

while(SituacaoDasCoordenadas)==False: #Chama a tabela para ser atualizada e mostrada aos jogadores.
	entrada = jogadaPlayer()
	SituacaoDasCoordenadas = validadorDeCoord(entrada)
tabela(entrada,SimbP1)