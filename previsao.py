rotacionadorX=[0,0,1,2,1,2,1,2,0,0,-1,-2,-1,-2,-1,-2,0,0,1,-1,1,-1,-1,1]
rotacionadorY=[1,2,1,2,0,0,-1,-2,-1,-2,-1,-2,0,0,1,2,1,-1,1,-1,0,0,1,-1]

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