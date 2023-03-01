from random import randint

n_escolhido = int(input('Chute um número: '))

sorteio = randint(0, 13)

if n_escolhido == sorteio:
    print('Parábens!')
    