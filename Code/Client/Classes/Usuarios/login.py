import bcrypt
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[4]))

from Code.Server.DbOperations.operationsUsers import logar_sistema

class Login():

    def logar_sistema(self, email, senha):
        """
        Metodo para realizar o login, faz uma requisição no bd utilizando o email como identificador do usuario,
        armazena a hash da senha, faz as conversões necessarias e depois utiliza o "checkpw" para validar a senha, utilizando a
        senha inserida pelo usuario e a hash do bd
        """

        usuario = logar_sistema(email) ##objeto com os dados do usuario a ser logado

        # Convertendo `senha_hash` de memoryview para bytes
        senha_hash_bytes = bytes(usuario[4]) #converte a senha do usuario para bytes

        # Verificar a senha
        if bcrypt.checkpw(senha.encode('utf-8'), senha_hash_bytes):
            print("Senha correta!")
            return usuario #retorna os dados o usuario
        else:
            print("Senha incorreta!")
            return False
