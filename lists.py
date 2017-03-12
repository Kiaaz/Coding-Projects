L=[]
B=[]
C=[]
for i in range(100):
	L.append(i**i)
	C+=L

print(len(C))

for j in range(len(C)*1000):
	C.insert(0,j*j)
	# C.append(j*j)

print(C)
