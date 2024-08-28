import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))


from db_connection import connect_to_db


def inserir_prof(nome, email, telefone, senha, sk,  cargaH, salario):
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
            
            inserir_query_prof = '''
            INSERT INTO teacher (idTeacher, workload, salary)
            VALUES (%s, %s, %s);
            '''
            cursor.execute(inserir_query_prof, (idUsuario, cargaH, float(salario)))
            connection.commit()
            print("Professor inserido com sucesso.")
            return idUsuario
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
            buscar_query = '''
            SELECT 
                t.idteacher, 
                u.name AS professor_name, 
                t.workload, 
                t.salary
            FROM 
                users u
            JOIN 
                teacher t 
            ON 
                u.idusuario = t.idteacher;
            '''
            cursor.execute(buscar_query)
            profs = cursor.fetchall()
            return profs
        except Exception as error:
            print(f"Erro ao buscar professores: {error}")
        finally:
            cursor.close()
            connection.close()

def buscar_disciplinas(idd):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            buscar_query = '''
            SELECT 
    d.iddiscipline, 
    d.name AS discipline_name, 
    d.credits, 
    d.idcourse, 
    d.type,
    c.name AS course_name, 
    t.idteacher 
FROM 
    discipline d
JOIN 
    course c ON d.idcourse = c.idcourse
JOIN 
    teacher t ON d.idteacher = t.idteacher
WHERE 
    t.idteacher = %s; 

            '''
            cursor.execute(buscar_query, (idd,))
            profs = cursor.fetchall()
            return profs
        except Exception as error:
            print(f"Erro ao buscar disciplinas: {error}")
        finally:
            cursor.close()
            connection.close()

def buscar_alunos_disciplina(id_disciplina):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            buscar_query = '''
            SELECT 
    u.name, 
    u.email
FROM 
    registration r
JOIN 
    student s ON r.idstudent = s.idstudent
JOIN 
    users u ON s.idstudent = u.idusuario
WHERE 
    r.iddiscipline = %s;

            '''
            cursor.execute(buscar_query, (id_disciplina,))
            profs = cursor.fetchall()
            return profs
        except Exception as error:
            print(f"Erro ao buscar disciplinas: {error}")
        finally:
            cursor.close()
            connection.close()

