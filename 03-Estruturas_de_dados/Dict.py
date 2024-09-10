alunos = {"Alice":6, "Diego":8, "Taís":7, "Erica":5, "Yasmin":9}

for k, v in alunos.items():
    print(k,v)

print("Alunos:")
for aluno in alunos.keys():
    print(aluno)

print("Notas:")
for nota in alunos.values():
    print(nota)
