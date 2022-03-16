#Faça um programa que leia a largura e a altura de uma parede em metros, 
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

lar = float(input('Insira a largura da parede em metros: '))
alt = float(input('Insira a altura da parede em metros: '))

print('O total de área é de {:.2f}m². Você precisará de {:.2f}lts de tinta para pintá-la.' .format(lar * alt, (lar * alt) / 2))