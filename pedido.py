# -*- coding: UTF-8 -*-

from datetime import date


class Pedido():
    def __init__(self, cliente, valor):
        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_finalizacao = None

    def paga(self):
        self.__pago = 'PAGO'

    def finaliza(self):
        self.__data_finalizacao = date.today()

    @property
    def cliente(self):
        return self.__cliente

    @property
    def valor(self):
        return self.__valor

    @property
    def status(self):
        return self.__status

    @property
    def data_finalizaca(self):
        return self.__data_finalizacao


from abc import ABCMeta, abstractmethod


class Comando():
    __metaclass__ = ABCMeta

    @abstractmethod
    def executa(self):
        pass


class Conclui_pedido(Comando):
    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.finaliza()


class Paga_pedido(Comando):
    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.paga()


class Fila_de_trabalho():
    def __init__(self):
        self.__comandos = []

    def adiciona(self, comando):
        self.__comandos.append(comando)

    def processa(self):
        for comando in self.__comandos:
            comando.executa()


if __name__ == '__main__':
    pedido1 = Pedido('Gilmar', 200)
    pedido2 = Pedido('Renata', 400)

    fila_de_trabalho = Fila_de_trabalho()

    comando1 = Conclui_pedido(pedido1)
    comando2 = Paga_pedido(pedido1)
    comando3 = Conclui_pedido(pedido2)

    fila_de_trabalho.adiciona(comando1)
    fila_de_trabalho.adiciona(comando2)
    fila_de_trabalho.adiciona(comando3)

    fila_de_trabalho.processa()
