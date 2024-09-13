def primo(n):
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for primo in primos:
        if n % primo == 0:
            p = False
            break
    if primo == 47 or n in primos:
        p = True
    return p

num = int(input("Digite um número inteiro entre 0 e 2500 para verificar se ele é primo.\n"))
print(primo(num))
