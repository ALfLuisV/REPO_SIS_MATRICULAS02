import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[4]))

import bcrypt
import random

from Code.Server.DbOperations.operationsStudents import inserir_aluno, buscar_alunos
from Code.Server.DbOperations.operationsTeachers import inserir_prof, buscar_profs 
from Code.Server.DbOperations.operationsSecretary import inserir_secretario, buscar_secretarios
from Code.Server.DbOperations.operationsCourses import inserir_curso, buscar_cursos
from Code.Server.DbOperations.operationsDiscipline import inserir_disciplinas, buscar_disciplinas, cancelamento_disciplina, reiniciar_disciplina
from Code.Server.DbOperations.operationsAdress import inserir_endereco, buscar_endereco





# sys.path.append(str(Path(__file__).parents[0]))

from Code.Client.Classes.Usuarios.professor import Professor
from Code.Client.Classes.Usuarios.aluno import Aluno
from Code.Client.Classes.Usuarios.usuario import Usuario
from Code.Client.Classes.Cursos.curso import Curso
from Code.Client.Classes.Usuarios.endereco import Endereco

class Secretario(Usuario):
    """
        sei ainda n
    """
    def __init__(self, idusuario, nome, telefone, email, turno):
        senha_gerada = self.gerarsenha()
        super().__init__(idusuario, nome, telefone, email)
        self.idsecretario = idusuario
        self.turno = turno
        self.senha = senha_gerada


    def buscaralunos(self):
        alunos = buscar_alunos()
        for aluno in alunos:
            print(aluno)

    def gerarsenha(self):
        """
        este metodo é utilizado para gerar uma senha contendo letras maiusculas, minusculas e numeros.
        Se baseia na geração randomica de um numero e a inserção do seu caractere respectivo da tabela ascii na string da senha
        """
        password = ""
        for i in range(7):
            while True:
                number = random.randrange(48, 122)
                if (not (number >= 58 and number <= 64)) and (not (number >= 91 and number <= 96)):
                    break
            password += chr(number)
        return password
         

    def gerarcurriculo(self):
        """
        
        primeiro,realiza a verificação de turmas com < 3 alunos e seta o status para cancelado ("cancelamento_disciplina()")
        
        verifica as turmas que estão cheias, altera o status pra ativa e zera o numero de alunos("reiniciar_disciplina()")

        exibe todas as ativas no curriculo
        """


        cancelamento_disciplina()

        reiniciar_disciplina()

        cursos = buscar_cursos()
        for curso in cursos:
            print(curso)

        id_curso = input("insira o id do curso desejado: ")

        disciplinas = buscar_disciplinas(id_curso)

        disciplinas.sort(key=lambda x: x[6])

        print(disciplinas) #ordenar este array

    def cadastrar_aluno(self):
        """
        cadastra o aluno e utiliza uma senha criptografada
        """

        name = input("Insira o nome do aluno:")
        tel = input("Insira o telefone do aluno:")
        email = input("Insira o email do aluno:")
        senha_gerada = self.gerarsenha()
        user1 = Aluno("", name, tel, email, "XXXXXX")
        user1.senha = senha_gerada
        print(senha_gerada)
        sk = bcrypt.gensalt()
        senha_hash = bcrypt.hashpw(senha_gerada.encode('utf-8'), sk)
        id_usuario = inserir_aluno(user1.nome, user1.email, user1.telefone, senha_hash, sk)
        self.inserir_endereco(id_usuario)



        # verificação de senha:
        # if bcrypt.checkpw(user1.senha.encode('utf-8'), senha_hash):
        #       print("Senha correta!")
        # else:
        #       print("Senha incorreta!")


    def cadastrar_professor(self):
        """
        cadastra o professor e utiliza uma senha criptografada
        """
        name = input("Insira o nome do professor:")
        tel = input("Insira o telefone do professor:")
        email = input("Insira o email do professor:")
        carga_horaria = input("Insira a carga horária do professor:")
        salario = input("insira o salário do professor:")
        senha_gerada = self.gerarsenha()
        prof = Professor(1, name, tel, email, carga_horaria, salario)
        prof.senha = senha_gerada
        sk = bcrypt.gensalt()
        senha_hash = bcrypt.hashpw(senha_gerada.encode('utf-8'), sk)
        id_usuario = inserir_prof(prof.nome, prof.email, prof.telefone, senha_hash, sk, prof.cargahoraria, prof.salario)
        self.inserir_endereco(id_usuario)

        
    def cadastrar_secretario(self):
        """
        cadastra o secretário e utiliza uma senha criptografada
        """

        name = input("Insira o nome do secretário:")
        tel = input("Insira o telefone do secretário:")
        email = input("Insira o email do secretário:")
        turno = input("Insira o turno do secretário")
        senha_gerada = self.gerarsenha()
        sec = Secretario(1, name, tel, email, turno)
        sec.senha = senha_gerada
        sk = bcrypt.gensalt()
        senha_hash = bcrypt.hashpw(senha_gerada.encode('utf-8'), sk)
        id_usuario = inserir_secretario(sec.nome, sec.email, sec.telefone, senha_hash, sk, sec.turno)
        self.inserir_endereco(id_usuario)
    
    def inserir_endereco(self, idd):
        """
        metodo utilizado para inserir o endereço em um id de um usuario(novo ou previamente criado),
        recebe o id deste usuario como argumento e insere os dados no banco pela função "inserir_endereco"
        """
        print("Cadastre o endereço:")
        street = input("Insira a rua: ")
        city = input("Insira a cidade: ")
        state = input("Insira o estado: ")
        country = input("Insira o país: ")

        end = Endereco(street, city, state, country)
        inserir_endereco(end.rua, end.cidade, end.estado, end.pais, idd)

        



    def cadastrar_curso(self):
        """
        cadastra o curso, lmao
        """
        name = input("Insira o nome do curso: ")
        creditos = input("Insira o total de creditos do curso: ")
        curso = Curso(1, name, creditos)

        idCourse = inserir_curso(curso.nomecurso, curso.numcreditos)#id do curso cadastrado, serve para a inserção das disciplinas no mesmo
        self.inserir_disciplinas_em_novo_curso(idCourse)

    def criar_array_disciplinas(self, idd):
        """
        Cria e retorna o array de disciplinas para serem inseridas na tabela de disciplinas no bd (o id do curso pertencente já vai inserido no array)
        """

        contInue = True
        lista_disciplinas = []
        professores = buscar_profs()

        while contInue:
            name = input("Insira o nome da disciplina: ")
            creditos = input("Insira os creditos da disciplina: ")
            tipo = input("insira o tipo de disciplina(Optativa/Obrigatoria): ")
            periodo = input("Insira o perido do curso referente a disciplina: ")
            
            for prof in professores:
                print(prof)
            idProf = input("Insira o id do professor: ")
            disciplina = {"nome": name, "credit": creditos, "tip": tipo, "prof": idProf, "id_curso": idd, "period": periodo}
            lista_disciplinas.append(disciplina)
            cont = input("Deseja adicionar mais uma disciplina?(SIM: 1/ NÃO: 0):")
            if cont == "0":
                contInue = False
        return lista_disciplinas
    
    def inserir_disciplinas_em_novo_curso(self, idd):
        """
        metodo onde disciplinas serão inseridas num curso recem criado, onde as disciplinas serão cadastradas no metodo "criar_array_disciplinas"
         e depois inseridas no banco pelo metodo "inserir_disciplinas"
        """

        lista_disciplinas = self.criar_array_disciplinas(idd)
        inserir_disciplinas(lista_disciplinas)
        

    def cadastrar_disciplina_em_curso_existente(self):
        """
        metodo responsavel por cadastrar a disciplina em um curso já existente, onde ele mostra a lista de cursos,
        o secretario insere o id no metodo do cadastro de disciplinas chamado "criar_array_disciplinas", e depois estas disciplinas são inseridas no banco de dados 
        pelo metodo "inserir_disciplina"
         """
        

        cursos = buscar_cursos()
        print("Lista de cursos:")
        print(cursos)
        idd = input("insira o id do curso desejado:")
        lista_disciplinas = self.criar_array_disciplinas(idd)
        inserir_disciplinas(lista_disciplinas)

    def removeraluno(self):
        """
        sei ainda n
        """
        print("em breve")

    def atualizardados(self):
        """
        sei ainda n
        """
        print("em breve")

    def consultardados(self):
        """
        sei ainda n
        """
        print("em breve")
