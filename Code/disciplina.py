class Disciplina:
    def __init__(self, iddisciplina, nomedisciplina, numcreditos, status):
        self.iddisciplina = iddisciplina
        self.nomedisciplina = nomedisciplina
        self.numcreditos = numcreditos
        self.status = status

        def verificarstatus():
            print("verificando")
            return 1