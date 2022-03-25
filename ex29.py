#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Insira a velocidade em Km: '))
if velocidade > 80:
    multa = (velocidade - 80)* 7
    print('MULTADO! Você excedeu o limite de velocidade.')
    print('Sua multa é de: R${:.2f}'.format(multa))
print('Tenha um bom dia, dirija com segurança.')