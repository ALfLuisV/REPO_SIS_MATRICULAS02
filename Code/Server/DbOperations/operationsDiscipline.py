import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[2]))


from Server.db_connection import connect_to_db




def inserir_disciplinas(lista_disciplinas):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
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
            buscar_query = "SELECT * FROM discipline WHERE IdCourse = %s AND status = 'ativa';"
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
                    ('{disciplina["date"]}', '{disciplina["status"]}', {disciplina["id_student"]}, {disciplina["id_disc"]})
                    '''
                else:
                    insert_disciplines_query += f'''
                    ('{disciplina["date"]}', '{disciplina["status"]}', {disciplina["id_student"]}, {disciplina["id_disc"]}),
                    '''

            insert_disciplines_query += '''RETURNING idregistration;'''

            discipline_ids = []

            for disciplina in lista_disciplinas:
                discipline_ids.append(disciplina["id_disc"])

            query = f"""
                UPDATE discipline
                SET alunos = alunos + 1
                WHERE iddiscipline IN ({', '.join(map(str, discipline_ids))});
                """
            
            cursor.execute(insert_disciplines_query)
            connection.commit()
            ids = cursor.fetchall()


            cursor.execute(query)
            connection.commit()

            verificar_lotacão()

            print(lista_disciplinas)
            print(ids)
            print("Matricula realizada com sucesso!!!!")
            return ids
        except Exception as error:
            print(f"Erro ao buscar disciplinas: {error}")
        finally:
            cursor.close()
            connection.close()

def cancelar_matricula(id_student, id_discipline):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:

            buscar_id_registration = "SELECT idregistration FROM registration WHERE idstudent = %s AND iddiscipline = %s;"
            cursor.execute(buscar_id_registration, (id_student,id_discipline))
            connection.commit()
            id_registration = cursor.fetchone()[0]

            buscar_query_charge = "DELETE FROM charge WHERE idregistration = %s;"
            cursor.execute(buscar_query_charge, (id_registration,))
            connection.commit()


            buscar_query = "DELETE FROM registration WHERE idstudent = %s AND iddiscipline = %s;"
            cursor.execute(buscar_query, (id_student,id_discipline))
            connection.commit()
            print("Matricula(s) excluidas com sucesso!!!")
        except Exception as error:
            print(f"Erro ao excluir disciplinas: {error}")
        finally:
            cursor.close()
            connection.close()

def get_discipline_type(idd):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            buscar_query = "SELECT type FROM discipline WHERE iddiscipline = %s;"
            cursor.execute(buscar_query, (idd,))
            connection.commit()
            id_discipline = cursor.fetchall()
            return id_discipline
        except Exception as error:
            print(f"Erro ao buscar disciplinas: {error}")
        finally:
            cursor.close()
            connection.close()

def verificar_lotacão():
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            print("atualizando status....")
            verification_query = """
            UPDATE discipline
                SET status = 'cheia'
                WHERE alunos = 60;
            """
            cursor.execute(verification_query)
            connection.commit()
            print("Disciplinas atualizadas com sucesso!!!")
        except Exception as error:
            print(f"Erro ao atualizar disciplinas: {error}")
        finally:
            cursor.close()
            connection.close()


def cancelamento_disciplina():
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            print("atualizando status....")
            verification_query = """
            UPDATE discipline
                SET status = 'cancelada'
                WHERE alunos < 3 AND status = 'ativa';
            """
            cursor.execute(verification_query)
            connection.commit()
            print("Disciplinas atualizadas com sucesso!!!")
        except Exception as error:
            print(f"Erro ao atualizar disciplinas: {error}")
        finally:
            cursor.close()
            connection.close()   

def reiniciar_disciplina():
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            print("atualizando status....")
            verification_query = """
            UPDATE discipline
            SET 
            alunos = 0,
            status = 'ativa'
            WHERE 
            status != 'cancelada';
            """
            cursor.execute(verification_query)
            connection.commit()
            print("Disciplinas atualizadas com sucesso!!!")
        except Exception as error:
            print(f"Erro ao atualizar disciplinas: {error}")
        finally:
            cursor.close()
            connection.close() 