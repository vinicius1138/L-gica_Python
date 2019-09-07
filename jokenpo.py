import random

vitorias = 0
aux = 1 
while aux <= 5:

    jogadaPlayer = input("SUA JOGADA:")
    jogadaComputador = random.randrange(0,2)

    jogadas = ["pedra", "papel", "tesoura"]

    print("Player:", jogadaPlayer)
    print("Computador:", jogadas[jogadaComputador])

    if jogadaPlayer == jogadas[jogadaComputador]:
        print("Empate")

    if jogadaPlayer == "pedra" and jogadas[jogadaComputador] == "tesoura":
        print("Player venceu")
        vitorias += 1
    if jogadaPlayer == "papel" and jogadas[jogadaComputador] == "pedra":
        print("Player venceu")
        vitorias += 1
    if jogadaPlayer == "tesoura" and jogadas[jogadaComputador] == "papel":
        print("Player venceu")
        vitorias += 1

    if jogadaPlayer == "tesoura" and jogadas[jogadaComputador] == "pedra":
        print("Computador venceu")
    if jogadaPlayer == "pedra" and jogadas[jogadaComputador] == "papel":
        print("Computador venceu")
    if jogadaPlayer == "papel" and jogadas[jogadaComputador] == "tesoura":
        print("Computador venceu")

    aux += 1
    
if(vitorias >= 3):
    print("Player venceu!!!")
else:
    print("Computador venceu!!!")
