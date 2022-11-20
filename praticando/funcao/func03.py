from time import sleep
def contador(i, f, p):
    print('-=' * 20)
    print(f'contagem de {i} ate o {f} de {p} em {p}')
    sleep(3.0)

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p

    print('FIM')

contador(1, 10, 1)
contador(10, 0, 1)
print('Agora é  sua vez de personalizar a contagem.')
ini = int(input('Ínicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)