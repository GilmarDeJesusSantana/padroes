# -*- coding: UTF-8 -*-
from orcamentos import Orcamentos, Item
from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhetos_reais, Sem_desconto


class Calculador_de_descontos(object):
    def calcula(self, orcamento):
        desconto = Desconto_por_cinco_itens(Desconto_por_mais_de_quinhetos_reais(Sem_desconto())).calcula(orcamento)

        return desconto


if __name__ == '__main__':
    orcamento = Orcamentos()
    orcamento.adiciona_item(Item('Item -1', 100))
    orcamento.adiciona_item(Item('Item -2', 100))
    orcamento.adiciona_item(Item('Item -3', 100))
    orcamento.adiciona_item(Item('Item -3', 100))
    orcamento.adiciona_item(Item('Item -3', 100))
    orcamento.adiciona_item(Item('Item -3', 100))
    orcamento.adiciona_item(Item('Item -3', 100))
    orcamento.adiciona_item(Item('Item -3', 100))
    orcamento.adiciona_item(Item('Item -3', 100))
    orcamento.adiciona_item(Item('Item -3', 100))
    orcamento.adiciona_item(Item('Item -3', 100))

    calculador = Calculador_de_descontos()
    desconto = calculador.calcula(orcamento)
    print(f'Desconto calculado {desconto}')
