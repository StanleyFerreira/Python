jogador = {
    'nome': str(input('Nome do jogador; ')),
    'partidas-jogadas': int(input('Numero de partidas que ele jogou: ')),
}

gols_partidas = list()

for g in range(jogador['partidas-jogadas']):
    gols_partidas.append(int(input(f'Quantos gols ele fez na partida {g}? ')))

jogador['gols'] = gols_partidas[:]

jogador['total'] = sum(gols_partidas)

print(f'''
O jogador {jogador["nome"]}
 fez {jogador["total"]} gols em {jogador["partidas-jogadas"]} partidas jogadas.''')

for i, f in enumerate(jogador['gols']):
    print(f'Na {i} ele fez {f} gols')
