#introdução sobre a estrutura de repetição while

c = 1 #c é igual a 1
#enquanto c for diferente de 11, printe c aumentando 1 a cada print
'''while c != 6:
    print(c)
    c += 1
print('End')'''
#quando acabar o lasso print end

#com while podemos fazer uma repetição até encerrarmos manualmente
#quando não sabemos quando vamos encerrar
#diferente do for que sabemos o encerramento/quantidade de leitura

n = 1
par = impar = 0
while n != 0:
    n = int(input('Insira um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você inseriu {} números pares e {} números impares'.format(par, impar))