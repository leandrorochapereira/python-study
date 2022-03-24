#Faça um programa que leia o nome completo de uma pessoa,
#  mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Insira seu nome: ')).strip()
nome = n.split()
#transformamos o nome em lista e pedimos o numero 0 da lista e o ultimo numero da lista
print('Seu primeiro nome é {}.' .format(nome[0]))
print('Seu ultimo nome é {}.' .format(nome[len(nome)-1]))