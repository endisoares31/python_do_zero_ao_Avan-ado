# São estruturas de dados que nos permitem armazenzar valores distintos
# Os dados Armanezados estao associados a dodos unicos

miDicionario = {"Espanha": "Madrid", "Dakar":"Senegal","Hollanda":"Roterdam","Cabo Verde":"Praia"}
print(miDicionario["Cabo Verde"])
print(miDicionario)
miDicionario["Portugal"]="Lisboa"
print(miDicionario)

del miDicionario["Espanha"]
print(miDicionario)

dic2 = {"Garcia": "Oscar", 25: True, "Saldo": 150.80}
print(dic2[25])

dados_pessoais = {"Apelidos": "Garcia","Anos": {1:2010, 2:2011, 3:2012, 4:2013, 5:2014}}
print(dados_pessoais["Anos"])

print(dados_pessoais.get('Apelidos',"Garcia"))
valores = tuple(dados_pessoais.values())
print(valores)
