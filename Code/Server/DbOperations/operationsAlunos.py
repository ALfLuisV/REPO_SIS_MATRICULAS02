import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))


from db_connection import connect_to_db

# Função para inserir dados na tabela 'alunos'
def inserir_aluno(nome, email, telefone):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            inserir_query = '''
            INSERT INTO alunos (nome, email, telefone) 
            VALUES (%s, %s, %s);
            '''
            cursor.execute(inserir_query, (nome, email, telefone))
            connection.commit()
            print("Aluno inserido com sucesso.")
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
            buscar_query = "SELECT * FROM alunos;"
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
