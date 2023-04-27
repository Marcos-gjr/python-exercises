# Jogo da adivinhação

# Gere um número aleatório entre 1 e 9 (incluindo 1 e 9). 
# Peça ao usuário para adivinhar o número, e então diga se 
#a tentativa foi menor, maior ou correta. 
# (Dica: lembre-se de usar o input dos exercícios anteriores). 
# Mantenha o jogo executando até que o usuário digite "sair".

import random


numero = random.randint(1, 9)

while True:    
    tentativa = input("Tente adivinhar o número entre 1 e 9 ou digite 'sair' para finalizar o programa: ")
    
    if tentativa.lower() == "sair":
        break
    elif int(tentativa) == numero:
        print("Parabéns, você acertou!")
        numero = random.randint(1, 9)    
    elif int(tentativa) > numero:
        print("O número é menor que", tentativa)
    else:
        print("O número é maior que", tentativa)