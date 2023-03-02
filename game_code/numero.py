print('==================== SEJA BEM-VINDO =======================')

print('\n')

from random import randint

n_escolhido = int(input('Chute um número: '))

sorteio = randint(0, 7)

if n_escolhido == sorteio:
    print('Parabéns, Você venceu!!!')
    
else:
    print('Errado!!! \nNúmero que pensei foi {}!'.format(sorteio))
    
print('\n')
print('==================== OBRIGADO POR JOGAR ====================')
    
    
    