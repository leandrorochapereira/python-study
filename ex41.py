#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento 
# de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR

from datetime import date
idade = int(input('Insira o ano de nascimento do atleta: '))
categoria = date.today().year - idade

if categoria >= 15 and categoria <= 19:
    print('O atleta tem {} anos. Ele deverá estar na categoria JÚNIOR'.format(categoria))
elif categoria >= 10 and categoria < 15:
    print('O atleta tem {} anos. Ele deverá estar na categoria INFANTIL'.format(categoria))
elif categoria <= 9:
    print('O atleta tem {} anos. Ele deverá estar na categoria MIRIM.'.format(categoria))
elif categoria > 20 and categoria <= 25:
    print('O atleta tem {} anos. Ele deverá estar na catergoria SÊNIOR.'.format(categoria))
else:
    print('O atleta tem {} anos. Ele deverá estar na categoria MASTER.'.format(categoria))