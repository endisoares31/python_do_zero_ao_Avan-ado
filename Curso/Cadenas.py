texto = "Benvindos a Localidade de Fajã"
print(texto)
print(texto.upper())
print(texto.lower())
print(texto.title())

print(texto.find("Loc"))
print(texto.count("e"))
print(texto.count('F'))
textoFinal = texto.replace("a","3")
print(textoFinal)

valor = texto.isnumeric()
print(valor)

caracteresSeparadas = texto.split(" ")
print(caracteresSeparadas)