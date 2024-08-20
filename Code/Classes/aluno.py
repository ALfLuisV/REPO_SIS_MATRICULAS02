from usuario import Usuario

class Aluno(Usuario):
    def __init__(self, idaluno, matricula):
        self.idaluno = idaluno
        self.matricula = matricula

        def matricular():
            print("o aluno foi matriculado")

        def cancelarMatricula():
            print("Matricula cancelada!!")