import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[2]))


from Server.db_connection import connect_to_db

# Função para inserir dados na tabela 'alunos'
def inserir_aluno(nome, email, telefone, senha, sk):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            inserir_query_usuario = '''
            INSERT INTO users (name, number, email, password, saltk) 
            VALUES (%s, %s, %s, %s, %s)
            RETURNING idusuario;
            '''
            
            cursor.execute(inserir_query_usuario, (nome, telefone , email, senha, sk))
            idUsuario = cursor.fetchone()[0]
            connection.commit()
            print("usuario criado....")

            inserir_query_aluno = '''
            INSERT INTO Student (idStudent, registration)
            VALUES (%s, %s);
            '''
            cursor.execute(inserir_query_aluno, (idUsuario, idUsuario * 10))
            connection.commit()
            print("Aluno inserido com sucesso.")
            return idUsuario
        except Exception as error:
            print(f"Erro ao inserir aluno: {error}")
        finally:
            cursor.close()
            connection.close()

# Função para buscar todos os alunos
def buscar_alunos():
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            buscar_query = '''
SELECT s.idstudent, u.name
FROM student s
JOIN users u ON s.idstudent = u.idusuario;

'''
            cursor.execute(buscar_query)
            alunos = cursor.fetchall()
            return alunos
            # for aluno in alunos:
            #     print(aluno)
        except Exception as error:
            print(f"Erro ao buscar alunos: {error}")
        finally:
            cursor.close()
            connection.close()

def excluir_aluno():
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            alunos = buscar_alunos()

            for e in alunos:
                print(e)


            id_aluno = input("Digite o id do aluno a ser excluido")

            delete_queryD = "DELETE FROM address WHERE idusuario = %s;"
            cursor.execute(delete_queryD, (id_aluno,))
            connection.commit()

            delete_queryB = "DELETE FROM charge WHERE idstudent = %s;"
            cursor.execute(delete_queryB, (id_aluno,))
            connection.commit()

            delete_queryA = "DELETE FROM registration WHERE idstudent = %s;"
            cursor.execute(delete_queryA, (id_aluno,))
            connection.commit()

            delete_query = "DELETE FROM student WHERE idstudent = %s;"
            cursor.execute(delete_query, (id_aluno,))
            connection.commit()

            delete_queryC = "DELETE FROM users WHERE idusuario = %s;"
            cursor.execute(delete_queryC, (id_aluno,))
            connection.commit()


            print("Aluno foi excluido com sucesso!!!")
            return alunos
            # for aluno in alunos:
            #     print(aluno)
        except Exception as error:
            print(f"Erro ao buscar alunos: {error}")
        finally:
            cursor.close()
            connection.close()