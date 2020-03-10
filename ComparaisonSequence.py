def reverseAll():
	global soluce1
	global soluce2
	for l in range(len(soluce1)):
		soluce1[l] = soluce1[l][::-1]
	for l in range(len(soluce2)):
		soluce2[l] = soluce2[l][::-1]

def getValue(i, j):
	global matrixChangement
	global seq1
	global seq2
	lettre1 = seq1[j]
	lettre2 = seq2[i]

	# print(i, j, lettre1, lettre2)

	index1 = 0
	index2 = 0
	if lettre1 == 'A':
		index1 = 0
	elif lettre1 == 'C':
		index1 = 1
	elif lettre1 == 'G':
		index1 = 2
	elif lettre1 == 'T':
		index1 = 3

	if lettre2 == 'A':
		index2 = 0
	elif lettre2 == 'C':
		index2 = 1
	elif lettre2 == 'G':
		index2 = 2
	elif lettre2 == 'T':
		index2 = 3

	# print(matrixChangement[index2][index1])
	return matrixChangement[index2][index1]

def fillMatrix(iteration, mode = "global"):
	global matrixValeur
	global matrixFleche
	global gap
	i = int(iteration/len(matrixValeur[0])) #ligne
	j = iteration%len(matrixValeur[0]) #colonne
	print(iteration," ",i," ",j)
	fin = False
	if i >= len(matrixValeur) or j >= len(matrixValeur[0]):
		fin = True
		return fin
	if mode == "global":
		if i-1 >= 0:
			if j-1 >= 0:
				value = getValue(i-1,j-1)
				matrixValeur[i][j] = max(matrixValeur[i-1][j]+gap, matrixValeur[i][j-1]+gap, matrixValeur[i-1][j-1]+value)
				if matrixValeur[i][j] == matrixValeur[i-1][j]+gap:
					matrixFleche[i][j][0] = True #haut
				if matrixValeur[i][j] == matrixValeur[i][j-1]+gap:
					matrixFleche[i][j][1] = True #gauche
				if matrixValeur[i][j] == matrixValeur[i-1][j-1]+value:
					matrixFleche[i][j][2] = True #diag
			else:
				matrixValeur[i][j] = matrixValeur[i-1][j]+gap
				matrixFleche[i][j][0] = True #haut
		else:
			if j-1 >= 0:
				matrixValeur[i][j] = matrixValeur[i][j-1]+gap
				matrixFleche[i][j][1] = True #gauche
			else:
				matrixValeur[i][j] = 0
	elif mode == "local":
		if i-1 >= 0:
			if j-1 >= 0:
				value = getValue(i-1,j-1)
				matrixValeur[i][j] = max(matrixValeur[i-1][j]+gap, matrixValeur[i][j-1]+gap, matrixValeur[i-1][j-1]+value,0)
				if matrixValeur[i][j] == matrixValeur[i-1][j]+gap:
					matrixFleche[i][j][0] = True #haut
				if matrixValeur[i][j] == matrixValeur[i][j-1]+gap:
					matrixFleche[i][j][1] = True #gauche
				if matrixValeur[i][j] == matrixValeur[i-1][j-1]+value:
					matrixFleche[i][j][2] = True #diag
			else:
				matrixValeur[i][j] = max(matrixValeur[i-1][j]+gap,0)
				if matrixValeur[i][j] == matrixValeur[i-1][j]+gap:
					matrixFleche[i][j][0] = True #haut
		else:
			if j-1 >= 0:
				matrixValeur[i][j] = max(matrixValeur[i][j-1]+gap,0)
				if matrixValeur[i][j] == matrixValeur[i][j-1]+gap:
					matrixFleche[i][j][1] = True #gauche
			else: #coin
				matrixValeur[i][j] = 0
	return fin

def creerChemin(i, j):
	global soluce1
	global soluce2
	soluce1.append("")
	soluce2.append("")
	index = len(soluce1)-1
	determinerChemin(i,j,index)

def determinerChemin(i, j, index):
	# print("i-1: ",i-1)
	# print("j-1: ",j-1)
	global seq1
	global seq2
	global soluce1
	global soluce2
	nb = 0
	if matrixFleche[i][j][2] == True: #diag
		nb+=1
	if matrixFleche[i][j][0] == True: #haut
		nb+=1
	if matrixFleche[i][j][1] == True: #gauche
		nb+=1

	if nb == 1:
		if matrixFleche[i][j][2] == True: #diag
			soluce1[index] += seq1[j-1]
			soluce2[index] += seq2[i-1]
			determinerChemin(i-1, j-1, index)
		elif matrixFleche[i][j][0] == True: #haut
			soluce1[index] += "-"
			soluce2[index] += seq2[i-1]
			determinerChemin(i-1, j, index)
		elif matrixFleche[i][j][1] == True: #gauche
			soluce1[index] += seq1[j-1]
			soluce2[index] += "-"
			determinerChemin(i, j-1, index)
	elif nb == 2:
		if matrixFleche[i][j][2] == True and matrixFleche[i][j][0] == True: #diag && #haut
			temp1 = soluce1[-1]
			temp2 = soluce2[-1]
			
			soluce1[index] += seq1[j-1]
			soluce2[index] += seq2[i-1]
			determinerChemin(i-1, j-1, index)

			soluce1.append(temp1)
			soluce2.append(temp2)
			index2 = len(soluce1)-1
			
			soluce1[index2] += "-"
			soluce2[index2] += seq2[i-1]
			determinerChemin(i-1, j, index2)

		elif matrixFleche[i][j][0] == True and matrixFleche[i][j][1] == True: #haut && gauche
			temp1 = soluce1[-1]
			temp2 = soluce2[-1]
			
			soluce1[index] += "-"
			soluce2[index] += seq2[i-1]
			determinerChemin(i-1, j, index)

			soluce1.append(temp1)
			soluce2.append(temp2)
			index2 = len(soluce1)-1
			
			soluce1[index2] += seq1[j-1]
			soluce2[index2] += "-"
			determinerChemin(i, j-1, index2)

		elif matrixFleche[i][j][1] == True and matrixFleche[i][j][2] == True: #gauche && #diag
			temp1 = soluce1[-1]
			temp2 = soluce2[-1]
			
			soluce1[index] += seq1[j-1]
			soluce2[index] += "-"
			determinerChemin(i, j-1, index)

			soluce1.append(temp1)
			soluce2.append(temp2)
			index2 = len(soluce1)-1
			
			soluce1[index2] += seq1[j-1]
			soluce2[index2] += seq2[i-1]
			determinerChemin(i-1, j-1, index2)

	elif nb == 3:
		temp1 = soluce1[-1]
		temp2 = soluce2[-1]

		soluce1[index] += seq2[i-1]
		soluce2[index] += seq1[j-1]
		determinerChemin(i-1, j-1, index)

		soluce1.append(temp1)
		soluce2.append(temp2)
		index2 = len(soluce1)-1
		
		soluce1[index2] += seq1[j-1]
		soluce2[index2] += "-"
		determinerChemin(i, j-1, index2)

		soluce1.append(temp1)
		soluce2.append(temp2)
		index3 = len(soluce1)-1
		
		soluce1[index3] += "-"
		soluce2[index3] += seq2[i-1]
		determinerChemin(i-1, j, index3)
		



mode = "global"

seq1 = "ACGTACG" #horizonal
seq2 = "CACGTAT" #vertical

seq1 = input("Entrez la premiere sequence: (attention seulement ACGT)")
print(seq1)
seq2 = input("Entrez la premiere sequence: (attention seulement ACGT)")

gap = -1
matrixChangement = [[1,0,0,0], #ACGT
                [0,1,0,0], #C
                [0,0,1,0], #G
                [0,0,0,1]] #T

matrixValeur = []
for i in range(len(seq2)+1):
	matrixValeur.append([])
	for j in range(len(seq1)+1):
		matrixValeur[i].append(None)

# print("matrixValeur: ",matrixValeur)


matrixFleche = []
for i in range(len(seq2)+1):
	matrixFleche.append([])
	for j in range(len(seq1)+1):
		matrixFleche[i].append([])
		for k in range(3):
			matrixFleche[i][j].append(False) #haut, gauche, diag

# print("matrixFleche: ",matrixFleche)

soluce1 = []
soluce2 = []

valMax = -1

iteration = 0

while fillMatrix(iteration, mode) == False:
	#PRINT MATRIX VALEUR
	for lig in matrixValeur:
		string = ""
		for col in lig:
			string += str(col)+"\t"
		print(string)
	#FIN PRINT MATRIX VALEUR
	#val = input("press a key to continue!")
	iteration+=1


#PRINT MATRIX VALEUR
# for lig in matrixValeur:
# 	string = ""
# 	for col in lig:
# 		string += str(col)+"\t"
# 	print(string)

#print("matrixFleche: ",matrixFleche)

if mode == "global":
	creerChemin(len(matrixValeur)-1, len(matrixValeur[len(matrixValeur)-1])-1)
elif mode == "local":
	listCooMax = []
	for i in range(len(matrixValeur)):
		for j in range(len(matrixValeur[i])):
			if matrixValeur[i][j] > valMax:
				listCooMax.clear()
				valMax = matrixValeur[i][j]
				listCooMax.append((i,j))
			elif matrixValeur[i][j] == valMax:
				listCooMax.append((i,j))
	for x in range(len(listCooMax)):
		creerChemin(listCooMax[x][0], listCooMax[x][1])


reverseAll()

if mode == "global":
	print("solutions globales avec un score de",matrixValeur[-1][-1],":")
	print(soluce1)
	print(soluce2)
elif mode == "local":
	print("solutions locales avec un score de",valMax,":")
	print(soluce1)
	print(soluce2)
