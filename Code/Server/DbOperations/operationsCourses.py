import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[2]))


from Server.db_connection import connect_to_db


def inserir_curso(name, creditos):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            inserir_query_curso = '''
            INSERT INTO course (name, credits) 
            VALUES (%s, %s)
            RETURNING idCourse;
            '''
            
            cursor.execute(inserir_query_curso, (name, creditos))
            idCurso = cursor.fetchone()[0]
            connection.commit()
            print("Curso inserido com sucesso.")
            return idCurso #retorna o id do curso selecionado para inserção de disciplinas no mesmo
        except Exception as error:
            print(f"Erro ao inserir curso: {error}")
        finally:
            cursor.close()
            connection.close()

# Função para buscar todos os cursos
def buscar_cursos():
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            buscar_query = "SELECT * FROM course;"
            cursor.execute(buscar_query)
            cursos = cursor.fetchall()
            return cursos
        except Exception as error:
            print(f"Erro ao buscar cursos: {error}")
        finally:
            cursor.close()
            connection.close()
