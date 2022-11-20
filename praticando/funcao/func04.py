def maior(* num):
    cont = maior = 0
    print('\nAnalisanod os vlaores passados')
    for i in num:
        print(f'{i} ', end='')
        if cont == 0:
            maior = i
        else:
            if i > maior:
                maior = i
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)