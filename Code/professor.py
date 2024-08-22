from usuario import Usuario
# from Code.Client.Classes.usuario import Usuario

class Professor(Usuario):
    
    def __init__(self, idusuario,nome, telefone, email, cargahoraria, salario):
        super().__init__(idusuario, nome, telefone, email)
        self.idprof = idusuario
        self.cargahoraria = cargahoraria
        self.salario = salario

        def visualizaralunos():
            print("visualizando alunos...")
        