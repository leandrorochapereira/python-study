#Escreva um programa em Python que leia um número inteiro qualquer e 
# peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Insira um número inteiro: '))
print('''Escolha uma das bases para conversão:
    [ \033[32m1\033[0m ] Converter para \033[31mBINÁRIO\033[0m
    [ \033[32m2\033[0m ] Converter para \033[31mOCTAL\033[0m
    [ \033[32m3\033[0m ] Converter para \033[31mHEXADECIMAL\033[0m''')
opção = int(input('Sua opção: '))

if opção == 1:
    print('\033[32m{}\033[0m convertido para \033[31mBINÁRIO\033[0m é igual a \033[33m{}\033[0m'.format(num, bin(num)[2:]))
elif opção == 2:
    print('\033[32m{}\033[0m convertido para \033[31mOCTAL\033[0m é igual a \033[33m{}\033[0m'.format(num, oct(num)[2:]))
elif opção == 3:
    print('\033[32m{}\033[0m convertido para \033[31mHEXADECIMAL\033[0m é igual a \033[33m{}\033[0m'.format(num, hex(num)[2:]))
else:
    print('Opção inválida.')