alunos = [{"nome": "Alice", "nota": 8}, {"nome": "Bob", "nota": 7}, {"nome": "Carlos", "nota": 9,}]
soma_notas = 0

for aluno in alunos:
    print(aluno["nome"], aluno["nota"])
    soma_notas += aluno["nota"]

media_alunos = soma_notas // len(alunos)

print(f"A média das notas de todos os alunos é igual a {media_alunos}")
