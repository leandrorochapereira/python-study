#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%. 
#Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Insira seu salário em: R$'))

if salario > 1250.00:
    print('Seu aumento é de 10%. Seu salário é: R${:.2f}'.format((salario*0.10)+salario))
else:
    print('Seu aumento é de 15%. Seu novo salário é de: R${:.2f}'.format((salario*0.15)+salario))