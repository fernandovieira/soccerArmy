
class TabelaClassificacaoModel(object):

    def __init__(self):
        self.posicao = ""
        self.time = ""
        self.variacao = ""
        self.numeroJogos = ""
        self.pontosGanho = ""
        self.numeroVitorias = ""
        self.numeroEmpates = ""
        self.golsPro = ""
        self.golsContra = ""
        self.saldoGols = ""
        self.aproveitamento = ""

    @property
    def nomeTime(self):
        return self.time

    @nomeTime.setter
    def nomeTime(self, value):
        self.time = value[0]
