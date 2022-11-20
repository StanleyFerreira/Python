aluno = {
    'nome': str(input('Digite o nome do aluno: ')),
    'media': float(input('Qual a média do aluno: ')),
}
if aluno['media'] <= 6:
    aluno['situacao'] = str('Reprovado')
else:
    aluno['situacao'] = str('Aprovado')
print(aluno['situacao'])

print(f'O aluno {aluno["nome"]} teve uma media {aluno["media"]} e esta {aluno["situacao"]}')