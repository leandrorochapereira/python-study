#Faça um programa que leia o sexo de uma pessoa, 
#mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente 
#até ter um valor correto.
'''
sexo = 'Mm','Ff'

while sexo != 'Mm' and 'Ff':
    sexo = str(input('Insira o seu sexo [M] / [F]: '))
    if sexo != 'Mm' and 'Ff':
        print('Escolha novamente.')
print('Obrigado')
''' 


sexo = str(input('Informe seu sexo: [M] or [F]   ')).strip().upper()[0] #tirando os espaços, deixando tudo em maiúsculo e pedindo só a 1a letra
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Digite novamente: ')).strip().upper()[0] #pedindo novamente a inserção de dados
print('Sexo {} registrado com sucesso'.format(sexo))