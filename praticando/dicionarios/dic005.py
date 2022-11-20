galera = list()
soma = media = 0
while True:
    pessoa = {
        'nome': str(input('Nome: ')),
        'idade': int(input('Idade: ')),
    }
    soma += pessoa['idade']
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).upper()[0]
        if pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':
            print('Sexo invalido, tente novamente')
        else:
            break
    galera.append(pessoa.copy())
    while True:
        continuar = str(input('deseja continuar? ')).upper()[0]
        if continuar != 'N' and continuar != 'S':
            print('ERRO: Digite apenas S/sim ou N/não')
        else:
            break
    if continuar == 'N':
            break

print('=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'Amédia de idade é de {media:5.2f} anos')
print('As mulheres cadastradas foram: ')
for i in galera:
    if i['sexo'] == 'F':
        print(f'-->{i["nome"]}')
print('lista de pessoas que estão acima da media: ')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('>>>>FIM<<<<<')
        

