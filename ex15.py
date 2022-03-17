# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kms = float(input('Insira o total de Kms percorridos: '))
dias = int(input('Insira o total de dias que o veículo foi alugado: '))

preçoKm = kms * 0.15
preçoDia = dias * 60
preçoTotal = preçoDia + preçoKm

print('O valor por Kilometros é R${:.2f}.\nO valor por dias é R${:.2f}.\nO valor total é de : R${}'.format(
    preçoKm, preçoDia, preçoTotal))
