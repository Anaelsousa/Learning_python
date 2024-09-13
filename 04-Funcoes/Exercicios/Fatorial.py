def fatorial(n):
    resutado = 1
    for v in range(n, 0, -1):
        resutado *= v
    return resutado

num = int(input("Digite um número inteiro positivo para ver o seu fatorial.\n"))
fat = fatorial(num)
print(f"O fatorial de {num} é {fat}.")
