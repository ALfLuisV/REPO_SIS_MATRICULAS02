import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))


from db_connection import connect_to_db


def inserir_prof(nome, email, telefone, senha, cargaH, salario):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            inserir_query_usuario = '''
            INSERT INTO users (name, number, email, password) 
            VALUES (%s, %s, %s, %s)
            RETURNING idusuario;
            '''
            
            cursor.execute(inserir_query_usuario, (nome, telefone , email, senha))
            idUsuario = cursor.fetchone()[0]
            connection.commit()
            print("usuario criado....")
            
            inserir_query_prof = '''
            INSERT INTO teacher (idTeacher, workload, salary)
            VALUES (%s, %s, %s);
            '''
            cursor.execute(inserir_query_prof, (idUsuario, cargaH, float(salario)))
            connection.commit()
            print("Professor inserido com sucesso.")
        except Exception as error:
            print(f"Erro ao inserir professor: {error}")
        finally:
            cursor.close()
            connection.close()

# Função para buscar todos os alunos
def buscar_profs():
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            buscar_query = "SELECT * FROM teacher;"
            cursor.execute(buscar_query)
            alunos = cursor.fetchall()
            return alunos
            # for aluno in alunos:
            #     print(aluno)
        except Exception as error:
            print(f"Erro ao buscar professores: {error}")
        finally:
            cursor.close()
            connection.close()
