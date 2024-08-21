from .usuario import Usuario
from .aluno import Aluno
import random

class Secretario(Usuario):
    def __init__(self, idsecretario, turno):
        self.idsecretario = idsecretario
        self.turno = turno

        def gerarcurriculo():
            print("em breve")

        def cadastraraluno():
            name = input("Insira o nome do aluno:")
            tel = input("Insira o telefone do aluno:")
            email = input("Insira o email do aluno:")
            senha = self.gerarsenha()
            user1 = Usuario(1,name, tel, email, senha)
            print(user1.name)
            print(user1.tel)
            print(user1.email)
            print(user1.senha)






        def removeraluno():
            print("em breve")

        def atualizardados():
            print("em breve")

        def consultardados():
            print("em breve")


        def gerarsenha():
            password = ""
            for i in range(5):
                number = random.randrange(48,122)
                password += chr(number)
            return password






