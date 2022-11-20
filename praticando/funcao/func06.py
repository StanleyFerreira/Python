


def voto(nasc):
    idade = 2022 - nasc
    if idade < 16:
        print('Você e  muito novo para votar')
    elif idade < 18:
        print('Você já tem idade para votar, se quiser.')
    else:
        print('Você é obrigado a votar')


nascimento = int(input('digte seu ano de nascimento'))

voto(nascimento)