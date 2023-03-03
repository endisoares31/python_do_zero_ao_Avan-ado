# Funcoes: é um conjunto de instruções que realizam processos
# A Principal vantagem é que nos ajuda a evitar códigos repetidos

def comprimentar():
    print("Endi")
    print("Soares")
    print("Fajã de Baixo")
    return "Ola"

print(comprimentar())



def evolucaosaldominimo(saldo):
    if saldo >= 850:
        print("Podes comprar com o Saldo")
    else:
        print("Estás no limite do Saldo minímo")
evolucaosaldominimo(100) 


