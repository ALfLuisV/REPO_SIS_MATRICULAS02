import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[2]))




from Code.Client.Classes.Usuarios.aluno import Aluno
from Code.Client.Classes.Usuarios.secretario import Secretario
from Code.Client.Classes.Usuarios.professor import Professor
from Code.Client.Classes.Usuarios.login import Login


sec1 = Secretario(1, "maria","33753729","maria@gmail.com", "manha")
# log = Login()
# log.logar_sistema("mateus@gmail.com", "6qkC50U")
# sec1.cadastrar_aluno()
aluno = Aluno(1, "JV", "31990890989", "jvdobairro@gmail.com","xxxxxxxxx")
aluno.matricular(29)

prof = Professor(1, "mario", "33759686","mario@gmail.com", 40, 3200.00 )

# prof.visualizaralunos(30)
# sec1.cadastrar_secretario()
# sec1.cadastrar_curso()
# sec1.cadastrar_disciplina_em_curso_existente()
# sec1.gerarcurriculo()