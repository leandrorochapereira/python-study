#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 
# para viagens mais longas.

kms = float(input('Insira a quilometragem de sua viagem: '))
if kms <= 200:
    print('Sua passagem custa: R${:.2f}' .format(kms*0.5))
else:
    print('Sua passagem custa: R${:.2f}'.format(kms*0.45))