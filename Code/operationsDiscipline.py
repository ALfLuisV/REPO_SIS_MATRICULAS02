import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))


from db_connection import connect_to_db


def inserir_disciplinas(lista_disciplinas):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:

            # disciplina = {"nome": name, "credit": creditos, "tip": tipo, "prof": idProf, "id_curso": idd}

            lista_disciplinas_length = len(lista_disciplinas)

            insert_disciplines_query = '''
            INSERT INTO discipline (name, credits, type, IdTeacher, IdCourse)
            VALUES
            '''

            count = -1
            for disciplina in lista_disciplinas:
                count += 1
                if count == lista_disciplinas_length-1:
                    insert_disciplines_query += f'''
                    ('{disciplina["nome"]}', {disciplina["credit"]}, '{disciplina["tip"]}', {disciplina["prof"]}, {disciplina["id_curso"]});
                    '''
                else:
                    insert_disciplines_query += f'''
                    ('{disciplina["nome"]}', {disciplina["credit"]}, '{disciplina["tip"]}', {disciplina["prof"]}, {disciplina["id_curso"]}),
                    '''


            

            cursor.execute(insert_disciplines_query)
            connection.commit()
            print("Disciplinas inseridas com sucesso.")
        except Exception as error:
            print(f"Erro ao inserir disciplinas: {error}")
        finally:
            cursor.close()
            connection.close()

# Função para buscar todos os alunos
def buscar_disciplinas(id):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            buscar_query = "SELECT * FROM teacher WHERE IdCourse = {id};"
            cursor.execute(buscar_query, (id))
            profs = cursor.fetchall()
            return profs
        except Exception as error:
            print(f"Erro ao buscar disciplinas: {error}")
        finally:
            cursor.close()
            connection.close()

