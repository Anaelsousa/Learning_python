numeros = []
soma = 0

while True:
    n = int(input("Digite um número para ser adicionado a lista. Digite 999 para parar.\n"))
    if n == 999:
        break
    else:
        numeros.append(n)
        soma += n

media = soma // len(numeros)

print(f"Sua lista ficou assim:\n{numeros}")
print(f"A soma de todos esses números é igual a {soma}")
print(f"A média dos números dessa lista é igual a {media}")

print(f"O maior número da llista é o {max(numeros)}.")
print(f"O menor número da lista é o {min(numeros)}.")
