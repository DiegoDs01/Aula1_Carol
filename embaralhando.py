from random import shuffle

nome1 = input("Primeira pessoa ")
nome2 = input("Segunda pessoa ")
nome3 = input("Terceira pessoa ")
nome4 = input("Quarta pessoa ")

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print(lista)