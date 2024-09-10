resultado = 0
n1 = int(input("Digite o primeiro número...\n"))
n2 = int(input("Digite o segundo número...\n"))
operacao = str(input("Digite a operação: (+, -, *, /)")).strip()

if operacao == "+":
    resultado = n1 + n2
elif operacao == "-":
    resultado = n1 - n2
elif operacao == "*":
    resultado = n1 * n2
elif operacao == "/":
    if n2 == 0:
        resultado = str("Não é pocível dividir nenhum número por zero.")
    else:
        resultado = n1 / n2
else:
    resultado = str("Operação inválida.")

print(n1, operacao, n2, "=", resultado)
