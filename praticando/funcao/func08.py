
def ficha(jog='<desconhecido>', gols=0):
    print(f'O jogador {jog} fez {gols} gols')


nome = str(input("Nome do jogador: "))
g = str(input("N de gols: "))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if nome.strip() == '':
    ficha(gols=g)
else:
    ficha(nome, g)