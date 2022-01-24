# -*- coding: UTF-8 -*-

from datetime import date


class Item(object):
    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor


class Nota_fiscal():
    def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes=''):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        self.__itens = itens
        self.__detalhes = detalhes
        if len(detalhes) > 20:
            raise Exception('Detalhes da nota não pode ter mais do que 20 caracteres.')

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_vencimento(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes


if __name__ == '__main__':
    itens = [
        Item(
            descricao='Item A',
            valor=100
        ),
        Item(
            descricao='Item B',
            valor=200
        )
    ]
    nota_fiscal = Nota_fiscal(
        razao_social='FHSA Limitada',
        cnpj='012345678901234',
        itens=itens,
        # data_de_emissao=date.today(),
        # detalhes='Referente à ...'
    )
