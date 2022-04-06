#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

ano = int(input('Insira o seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - ano
print('Quem nasceu em {}, tem {} anos em {}'.format(ano, idade, anoAtual))


if idade > 18:
    print('Você \033[1;32mjá se alistou\033[0m em \033[1m{}\033[0m.'.format(ano+18))
elif idade == 18:
    print('Você faz \033[1;31m18 anos\033[0m este ano e \033[1;31mDEVE\033[0m se alistar \033[1;31mIMEDIATAMENTE.\033[0m')
else:
    print('\033[1;32mFalta(m) {} ano(s)\033[0m para você se alistar.'.format(18-idade))
