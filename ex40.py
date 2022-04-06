#Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, 
# de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota1 = float(input('Insira sua 1ª nota: '))
nota2 = float(input('Insira sua 2ª nota: '))
media = (nota1 + nota2) / 2
print('Sua 1ª nota é: {:.1f}, sua 2ª nota é: {:.1f} e sua média é: {:.1f}'.format(nota1, nota2, media))

if media >= 7:
    print('Sua média é: \033[1;32m{:.1f}\033[0m.\nVocê está \033[1;32mAPROVADO\033[0m'.format(media))
elif media >=5 and media <= 6.9:
    print('Sua média é: \033[1;33m{:.1f}\033[0m.\nVocê está em \033[1;33mRECUPERAÇÃO\033[0m.'.format(media))
else:
    print('Sua média é: \033[1;31m{:.1f}\033[0m.\nVocê está \033[1;31mREPROVADO\033[0m.'.format(media))