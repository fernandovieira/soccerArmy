from goodSpy.TabelaClassificacaoModel import TabelaClassificacaoModel


class TabelaClassificacaoWrapper(object):

    def __init__(self):
        self.dicionario = []

    def extract(self, response):

        tabelaTimes = response.xpath('//table[@class="tabela-times"]')

        tabelaPontos = response.xpath('//table[@class="tabela-pontos"]')

        tabelaPontosLinha = tabelaPontos.xpath(
            './/tr[@class="tabela-body-linha"]')

        numeroLinha = 0

        for linha in tabelaTimes.xpath('.//tr[@class="tabela-body-linha"]'):
            tabelaClassificacaoModel = TabelaClassificacaoModel()

            tabelaClassificacaoModel.posicao = linha.xpath(
                './/td[@class="tabela-times-posicao"]/text()').extract()
            tabelaClassificacaoModel.nomeTime = linha.xpath(
             './/strong[@class="tabela-times-time-nome"]/text()').extract()
            tabelaClassificacaoModel.variacao = linha.xpath(
              './/td[@class="tabela-times-variacao"]//span/text()').extract()

            sobeDesce = linha.xpath(
                './/td[@class="tabela-times-variacao"]')

            if (sobeDesce.xpath(
              './/span[contains(@class, "tabela-icone tabela-icone-positiva")]'
            ) != []):
                variacao = tabelaClassificacaoModel.variacao * -1
                tabelaClassificacaoModel.variacao = variacao

            itensTabela = []

            for pontosLinha in tabelaPontosLinha[numeroLinha].xpath(
             './/td/text()'):
                itensTabela.append(pontosLinha.extract())

            numeroLinha = numeroLinha + 1

            tabelaClassificacaoModel.pontosGanhos = itensTabela[0]
            tabelaClassificacaoModel.numeroJogos = itensTabela[1]
            tabelaClassificacaoModel.numeroVitorias = itensTabela[2]
            tabelaClassificacaoModel.numeroEmpates = itensTabela[3]
            tabelaClassificacaoModel.setGolsPro = itensTabela[4]
            tabelaClassificacaoModel.golsPro = itensTabela[5]
            tabelaClassificacaoModel.saldoGols = itensTabela[6]
            tabelaClassificacaoModel.aproveitamento = itensTabela[7]

            self.dicionario.append(tabelaClassificacaoModel.__dict__)
