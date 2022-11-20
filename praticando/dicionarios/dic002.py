from operator import itemgetter
from random import randint

jogo = {
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)
}

print('Valores Sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')

ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, f in enumerate(ranking):
    print(f'{i} lugar {f[0]} com {f[1]} ')