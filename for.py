#estudando a estrutura de repetição for em python

'''
contando de 0 a 6
for c in range(0,6):
    print(c)
print('Fim')

contando de 6 a 0
for c in range(6, 0 ,-1):
    print(c)
print('Fim')

contando de 0 a 6 pulando de 2 em 2
for c in range(0, 7, 2):
    print(c)
print('Fim')

somando valores inseridos pelo comando
'''
s = 0
for c in range(0,3):
    n = int(input('Digite um valor: '))
    s += n
print('A soma dos valores é {}'.format(s))