from Classes.usuario import Usuario

class Aluno(Usuario):
    def __init__(self,idusuario, nome, telefone, email, matricula):
        super().__init__(idusuario, nome, telefone, email)
        self.matricula = matricula

        def matricular():
            print("o aluno foi matriculado")

        def cancelarMatricula():
            print("Matricula cancelada!!")