#Estruturas de dados que nos permitem armazenar distintos valores

#São estruturas dinamicas, podem mutar-se,

lista1= ["oscar", 25, 98, 3, True, "Flavio", 56.3]
print(lista1)
print(lista1[:])
print(lista1[2])
print(lista1[-1])

print(lista1[0:3])
print(lista1[:2])
print(lista1[3:])

lista1.append("Endi Soares")
print(lista1)

lista1.insert(4,"Cabo Verde")
print(lista1)

lista1.extend(["Alexandro", 110, False])
print(lista1)

print(lista1.index("Alexandro"))

lista1.remove("Alexandro")
print(lista1)

lista1.pop()
print(lista1)

print("Cabo Verde" in lista1)
