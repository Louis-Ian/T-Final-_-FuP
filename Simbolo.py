#-*- coding:utf-8 -*-
SimbP1=0
SimbP2=1

def simbolo():
	Simb = raw_input("Símbolo do jogador 1: ")

	global SimbP1
	global SimbP2

	if Simb == "X":
		SimbP1 = "X"
		SimbP2 = "O"
	elif Simb == "O":
		SimbP1 = "O"
		SimbP2 = "X"
	else:
			print("Insira símbolos válidos 'X' ou 'O':")
			return simbolo()

#debug

#simbolo()
#print SimbP1
#print SimbP2