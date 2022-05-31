#Uma equipe da Fórmula 1 deseja calcular o número mínimo de litros que deverá colocar no tanque de um de seus 
# carros para que ele possa percorrer um determinado número de voltas até o primeiro reabastecimento. 
# Escreva um programa (EM QUALQUER LINGUAGEM) que leia o comprimento da pista (em metros), o 
# número total de voltas a serem percorridas no grande prêmio, o número de reabastecimentos desejados e o 
# consumo de combustível do carro (em Km/L). Calcular e escrever o número mínimo de litros necessários para 
# percorrer até o primeiro reabastecimento. Considere que o número de voltas entre os reabastecimentos é o mesmo.
#Faltam saber quantos litros estão no carro

pista = float(input('Insira o tamanho da pista em Metros: '))
consumo = float(input('Insira o consumo do carro por KMs: '))
voltas = int(input('Insira o número de voltas: '))
numReabast = int(input('Insira o numero de vezes que quer reabastecer: '))

totPista = (pista / 1000 ) * voltas
reabastecer = totPista / (numReabast + 1)
numLts = reabastecer / consumo


print(f'Total de Voltas máximas até o próximo reabastecimento é: {numLts:.2f}')


