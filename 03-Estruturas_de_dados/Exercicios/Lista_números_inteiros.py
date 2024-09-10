numeros = []

while True:
    n = int(input("Digite um número inteiro positivo para ser adicionado a lista\nDigite um número inteiro negativo para parar de adicionar números.\n"))
    if n < 0:
        break
    else:
        numeros.append(n)    
print("Sua lista ficou assim:\n", numeros)
