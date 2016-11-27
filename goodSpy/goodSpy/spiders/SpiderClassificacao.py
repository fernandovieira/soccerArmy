import scrapy
from goodSpy.TabelaClassificacaoWrapper import TabelaClassificacaoWrapper
from goodSpy.items import GoodspyItem
# import json


class SpiderClassificacao(scrapy.Spider):
    name = 'SpiderClassificacao'

    def start_requests(self):
        urls = ['http://globoesporte.globo.com/futebol/brasileirao-serie-a/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        tabelaClassificacaoWrapper = TabelaClassificacaoWrapper()

        tabelaClassificacaoWrapper.extract(response)

        # dicionario.append(tabelaClassificacao.__dict__)

        # tabelaClassificacao.setClassificacao(
        #             posicao[0], time[0], variacao[0], itensTabela)

        # print(tabelaClassificacaoWrapper.dicionario)

        # tabela = json.dumps(tabelaClassificacaoWrapper.dicionario)
        yield GoodspyItem(classificacao=tabelaClassificacaoWrapper.dicionario)
