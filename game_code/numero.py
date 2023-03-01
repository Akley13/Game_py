from random import randint

n_escolhido = int(input('Chute um número: '))

sorteio = randint(0, 13)

if n_escolhido == sorteio:
    print('Parábens!')
else:
    from random import shuffle
    shuffle_1 = print('Eitaaa, que azar hein ?! \nNúmero Escolhido: {} \n Número Sorteado: {}'.format(n_escolhido, sorteio))
    shuffle_2 = print('Deu ruim parceiro KKKK \nNúmero Escolhido: {} \n Número Sorteado: {}'.format(n_escolhido, sorteio))
    shuffle_3 = print('Você é muito Azarado...TRISTE! \nNúmero Escolhido: {} \n Número Sorteado: {}'.format(n_escolhido, sorteio))
    shuffle_4 = print('TRY AGAIN BABY, Bye Bye <3 \nNúmero Escolhido: {} \n Número Sorteado: {}'.format(n_escolhido, sorteio))
    lista = [shuffle_1, shuffle_2,shuffle_3, shuffle_4]
    print(lista)
    
    
    