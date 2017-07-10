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