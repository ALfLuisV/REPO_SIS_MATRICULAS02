import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[4]))

from Code.Server.DbOperations.operationsTeachers import buscar_disciplinas, buscar_alunos_disciplina, buscar_cursos


from Code.Client.Classes.Usuarios.usuario import Usuario

class Professor(Usuario):
    
    def __init__(self, idusuario,nome, telefone, email, cargahoraria, salario):
        super().__init__(idusuario, nome, telefone, email)
        self.idprof = idusuario
        self.cargahoraria = cargahoraria
        self.salario = salario

    def visualizaralunos(self, idd):

        """
        recebe como argumento, o id do professor, utiliza o metodo "buscar_cursos()" para buscar todos os cursos onde
        este professor ministra aulas, depois busca disciplinas deste curso onde o mesmo da aulas, utilizando o medoto
        "buscar_disciplinas()", e apos inserir o id da disciplina, busca os alunos relacionados a mesma utlizando o metodo 
        "buscar_alunos_disciplina()"
        """

        cursos = buscar_cursos(idd)

        print(cursos)  

        id_disciplina = input("Insira o id do curso selecionado: ")

        disciplinas = buscar_disciplinas(idd, id_disciplina)
        for const in disciplinas:
            print(const)

        id_disciplina = input("Insira o id da disciplina: ")
        students = buscar_alunos_disciplina(id_disciplina)
        if len(students) == 0:
            print("Nenhum aluno matriculado")
        else:
            for const in students:
                print(const)

