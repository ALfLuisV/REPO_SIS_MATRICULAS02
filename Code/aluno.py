from datetime import datetime
from usuario import Usuario
from operationsCourses import buscar_cursos
from operationsDiscipline import buscar_disciplinas, matricular_aluno, cancelar_matricula, buscar_disciplinas_por_aluno


class Aluno(Usuario):
    def __init__(self, idusuario, nome, telefone, email, matricula):
        super().__init__(idusuario, nome, telefone, email)
        self.matricula = matricula

    def matricular(self, id_aluno):
            lista_cursos = buscar_cursos()
            print("Lista de cursos:")
            print(lista_cursos)
            idd = input("insira o codigo do curso desejado: ")
            disciplinas = buscar_disciplinas(idd)
            print("Lista de disciplinas do curso selecionado:")
            print(disciplinas) 

            lista = self.criar_lista_matricula(id_aluno, disciplinas)
            matricular_aluno(lista)

    def criar_lista_matricula(self, id_aluno, disciplinas):
                """
                cria uma lista de matriculas nas disciplinas desejadas(o array gerado por este metodo, vai ser utilizado na criação
                da query sql do banco de dados)
                """


                lista_disciplinas = []
                cont = True

                while cont:
                    obrigatorias = 0
                    optativas = 0
                    id_disciplina = input("Insira o id da disciplina que deseja se cadastrar: ")
                    

                    data_e_hora_atuais = datetime.now()
                    matricula = {"date": data_e_hora_atuais, "id_student": id_aluno,
                        "status": "pendente", "id_disc": id_disciplina}

                    lista_disciplinas.append(matricula)

                    for my_disc in lista_disciplinas:
                        for disc in disciplinas:
                            if disc[0] == int(my_disc['id_disc']):
                                if disc[4] == "Obrigatoria":
                                    obrigatorias += 1
                                elif disc[4] == "Optativa":
                                    optativas += 1

                    if obrigatorias > 4:
                        print("Numero de matriculas de disciplinas obrigatorias ultrapassado!!")
                        lista_disciplinas = self.remover_matricula(lista_disciplinas)
                    elif optativas > 2:
                        print("Numero de matriculas de disciplinas optativas ultrapassado!!")
                        lista_disciplinas = self.remover_matricula(lista_disciplinas)

                    contInue = input(
                        "Deseja adicionar mais uma disciplina?(SIM: 1/ NÃO: 0):")
                    if contInue == "0":
                        cont = False

                return lista_disciplinas


    def remover_matricula(self, disciplinas):
        """
        metodo para remover alguma matricula em disciplina do array do aluno, utilizado quando ele se matricula em mais disciplinas
        do que o limite estabelecido (pode ser utilizado em caso de opção facultativa de exclusão)
        """

        cont = True

        while cont:
            idd = input("insira o id da disciplina que deseja remover: ")
            print(disciplinas)
            for index in disciplinas:
                if index['id_disc'] == idd:
                    disciplinas.remove(index)




            contInue = input(
                        "Deseja remover mais uma disciplina?(SIM: 1/ NÃO: 0):")
            if contInue == "0":
                cont = False

            for i in disciplinas:
                    print(i)
        
        return disciplinas

    def cancelarMatricula(self, id_aluno):
        disciplinas = buscar_disciplinas_por_aluno(id_aluno)

        for e in disciplinas:
             print(e)
        
        id_disciplina = input("insira o id da materia que deseja cancelar a matricula:")
        
        cancelar_matricula(id_aluno ,id_disciplina)



        print("Matricula cancelada!!")
