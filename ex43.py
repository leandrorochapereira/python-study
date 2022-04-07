#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Insira o seu peso em Kilos: '))
altura = float(input('Insira usa altura: '))
imc = peso / (altura**2) #altura ao quadrado **

if imc < 18.5:
    print('Seu imc é \033[1;34m{:.1f}\033[0m. Você está \033[1;34mabaixo do peso\033[0m.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu imc é \033[1;32m{:.1f}\033[0m. Você está com o \033[1;32mpeso ideal\033[0m.'.format(imc))
elif 25 <= imc < 30:
    print('Seu imc é \033[1;33m{:.1f}\033[0m. Voce está com \033[1;33msobrepeso\033[0m.'.format(imc))
elif 30 <= imc < 40:
    print('Seu imc é \033[1;31m{:.1f}\033[0m. Você está com \033[1;31mobesidade\033[0m.'.format(imc))
else:
    print('Seu imc é \033[1;35m{:.1f}\033[0m. Você está com \033[1;35mObesidade Mórbida\033[0m.'.format(imc))