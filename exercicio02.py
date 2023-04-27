# Palíndromos

# Peça uma string qualquer ao usuário e informe a ele se a 
#string é um palíndromo ou não. (um palíndromo é uma string 
#que pode ser lida da mesma forma, da 
#esquerda para a direita ou vice-versa. Ex.: omo).

palavra = input("Digite uma palavra para saber se ela é ou não um palíndromo: ")

palavra_inversa = palavra[::-1]

if palavra == palavra_inversa:
    print("Essa palavra é um palíndromo!")
else:
    print("Essa palavra não é um palíndromo!")
