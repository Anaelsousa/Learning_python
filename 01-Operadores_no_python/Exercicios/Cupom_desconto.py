valor_compra = float(input("Digite o valor da compra...\n"))
valor_frete = float(input("Digite o valor do frete...\n"))
cliente_cadastrado = str(input("Você é cadastrado no programa de fidelidade? (S/N)\n")).upper()

desconto = ((valor_compra + valor_frete) >= 100) or cliente_cadastrado == "S"

print("Você tem cupom de desconto?", desconto)
