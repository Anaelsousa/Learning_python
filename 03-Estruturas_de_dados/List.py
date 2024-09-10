list = []
count = 0

for c in range(0, 5):
    list.append(input("Digite alguma coisa para adicionar na lista.\n"))

for i in list:
    count += 1
    print(f"{count}° item: {i}")

list.sort(reverse=True)
for i in list:
    print(i)

utimo_item = list.pop()
print(f"Apagamos o item {utimo_item} da lista.")

list.insert(0, input("Digite um valor para ser adicionado no primeiro indice da lista.\n"))
print(list)

indice = int(input("Digite um indice para ver o item da lista.\n"))
print(list[indice])
