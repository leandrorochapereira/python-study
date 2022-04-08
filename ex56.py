#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho 
#e quantas mulheres têm menos de 20 anos.

somaIdade = 0 #para calcular a media das idades e ver qual a maior idade, pra depois ver
#o nome do homem mais velho, tenho que achar a soma das idades
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulher20 = 0

for p in range(1,4): #o que estiver no for vai acontecer o tanto de vezes que eu pedir
    print('----- {}ª PESSOA ----- '.format(p))
    nome = str(input('Insira o nome da {} pessoa: '.format(p))).strip()#tirar os espaços é importante para ler uma frase
    idade = int(input('Insira a idade: '))
    sexo = str(input('Escolha o sexo:\n[ M ] ou [ F ]: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm': #se a maior idade e o sexo for M ou m
        maiorIdadeHomem = idade
        nomeVelho = nome
        #se a idade for a mais alta, a variavel nomeVelho recebe a variavel nome 
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    #mesma lógica do exercício 55 onde tínhamos que gravar as idades e colocar a maior idade
    #na variável escolhida
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1
    #se na variavel sexo tivermos a opção F ou f e a idade for menor que 20
    #a variavel totMulher recebe +1 

mediaIdade = somaIdade / 4
print('A média de idade do grupo é {:.0f} anos.'.format(mediaIdade))
print('O homem mais velho é {} e tem {}. '.format(nomeVelho, maiorIdadeHomem))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totMulher20))
