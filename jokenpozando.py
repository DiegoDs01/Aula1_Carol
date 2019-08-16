from random import randint 
#Importando da biblioteca random o randint que randomiza numeros inteiros
from time import sleep 
#Importando da biblioteca time o modulo sleep, que permite um intervalo de tempo de uma ação

print("0 = Pedra")
print("1 = Papel")
print("2 = Tesoura")
print ('-'*30)

opcoes = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0, 2)
jogador = int(input("Escolha sua jogada: "))

print('JO')
sleep(1)             #Sleep importado da biblioteca time
print('KEN')
sleep(1)
print('PO')

print('-'*30)
print('A maquina jogou {} '.format(opcoes[cpu])) #Variavel opcoes na posição cpu, para ao invés de mostrar os numeros, mostrar o quem contem nas posicoes escolhidas
print('Voce jogou {} '.format(opcoes[jogador]))
print('-'*30)

# -------------------------- Função if dentro de outros ifs e de elifs também ---------------------------------------------#
if cpu == 0:
    if jogador == 0:
        print('Empatou')
    elif jogador == 1:
        print('Voce ganhou')
    elif jogador == 2:
        print('Voce perdeu')    
    else:
        print("Escolhe uma opcao valida ai")
elif cpu == 1:
    if jogador == 0:
        print('Voce perdeu')
    elif jogador == 1:
        print('Empatou')
    elif jogador == 2:
        print('Voce ganhou')
    else:
        print('Escolhe uma opcao valida ai')
elif cpu == 2:
    if jogador == 0:
        print('Voce ganhou')
    elif jogador == 1:
        print('Voce perdeu')
    elif jogador == 2:
        print('Empatou')
    else:
        print('Escolhe uma opcao valida ai')