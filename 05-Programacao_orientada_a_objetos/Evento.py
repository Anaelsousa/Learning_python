# Exemplo simples de herança, com sobrescrição de atributos e métodos. Sujeito a alterações no futuro com base no aumento de conhecimento do autor.

class Evento:
    def __init__(self, Nome, local):
        self.nome = Nome
        self.local = local

    def exibir_informações(self):
        print(f"Nome: {self.nome}\nLocal: {self.local}")

class Evento_online(Evento):
    id = 1
    def __init__(self, nome, local = "https://meuevento.com/salas"):
        super().__init__(nome, local)
        self.id = Evento_online.id
        Evento_online.id += 1

    def exibir_informações(self):
        print(f"Nome: {self.nome}\nLink: {self.local} ID={self.id}")

ev1 = Evento("Aula de python", "São Paulo")
ev1.exibir_informações()
ev2 = Evento_online("Live de python")
ev2.exibir_informações()
ev3 = Evento_online("Live de java")
ev3.exibir_informações()
ev4 = Evento("Palestra de Anael", "Rio de Janeiro")
ev4.exibir_informações()
