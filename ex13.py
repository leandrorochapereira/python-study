#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, 
# com 15% de aumento.

sal = float(input('Insira o seu salário R$'))
nsal = sal + (sal * 15 / 100)

print('O seu salário com reajuste de 15% será de R${:.2f}'.format(nsal))
