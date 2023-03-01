from random import randint
from random import shuffle

n_escolhido = int(input('Chute um número: '))

sorteio = randint(0, 13)

if n_escolhido == sorteio:
    print('Parábens!')
else:
    shuffle_1 = print('Eitaaa, que azar hein ?! \nNúmero Escolhido: {} \n Número Sorteado: {}')
    shuffle_2 = print('Deu ruim parceiro, TRY AGAIN !!!',sorteio)
    shuffle_3 = print('Eitaaa, que azar hein ?! Seu número é ',sorteio)
    shuffle_4 = print('Eitaaa, que azar hein ?! Seu número é ',sorteio)
    shuffle_5 = print('Eitaaa, que azar hein ?! Seu número é ',sorteio)