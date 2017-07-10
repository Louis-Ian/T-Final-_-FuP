#-*- coding:utf-8 -*-

coord = [[' ', ' ', ' '],[' ', ' ', ' '],[' ',' ', ' ']]

def tabela(vetor, simb): #Função que recebe o símbolo como parâmetro e, ao chamar as funções linha e coluna, define onde ele deve ser inserido na figura e a retorna atualizada.
	
	coluna = ord(vetor[0])-65
	linha = int(vetor[1])-1

	if (coord[linha][coluna] != " "):
		print("Insira coordenadas que ainda não utilizadas:")
		return 1

	else:
		coord[linha][coluna] = simb
		
		print  "  A   B   C"
		print "1 %s | %s | %s 1" %( coord[0][0], coord[0][1], coord[0][2]) 
		print " ---+---+---"
		print "2 %s | %s | %s 2" %( coord[1][0], coord[1][1], coord[1][2])  
		print " ---+---+---"
		print "3 %s | %s | %s 3" %( coord[2][0], coord[2][1], coord[2][2])  
		print "  A   B   C \n"
		#Os prints's acima imprimem a figura sendo que as posições da "matriz" coord já estão identificadas com os seus lugares na figura.

#debug
#jogada = ["A","2"]
#tabela(jogada,"X")