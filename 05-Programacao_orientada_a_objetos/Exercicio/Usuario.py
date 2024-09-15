class Usuario:
    count_usuarios = 0
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        Usuario.count_usuarios += 1

    def perfil(self):
        print(f"Nome de usuário: {self.nome}\n Email: {self.email}\n", "-"*50)

    @classmethod
    def status(cls):
        print(f"Até o momento, {cls.count_usuarios} usuários foram cadastrados.")
