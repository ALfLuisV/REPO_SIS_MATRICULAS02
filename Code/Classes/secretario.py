import random
from .professor import Professor
from .aluno import Aluno
from .usuario import Usuario

from .operations import buscar_alunos, inserir_aluno



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

    def gerarcurriculo(self):
        """
        gera o curriculo
        """
        print("em breve")

    def cadastraraluno(self):
        """
        Cadastra um aluno solicitando informações ao usuário via input.

        Este método solicita o nome, telefone, e-mail e gera uma senha para o aluno.
        Cria uma instância de Usuario com essas informações e exibe os dados.
        """
        name = input("Insira o nome do aluno:")
        tel = input("Insira o telefone do aluno:")
        email = input("Insira o email do aluno:")
        senha_gerada = self.gerarsenha()
        user1 = Aluno(1, name, tel, email, "XXXXXXX")
        user1.senha = senha_gerada
        print(user1.nome)
        print(user1.telefone)
        print(user1.email)
        print(user1.senha)
        inserir_aluno(user1.nome, user1.email, user1.telefone)
        # buscar_alunos()

    def cadastrarprofessor(self):
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
