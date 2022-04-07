#Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

valor = float(input('Insira o valor do produto R$'))
print('''SELECIONE A FORMA DE PAGAMENTO:
    [ 1 ] À Vista em dinheiro/pix
    [ 2 ] À Vista no cartão
    [ 3 ] 2x no cartão de crédito
    [ 4 ] 3x ou mais no crédito\n''')
pagamento = int(input('Opção: '))

if pagamento == 1:
    desconto = valor - (valor * 0.10) 
    print('Sua compra no valor de R${:.2f} ficou por R${:.2f}!'.format(valor, desconto))
elif pagamento == 2:
    desconto = valor - (valor * 0.05)
    print('Sua compra no valor de R${:.2f} ficou por R${:.2f}!'.format(valor, desconto))
elif pagamento == 3:
    print('Sua compra no valor de R${:.2f} irá custar R${:.2f} por mês.'.format(valor, valor/2))
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas deseja pagar? '))
    desconto = valor + (valor * 0.20)
    valor = desconto / parcelas
    print('Sua compra no valor de R${:.2f} irá custar R${:.2f} em {}x!'.format(desconto, valor, parcelas))
else:
    print('\033[1;31mFORMA DE PAGAMENTO INVÁLIDA.\033[0m\nSelecione novamente uma forma e pagamento.')

