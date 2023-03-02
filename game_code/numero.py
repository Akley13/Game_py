print('==================== SEJA BEM-VINDO ====================')

print('\n')

from random import randint

n_escolhido = int(input('Chute um número: '))

sorteio = randint(0, 7)

while n_escolhido != sorteio:
    print('Que pena, tente de novo!')

print('==================== OBRIGADO POR JOGAR ====================')
    
    
    