from Usuario import Usuario

class Adm(Usuario):
    def __init__(self, nome, email, adm = True):
        super().__init__(nome, email)
        self.adm = adm

    def perfil(self):
    
        print(f"Nome de usuário: {self.nome}\nEmail: {self.email}\nUsuário administrador.\n", "-"*50)
