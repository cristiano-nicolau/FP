import random

"""
Um vagão é uma lista [mercadoria, quant] com 0<quant<=60 toneladas.
Um comboio é uma lista de vagões.
"""

# Capacidade máxima dos vagões:
Qmax = 60

# Constantes para indexar os vagões.
# Se w==['coal', 45], então w[M]=='coal' e w[Q]==45.
M,Q = 0,1

# Esta função cria um comboio aleatório (NÃO PRECISA PERCEBER).
def randomTrain(a, b=0):
	types = ["coal", "iron", "sand", "salt", "sugar", "rice"]
	n = a if a>b else random.randint(a, b)
	train = []
	for i in range(n):
		wagon = [random.choice(types), random.randint(1, Qmax)]
		train.append(wagon)
	return train


#a)
def quantityOf(t, m):
	total = 0
	for elem in t:
		if m in elem:
			total += elem[1]
	return total
	

#b)
def unload(t, m, q):
	for elem in t[::-1]:
		if m in elem:
			if elem[1] > q:
				elem[1] -= q
				q = 0
			else:
				q -= elem[1]
				t.remove(elem)
	return 0 if q == 0 else q
	

#c)
def merchandise(t):
    dic={}
    for elem in t:
        dic[elem[0]]=[elem[1]]
    return dic

#d)
def trainsPerMerchandise(trains):
	d = {}
	for train in trains:
		print(train)
		for vagao in trains[train]:
			if vagao[0] not in d:
				d[vagao[0]] = {train}
			else:
				d[vagao[0]].add(train)
	return d
		
	
def main():
	random.seed("abc") # Pode alterar o argumento para obter comboios distintos

	t = [['coal', 30], ['rice', 50], ['iron', 5], ['rice', 42], ['coal', 45]]
	#t = randomTrain(5)  # descomente se quiser gerar outro comboio
	print("t:", t)
	
	print("\na)")
	print(quantityOf(t, 'rice'),    # 92
		  quantityOf(t, 'iron'),    # 5
		  quantityOf(t, 'coal'),    # 75
		  quantityOf(t, 'salt'))    # 0

	print("\nb)")
	q = unload(t, 'rice', 40)
	print("unload(t, 'rice', 40) ->", q)
	print("t:", t)
	q =unload(t, 'coal', 50)
	print("unload(t, 'coal', 50) ->", q)
	print("t:", t)
	q =unload(t, 'iron', 20)
	print("unload(t, 'iron', 20) ->", q)
	print("t:", t)

	print("\nc)")
	print(merchandise(t))
	print("t:", t)

	print("\nd)")
	trains = { tid: randomTrain(1,5) for tid in ['T1', 'T2', 'T3', 'T4'] }
	print("trains:", trains)
	trainsPerM = trainsPerMerchandise(trains)
	print(trainsPerM)

####
main()
