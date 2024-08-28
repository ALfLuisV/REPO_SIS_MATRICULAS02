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
            INSERT INTO discipline (name, credits, type, IdTeacher, IdCourse, period)
            VALUES
            '''

            count = -1
            for disciplina in lista_disciplinas:
                count += 1
                if count == lista_disciplinas_length-1:
                    insert_disciplines_query += f'''
                    ('{disciplina["nome"]}', {disciplina["credit"]}, '{disciplina["tip"]}', {disciplina["prof"]}, {disciplina["id_curso"]}, {disciplina["period"]});
                    '''
                else:
                    insert_disciplines_query += f'''
                    ('{disciplina["nome"]}', {disciplina["credit"]}, '{disciplina["tip"]}', {disciplina["prof"]}, {disciplina["id_curso"]}, {disciplina["period"]}),
                    '''


            

            cursor.execute(insert_disciplines_query)
            connection.commit()
            print("Disciplinas inseridas com sucesso.")
        except Exception as error:
            print(f"Erro ao inserir disciplinas: {error}")
        finally:
            cursor.close()
            connection.close()

# Função para buscar todos as disciplinas de um determinado curso
def buscar_disciplinas(idd):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            buscar_query = "SELECT * FROM discipline WHERE IdCourse = %s;"
            cursor.execute(buscar_query, (idd,))
            disciplinas = cursor.fetchall()
            return disciplinas
        except Exception as error:
            print(f"Erro ao buscar disciplinas: {error}")
        finally:
            cursor.close()
            connection.close()

# Função para buscar todos as disciplinas matriculadas por um determinado aluno
def buscar_disciplinas_por_aluno(idd):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            buscar_query = "SELECT * FROM registration WHERE idstudent = %s;"
            cursor.execute(buscar_query, (idd,))
            disciplinas = cursor.fetchall()
            return disciplinas
        except Exception as error:
            print(f"Erro ao buscar disciplinas: {error}")
        finally:
            cursor.close()
            connection.close()

def matricular_aluno(lista_disciplinas):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            lista_disciplinas_length = len(lista_disciplinas)

            insert_disciplines_query = '''
            INSERT INTO registration (date, status, idstudent, iddiscipline)
            VALUES
            '''

            count = -1
            for disciplina in lista_disciplinas:
                count += 1
                if count == lista_disciplinas_length-1:
                    insert_disciplines_query += f'''
                    ('{disciplina["date"]}', '{disciplina["status"]}', {disciplina["id_student"]}, {disciplina["id_disc"]});
                    '''
                else:
                    insert_disciplines_query += f'''
                    ('{disciplina["date"]}', '{disciplina["status"]}', {disciplina["id_student"]}, {disciplina["id_disc"]}),
                    '''




            # print(insert_disciplines_query)
            cursor.execute(insert_disciplines_query)
            connection.commit()
            print("Matricula realizada com sucesso!!!!")
        except Exception as error:
            print(f"Erro ao buscar disciplinas: {error}")
        finally:
            cursor.close()
            connection.close()

def cancelar_matricula(id_student, id_discipline):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            buscar_query = "DELETE FROM registration WHERE idstudent = %s AND iddiscipline = %s;"
            cursor.execute(buscar_query, (id_student,id_discipline))
            connection.commit()
            print("Matricula(s) excluidas com sucesso!!!")
        except Exception as error:
            print(f"Erro ao excluir disciplinas: {error}")
        finally:
            cursor.close()
            connection.close()