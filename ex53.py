#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
#desconsiderando os espaços. Exemplos de palíndromos:

frase = str(input('Digite uma frase: ')).strip().upper() #Strip pra cortar os espaços e upper para não ter erro entre minuscula e maiuscula
palavras = frase.split()#separando a frase em palavras em uma lista
junto = ''.join(palavras)#juntando a frase pra eliminar os espaços
#inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('\033[1;34mTemos um PALÍNDROMO\033[0m')
else:
    print('Não temos um palíndromo.')
'''print('Você digitou a frase: \n\033[34m{}\033[0m'.format(palavras))'''