from random import randint
escolhas = ('Pedra', 'Papel', 'Tesoura')
com = randint(0,2)
print(
    '[0] Pedra\n'
    '[1] Papel\n'
    '[2] Tesoura\n'
)
jogada = int(input("Digite sua escolha: "))
print("O computador escolheu {}".format(escolhas[com]))
print("Você jogou {}".format(escolhas[jogada]))
if jogada == com:
    jogada = int(input("Empate, tente denovo: "))
if com == 0:
    if jogada == 1:
        print("Parabens, Você ganhou")
    if jogada == 2:
        print("Você perdeu")
elif com == 1:
    if jogada == 2:
        print("Parabens, Você ganhou")
    if jogada == 0:
        print("Você Perdeu")
elif com == 2:
    if jogada == 0:
        print("Parabens, Você ganhou")
    if jogada == 1:
        print("Você Perdeu")
else:
    print("Jogada invalida, escolha um dos valores representantes de Pedra, Papel ou Tesoura")