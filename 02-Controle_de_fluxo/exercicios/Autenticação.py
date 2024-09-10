usuario = "anael.sousa"
senha = "anael123"

while True:
    u = str(input("Digite seu nome de usuário:\n"))
    s = str(input("Digite sua senha:\n"))
    if u != usuario and s != senha:
        print("Usuário ou senha incorretos.\nTente novamente.")
    else:
        break

print("Altenticação realizada com sucesso.")
