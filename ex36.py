# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos deseja pagar? '))
prestacao = casa / (anos * 12)

if prestacao >= salario * 0.30:
    print('Sua prestação é de R${:.2f}/mensal.'.format(prestacao))
    print('Seu salário é de R${}. Seu empréstimo está \033[31mNEGADO.\033[0m'.format(salario))
else:
    print('Sua prestação é de R${:.2f}/mensal.'.format(prestacao))
    print('Seu salário é de {}. Seu empréstimo está \033[32mAPROVADO.\033[0m'.format(salario))

