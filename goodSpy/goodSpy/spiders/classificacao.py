import scrapy
from goodSpy.items import TabelaClassificacao
from goodSpy.items import GoodspyItem
import json


class Classificacao(scrapy.Spider):
    name = 'classificacao'

    def start_requests(self):
        urls = ['http://globoesporte.globo.com/futebol/brasileirao-serie-a/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        tabelaClassificacao = TabelaClassificacao()

        tabelaTimes = response.xpath('//table[@class="tabela-times"]')

        tabelaPontos = response.xpath('//table[@class="tabela-pontos"]')

        tabelaPontosLinha = tabelaPontos.xpath(
            './/tr[@class="tabela-body-linha"]')

        numeroLinha = 0
        for linha in tabelaTimes.xpath('.//tr[@class="tabela-body-linha"]'):

            posicao = linha.xpath(
                './/td[@class="tabela-times-posicao"]/text()').extract()

            time = linha.xpath(
                './/strong[@class="tabela-times-time-nome"]/text()').extract()

            variacao = linha.xpath(
                './/td[@class="tabela-times-variacao"]//span/text()').extract()

            sobeDesce = linha.xpath(
                './/td[@class="tabela-times-variacao"]')

            if (sobeDesce.xpath(
             './/span[contains(@class, "tabela-icone tabela-icone-positiva")]'
            ) != []):
                variacao[0] = int(variacao[0]) * -1

            itensTabela = []
            for pontosLinha in tabelaPontosLinha[numeroLinha].xpath(
                    './/td/text()'):
                itensTabela.append(pontosLinha.extract())

            numeroLinha = numeroLinha + 1

            tabelaClassificacao.setClassificacao(
                        posicao[0], time[0], variacao[0], itensTabela)

        yield GoodspyItem(
            classificacao=tabelaClassificacao.getClassificacao())

        # print(json.dumps(tabelaClassificacao.getClassificacao()))
