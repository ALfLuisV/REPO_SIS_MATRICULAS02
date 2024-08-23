import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[3]))
import bcrypt
import random
from operationsStudents import inserir_aluno, buscar_alunos
from operationsTeachers import inserir_prof, buscar_profs
from operationsSecretary import inserir_secretario, buscar_secretarios
from operationsCourses import inserir_curso, buscar_cursos
from operationsDiscipline import inserir_disciplinas, buscar_disciplinas
from operationsAdress import inserir_endereco, buscar_endereco
from professor import Professor
from aluno import Aluno
from usuario import Usuario
from curso import Curso
from endereco import Endereco

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
        """
        fodase porraaaaaaaaaaaa
        """
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
    
    def gerar_saltkey(self):
     alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
     return "".join(random.choice(alphabet) for i in range(64))
         

    def gerarcurriculo(self):
        """
        gera o curriculo
        """
        print("em breve")

    def cadastrar_aluno(self):
        """
        Cadastra um aluno solicitando informações ao usuário via input.

        Este método solicita o nome, telefone, e-mail e gera uma senha para o aluno.
        Cria uma instância de Usuario com essas informações e exibe os dados.
        """
        name = input("Insira o nome do aluno:")
        tel = input("Insira o telefone do aluno:")
        email = input("Insira o email do aluno:")
        senha_gerada = self.gerarsenha()
        user1 = Aluno("", name, tel, email, "XXXXXX")
        user1.senha = senha_gerada
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
        cadastra o professor
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
        street = input("Insira a rua: ")
        city = input("Insira a cidade: ")
        state = input("Insira o estado: ")
        country = input("Insira o país: ")

        end = Endereco(street, city, state, country)
        inserir_endereco(end.rua, end.cidade, end.estado, end.pais, idd)

        



    def cadastrar_curso(self):
        name = input("Insira o nome do curso: ")
        creditos = input("Insira o total de creditos do curso: ")
        curso = Curso(1, name, creditos)

        idCourse = inserir_curso(curso.nomecurso, curso.numcreditos)#id do curso cadastrado, serve para a inserção das disciplinas no mesmo
        self.inserir_disciplinas_em_novo_curso(idCourse)

    def criar_array_disciplinas(self, idd):
        #Cria o array de disciplinas para ser inserida na tabela de disciplinas no bd (o id do curso pertencente já vai inserido no array)
        contInue = True
        lista_disciplinas = []
        professores = buscar_profs()

        while contInue:
            name = input("Insira o nome da disciplina: ")
            creditos = input("Insira os creditos da disciplina: ")
            tipo = input("insira o tipo de disciplina(Optativa/Obrigatoria): ")
            
            for prof in professores:
                print(prof)
            idProf = input("Insira o id do professor: ")
            disciplina = {"nome": name, "credit": creditos, "tip": tipo, "prof": idProf, "id_curso": idd}
            lista_disciplinas.append(disciplina)
            cont = input("Deseja adicionar mais uma disciplina?(SIM: 1/ NÃO: 0):")
            if cont == "0":
                contInue = False
        return lista_disciplinas
    
    def inserir_disciplinas_em_novo_curso(self, idd):
        lista_disciplinas = self.criar_array_disciplinas(idd)
        inserir_disciplinas(lista_disciplinas)
        

    def cadastrar_disciplina_em_curso_existente(self):
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
