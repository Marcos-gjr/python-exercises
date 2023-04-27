# Pedra, Papel, Tesoura

# Faça um jogo de pedra, papel ou tesoura de dois jogadores.
# (Dica: peça as jogadas ao usuário - usando input
#- compare-os, imprima uma mensagem parabenizando o 
#vencedor e pergunte ao usuário se quer continuar jogando).



player1 = ""
player2 = ""

while True:

    while player1.lower() not in ["tesoura", "pedra", "papel"]:   
        player1 = input("E então, jogador um, você escolhe pedra, papel ou tesoura?")
        if player1.lower() not in ["tesoura", "pedra", "papel"]:
            print("Essa opção não existe, escolha uma opção válida")

    while player2.lower() not in ["tesoura", "pedra", "papel"]:
        player2 = input("E então, jogador dois, você escolhe pedra, papel ou tesoura?")
        if player2.lower() not in ["tesoura", "pedra", "papel"]:
            print("Essa opção não existe, escolha uma opção válida")

    if player1 == player2:
        print("E o resultado foi um tenso empate!!")
    elif player1 == "pedra" and player2 == "tesoura":
        print("Jogador 1 venceu!")
    elif player1 == "tesoura" and player2 == "papel":
        print("Jogador 1 venceu!")
    elif player1 == "papel" and player2 == "pedra":
        print("Jogador 1 venceu!")
    else:
        print("Jogador 2 venceu!")
    player1 = ""
    player2 = ""
    if input("Deseja jogar novamente? (s/n)").lower() == "n":
        break
    
    