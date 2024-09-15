# Teste inicial e criação de classes. Agora adicionando atributos de classe para faser uma contagem. Sujeito a alterações no futuro, conforme o aprendizado de novas funcionalidades por parte do autor.

class Conta:
    total_contas = 0
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        Conta.total_contas += 1

    def extrato(self):
        print(f"Número: {self.numero}\nNome do Titular: {self.titular}\nSaldo: {self.saldo}")

    def deposita(self, valor):
        print(f"Depositando {valor}")
        self.saldo += valor

    def saca(self, valor):
        if valor <= self.saldo:
            print(f"Sacando {valor}")
            self.saldo -= valor
        else:
            print("Saldo inssuficiente.")

    def transfere(self, destino, valor):
        if valor <= self.saldo:
            print(f"Transferindo {valor} para {destino.titular}.")
            self.saldo -= valor
            destino.saldo += valor
        else:
            print("Saldo inssuficiente.")

    @classmethod
    def get_total_contas(cls):
        print(f"Até o momento foram criadas {cls.total_contas} contas.")

conta1 = Conta(12345,"Anael de Sousa Oliveira", 1000.00)
conta2 = Conta(12346, "Aysla Brenda de Sousa Oliveira", 0.00)
conta1.transfere(conta2, 200)
conta1.extrato()
conta2.extrato()

Conta.get_total_contas()