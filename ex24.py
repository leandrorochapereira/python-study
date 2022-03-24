cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
#funciona apenas com o S maiusculo e sem espaço pré, essa é a falha
#o .strip elimina os finais do começo e do fim
#o .upper transforma tudo o que for escrito em maiusculo, assim mesmo se for em minusculo
#ele vai achar

