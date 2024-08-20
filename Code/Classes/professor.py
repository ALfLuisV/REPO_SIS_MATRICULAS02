from usuario import Usuario

class Professor(Usuario):
    def __init__(self, idprof, cargahoraria, salario):
        self.idprof = idprof
        self.cargahoraria = cargahoraria
        self.salario = salario

        def visualizaralunos():
            print("visualizando alunos...")
        