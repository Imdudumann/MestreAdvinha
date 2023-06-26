from random import randint

print('JOGO MESTRE DA ADVINHAÇÃO')
name = input('Digite seu nome: ')
print(f'Olá {name}, você devera tentar advinhar o número de 1 a 10'
      f', Você terá 10 tentativas!')
aleatorio = randint(1,11)
numero_tentativas = 0
while numero_tentativas <10:
    meu_palpite = int(input('Digite sua tentativa: '))
    if meu_palpite == aleatorio:
        print(f'Parabés você ganhou!')
        break
    elif meu_palpite > aleatorio:
        print(f'O número é menor!')
    elif meu_palpite < aleatorio:
        print(f'O número é maior')
    numero_tentativas+=1
else:
    if numero_tentativas ==10:
        print(f'infelizmente suas tentativas acabaram')