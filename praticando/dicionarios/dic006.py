from tkinter.tix import Tree


time = list()
gols_partidas = list()
jogador = dict()
while True:
    jogador.clear()
    jogador = {
        'nome': str(input('Nome do jogador; ')),
        'partidas': int(input('Numero de partidas que ele jogou: ')),
    }
    gols_partidas.clear()
    for g in range(jogador['partidas']):
        gols_partidas.append(int(input(f'Quantos gols ele fez na partida {g}? ')))

    jogador['gols'] = gols_partidas[:]

    jogador['total'] = sum(gols_partidas)
    time.append(jogador.copy())
    while True:
        continuar = input('Deseja continuar? ').upper()[0]
        if continuar != 'S' and continuar != 'N':
            print('ERRO, digite s/sim e n/nao')
        else:
            break
    if continuar == 'N':
        break
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
print('=-' * 30)
while True:
    busca = int(input('Mostar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO - Jogador {busca} não foi cadastrado.')
    else:
        print(f'--Levantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('FIM DO PROGRAMA')