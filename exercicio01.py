# Par ou Ímpar

# Peça ao usuário um número. 
# Retorne a ele se o número é par ou impar.


num = input("Digite um número: ")
num = int(num)

resultado = num % 2

if resultado == 0:
    print("O número digitado é par!")
else:
    print("O número digitado é impar!")