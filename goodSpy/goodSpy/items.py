# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoodspyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    classificacao = scrapy.Field()


class TabelaClassificacao(object):
    classificacao = []

    def __init__(self):
        pass

    def setClassificacao(self, posicao, time, variacao, itensTabela):

        self.classificacao.append({
            "posicao": posicao,
            "time": time,
            "variacao": variacao,
            "pontos_ganhos": itensTabela[0],    # Pontos
            "numero_jogos": itensTabela[1],     # Jogos
            "numero_vitorias": itensTabela[2],  # Vitorias
            "numero_empates": itensTabela[3],   # Empates
            "gols_pro": itensTabela[4],         # Gols Pro
            "gols_contra": itensTabela[5],      # Gols Contra
            "saldo_gols": itensTabela[6],       # Saldo e Gols
            "aproveitamento": itensTabela[7]    # Aproveitamento
        })

    def getClassificacao(self):
        #  classificacao = {"classificacao": self.classificacao}
        return self.classificacao
