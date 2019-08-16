import random

cpu = random.randint(1, 10)
print("Tente adivinhar o numero q a cpu escolheu")
print("-"*30)
jogador = int(input("Escolha um numero: "))

print("-"*30)
if cpu == jogador:
    print("Acertou, a cpu escolheu o numero {}".format(cpu))
else:
    print("Errou, a cpu escolheu o numero {}".format(cpu))