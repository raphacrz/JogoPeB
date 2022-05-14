
mesa=['p','p',' ','b','b']
def s(mesa):
	if mesa[0]==' ':
		mesa[0]=mesa[2]
		mesa[2]=' '
		return [mesa]
	elif mesa[1]==' ':
		mesa[1]=mesa[3]
		mesa[3]=' '
		return [mesa]
	elif mesa[2]==' ':
		mesac1=mesa.copy()
		mesac2=mesa.copy()
		mesac1[2]=mesac1[0]
		mesac1[0]=' '
		mesac2[2]=mesac2[4]
		mesac2[4]=' '
		return [mesac1,mesac2]

	elif mesa[3]==' ':
		mesa[3]=mesa[1]
		mesa[1]=' '
		return [mesa]
	elif mesa[4]==' ':
		mesa[4]=mesa[2]
		mesa[2]=' '
		return [mesa]

def d(mesa):
	if mesa[0]=='':
		mesa[0]=mesa[1]
		mesa[1]=' '
		return [mesa]
	elif mesa[1]==' ':
		mesac1=mesa.copy()
		mesac1[1]=mesac1[0]
		mesac1[0]=' '
		mesac2=mesa.copy()
		mesac2[1]=mesac2[2]
		mesac2[2]=' '
		return [mesac1,mesac2]
	elif mesa[2]==' ':
		mesac1=mesa.copy()
		mesac1[2]=mesac1[1]
		mesac1[1]=' '
		mesac2=mesa.copy()
		mesac2[2]=mesac2[3]
		mesac2[3]=' '
		return [mesac1,mesac2]
	elif mesa[3]==' ':
		mesac1=mesa.copy()
		mesac1[3]=mesac1[2]
		mesac1[2]=' '
		mesac2=mesa.copy()
		mesac2[3]=mesac2[4]
		mesac2[4]=' '
		return [mesac1,mesac2]
	elif mesa[4]=='':
		mesa[4]=mesa[3]
		mesa[3]=' '
		return [mesa]
	
def gerafilhos(mesa):
	filhos=s(mesa)+d(mesa)
	return filhos

def final(mesa):
	if mesa==['b','p','p','b',' '] or mesa==[' ','b','p','p','b']:
		return True
	else:
		return False

def profundidade(mesa, visitadas, proximos, cont):
	print("atual: "+str(mesa))
	if final(mesa)==True:
		print("achei")
		return mesa
	visitadas.append(mesa)	
	filhos=gerafilhos(mesa)
	for filho in filhos:
		if filho not in visitadas:
			proximos.append(filho)	#Adiciona elemento no fim da lista (topo da stack)
	for i in range(len(proximos)-1):
		atual=proximos.pop(-1) 		#Retira elemento do fim da lista (topo da stack)
		if atual not in visitadas:
			cont[0]=cont[0]+1
			teste=profundidade(atual,visitadas, proximos.copy(), cont)
			if teste:
				return teste

def largura(mesa, visitadas, proximos, cont):
	print("atual: "+str(mesa))
	if final(mesa)==True:
		print("achei")
		return mesa
	visitadas.append(mesa)
	filhos=gerafilhos(mesa)
	for filho in filhos:
		if filho not in visitadas:
			proximos.append(filho)	#Adiciona elemento no fim da lista (inicio da queue)
	for i in range(len(proximos)-1):
		atual=proximos.pop(0)		#Retira elemento do inicio da lista (fim da queue)
		if atual not in visitadas:
			cont[0]=cont[0]+1
			teste=largura(atual,visitadas, proximos, cont)
			if teste:
				return teste

#Lógica: Pontuar os possíveis estados da mesa em relação a ordem desejada no final
def heuristica(mesa):
	pontos=0
	for i in range(4):
		if mesa[i]=='b' and mesa[i+1]=='b':
			pontos-=1
		if mesa[i]=='p' and mesa[i+1]=='p':
			pontos+=1
		if mesa[i]=='b' and mesa[i+1]=='p':
			pontos+=1
		if mesa[i]=='p' and mesa[i+1]=='b':
			pontos+=1
		if mesa[i]=='p' and mesa[i+1]=='p':
			pontos+=1
		if mesa[i]==' ' and mesa[i+1]=='b':
			pontos+=1
		if mesa[i]=='b' and mesa[i+1]==' ':
			pontos+=1
		if mesa[i]==' ' and mesa[i+1]=='p':
			pontos-=1
		if mesa[i]=='p' and mesa[i+1]==' ':
			pontos-=1
	return pontos


#Insere um nó na lista de forma ordenada pela pontuação dada pela heurística
def insere(mesa, v):
	valor=heuristica(mesa)
	if len(v)==0:
		v.append(mesa)
	else:
		for i in range(len(v)):
			valoratual=heuristica(v[i])
			if valoratual<valor:
				v.insert(i,mesa)
				return 
		v.append(mesa)

	
def bests(mesa, visitadas, proximos, cont):
	print("atual: "+str(mesa))
	if final(mesa)==True:
		print("achei")
		return mesa
	visitadas.append(mesa)
	filhos=gerafilhos(mesa)
	for filho in filhos:
		if filho not in visitadas:
			insere(filho,proximos)
	for i in range(len(proximos)-1):
		atual=proximos.pop(0)
		if atual not in visitadas:
			cont[0]=cont[0]+1
			teste=bests(atual,visitadas, proximos.copy(), cont)
			if teste:
				return teste

print("Utilizando busca em largura: ")
visitadas=[]
proximos=[]
cont =[0]
largura(mesa, visitadas, proximos, cont)
print(cont)

print("Utilizando busca em profundidade: ")
mesa=['p','p',' ','b','b']
visitadas=[]
proximos=[]
cont =[0]
profundidade(mesa, visitadas, proximos, cont)
print(cont)

print("Utilizando busca heuristica pelo melhor: ")
mesa=['p','p',' ','b','b']
visitadas=[]
proximos=[]
cont =[0]
bests(mesa, visitadas, proximos, cont)
		
print(cont)