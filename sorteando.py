from random import choice
nome1 = input("Digite um nome para o sorteio ")
nome2 = input("Digite outro nome para o sorteio ")
nome3 = input("Digite outro nome para o sorteio ")

lista = [nome1, nome2, nome3]
sorteio = choice(lista)

print("Quem ganhou o sorteio foi {}".format(sorteio))