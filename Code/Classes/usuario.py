class Usuario:
    def __init__(self, idusuario, nome, telefone, email, senha):
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.senha = senha

        def atualizarendereco(novoendereco):
            print("em breve")
            
        def atualizarsenha(novasenha):
            self.senha = novasenha