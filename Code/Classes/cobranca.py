class Cobranca:
    def __init__(self, idcobranca, tempodivida, juros, status):
        self.idcobranca = idcobranca
        self.tempodivida = tempodivida
        self.juros = juros
        self.status = status

        def notificarcobranca():
            print("notificando")