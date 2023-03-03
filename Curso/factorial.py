# Factorial é o produto de todos os numeros positivos inteiros compreendidos entre 1 e um determinado numero
#Factorial de 5 1*2*3*4*5 = 120
#Factorial de 4 1*2*3*4

numero = int(input("Insira um numero:"))
factorial = 1
for n in range(1, (numero+1)):
    factorial = factorial * n
print("O factorial de {0} é: {1}".format(numero, factorial))



