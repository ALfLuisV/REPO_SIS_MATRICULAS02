from usuario import Usuario
from operationsTeachers import buscar_disciplinas, buscar_alunos_disciplina, buscar_cursos
# from Code.Client.Classes.usuario import Usuario

class Professor(Usuario):
    
    def __init__(self, idusuario,nome, telefone, email, cargahoraria, salario):
        super().__init__(idusuario, nome, telefone, email)
        self.idprof = idusuario
        self.cargahoraria = cargahoraria
        self.salario = salario

    def visualizaralunos(self, idd):

        cursos = buscar_cursos(idd)

        # for const in cursos:
        print(cursos)  

        id_disciplina = input("Insira o id do curso selecionado: ")

        disciplinas = buscar_disciplinas(idd, id_disciplina)
        for const in disciplinas:
            print(const)

        id_disciplina = input("Insira o id da disciplina: ")
        students = buscar_alunos_disciplina(id_disciplina)
        for const in students:
            print(const)

