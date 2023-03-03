print("--- Cursos ---")
print("Matemática - Biologia - Linguagem - Ciencias")
cursos = input("Insira o curso desejado: ")

if cursos in ("Matemática", "Biologia", "Linguagem", "Ciencias"):
    print("Curso {0} selecionado.".format(cursos))
else:
    print("Não existe esse curso")