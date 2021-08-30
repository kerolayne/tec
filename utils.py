from pathlib import Path
class ControleMT:
    def __init__(self,tipoMT, estados, operacao):
        self.tipoMT = tipoMT
        self.estados = estados
        self.operacao = operacao
        self.estadoInicial = "0"

class Operador:
    def __init__(self, estadoAtual, simbVisitado, novoSimb, direcao, novoEstado):
        self.estadoAtual = estadoAtual
        self.simbVisitado = simbVisitado
        self.novoSimb = novoSimb
        self.direcao = direcao
        self.novoEstado = novoEstado