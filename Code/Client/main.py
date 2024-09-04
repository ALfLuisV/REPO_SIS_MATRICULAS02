import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[2]))



from Classes.Usuarios.login import Login
from Classes.Usuarios.secretario import Secretario
from Classes.Usuarios.aluno import Aluno
from Classes.Usuarios.professor import Professor


from Server.DbOperations.operationsDiscipline import buscar_disciplinas_por_aluno
from Code.Server.DbOperations.operationsTeachers import buscar_disciplinas, buscar_alunos_disciplina, buscar_cursos

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

log = Login()

while True:  # Loop principal do programa
    limpar_tela()  # Limpa a tela ao começar o menu principal
    print("*************** Bem vindo ao sistema de gerência de matrículas! ***************")
    tipo = input("Selecione o seu tipo de usuário (Secretario: 1, Aluno: 2, Professor: 3) ou 'q' para sair: ")

    if tipo == '1':
        limpar_tela()  # Limpa a tela antes de mostrar o menu do secretário
        print("Secretario")
        email = input("Insira seu email: ")
        senha = input("Insira sua senha: ")
        user = log.logar_sistema(email, senha)
        
        if user:
            sec1 = Secretario(1, "x", "x", "x", "x")
            while True:  # Loop do menu do secretário
                limpar_tela()  # Limpa a tela antes de mostrar o menu de opções do secretário
                print("MENU DE OPÇÕES:\n1-Cadastrar Curso\n2-Cadastrar disciplina\n3-Cadastrar Usuário\n4-Gerar Currículo\n5-Logout")
                opcao = input("Insira o número da opção desejada: ")

                if opcao == '1':
                    sec1.cadastrar_curso()
                elif opcao == '2':
                    sec1.cadastrar_disciplina_em_curso_existente()
                elif opcao == '3':
                    print("USUÁRIOS:\n1-Secretário\n2-Professor\n3-Aluno")
                    tipoUsuario = input("Insira o número da opção desejada: ")
                    if tipoUsuario == '1':
                        sec1.cadastrar_secretario()
                    elif tipoUsuario == '2':
                        sec1.cadastrar_professor()
                    elif tipoUsuario == '3':
                        sec1.cadastrar_aluno()
                    else:
                        print("Opção inválida!")
                elif opcao == '4':
                    sec1.gerarcurriculo()
                elif opcao == '5':
                    break  # Sai do menu do secretário e volta ao login principal
                else:
                    print("Opção inválida!")
                input("\nPressione Enter para continuar...")  # Pausa para o usuário ver a saída antes de limpar a tela novamente

    elif tipo == '2':
        limpar_tela()  # Limpa a tela antes de mostrar o menu do aluno
        print("Aluno:")
        email = input("Insira seu email: ")
        senha = input("Insira sua senha: ")
        user = log.logar_sistema(email, senha)

        if user:
            aluno1 = Aluno(1, "x", "x", "x", "x")
            while True:  # Loop do menu do aluno
                limpar_tela()  # Limpa a tela antes de mostrar o menu de opções do aluno
                print("MENU DE OPÇÕES:\n1-Se Matricular\n2-Cancelar Matricula\n3-Visualizar disciplinas matriculadas\n4-Logout")
                opcao = input("Insira o número da opção desejada: ")

                if opcao == '1':
                    aluno1.matricular(user[0])
                elif opcao == '2':
                    aluno1.cancelarMatricula(user[0])
                elif opcao == '3':
                    aluno1.buscar_matriculas_aluno(user[0])
                elif opcao == '4':
                    break  # Sai do menu do aluno e volta ao login principal
                else:
                    print("Opção inválida!")
                input("\nPressione Enter para continuar...")  # Pausa para o usuário ver a saída antes de limpar a tela novamente

    elif tipo == '3':
        limpar_tela()  # Limpa a tela antes de mostrar o menu do professor
        print("Professor:")
        email = input("Insira seu email: ")
        senha = input("Insira sua senha: ")
        user = log.logar_sistema(email, senha)

        if user:
            prof = Professor(1, 'x', 'x', 'x', 'x', 320.00)
            while True:  # Loop do menu do professor
                limpar_tela()  # Limpa a tela antes de mostrar o menu de opções do professor
                print("MENU DE OPÇÕES:\n1-Visualizar disciplinas\n2-Logout")
                opcao = input("Insira o número da opção desejada: ")

                if opcao == '1':
                    prof.visualizaralunos(user[0])
                elif opcao == '2':
                    break  # Sai do menu do professor e volta ao login principal
                else:
                    print("Opção inválida!")
                input("\nPressione Enter para continuar...")  # Pausa para o usuário ver a saída antes de limpar a tela novamente

    elif tipo == 'q':
        limpar_tela()
        print("Saindo do sistema...")
        break  # Sai do loop principal e encerra o programa

    else:
        print("Opção inválida! Por favor, selecione uma opção válida.")
