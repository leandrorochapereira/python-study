#Estruturas condicionais

nome = str(input('Qual seu nome? '))

if nome == 'Leandro':
    print('{}! Que nome bonito!'.format(nome))
elif nome == 'Pedro' or nome == 'Carlos':
    print('Bom dia {} otário.'.format(nome))
else:
    print('Você de novo {}.'.format(nome))
print('Tenha um bom dia, {}.'.format(nome))
#Podemos ter quantos elif quisermos e else nao é necessário mas só pode 1