from datetime import datetime

pessoa = {
    'nome': str(input('Nome: ')),
    'nascimento': int(input('Ano de nascimento: ')),
    'CTPS': float(input('Carteiro de trabalho: ')),
}

pessoa['idade'] = datetime.now().year - pessoa['nascimento']

if pessoa['CTPS'] != 0:
    pessoa['contratacao'] = int(input('Ano de contatação: '))
    pessoa['salario'] = int(input('Salário: '))
    pessoa['aposentadoria'] = pessoa['contratacao'] + 65

print('=' * 30)

for i, f in pessoa.items():
    print(f'{i} -> {f}')