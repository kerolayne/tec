from pathlib import Path
from utils import *
import sys
Operador_lista = list()
#inicia a fita com £ (s_to_I)
def StoI(maquinaTuring):
    maquinaTuring.tipoMT = "I"
    #muda o número do estado com 1 para criar um novo estado 0 que prepara a fita
    for op in maquinaTuring.operacao:
        op.estadoAtual = op.estadoAtual + "1"
        op.novoEstado = op.novoEstado + "1"
    novoEstado = list()
    for estado in maquinaTuring.estados:
        novoEstado.append(estado + "1")
    maquinaTuring.estados = novoEstado
    for estado in maquinaTuring.estados:
        maquinaTuring.operacao.append(Operador(estado,"§","§","r",estado))
    maquinaTuring.operacao.insert(0,Operador(0,"*","*","l","step"))
    maquinaTuring.operacao.insert(1,Operador("step","_","§","r",maquinaTuring.estadoInicial+"1")) 
    return maquinaTuring
#trata o I_to_S    
def ItoS(maquinaTuring):
    maquinaTuring.tipoMT = "S"
    for op in maquinaTuring.operacao:
        op.estadoAtual = op.estadoAtual + "1"
        op.novoEstado = op.novoEstado + "1"
    novoEstado = list()
    for estado in maquinaTuring.estados:
        novoEstado.append(estado + "1")
    maquinaTuring.estados = novoEstado
    #parte1: idetifica estados de acordo com a informação lida
    maquinaTuring.operacao.insert(0,Operador(0,"1","§","r","step1")) 
    maquinaTuring.operacao.insert(1,Operador(0,"0","§","r","step2")) 
    maquinaTuring.operacao.insert(2,Operador("step1","1","_","l","step3")) 
    maquinaTuring.operacao.insert(3,Operador("step1","0","_","l","step4")) 
    maquinaTuring.operacao.insert(4,Operador("step2","1","_","l","step5")) 
    maquinaTuring.operacao.insert(5,Operador("step2","0","_","l","step6")) 
    maquinaTuring.operacao.insert(6,Operador("step3","§","§","r","step3")) 
    maquinaTuring.operacao.insert(7,Operador("step3","_","_","r","step3")) 
    maquinaTuring.operacao.insert(8,Operador("step3","1","1","r","step7")) 
    maquinaTuring.operacao.insert(9,Operador("step3","0","1","r","step8")) 
    maquinaTuring.operacao.insert(10,Operador("step4","§","§","r","step4")) 
    maquinaTuring.operacao.insert(11,Operador("step4","_","_","r","step4")) 
    maquinaTuring.operacao.insert(12,Operador("step4","1","1","r","step9")) 
    maquinaTuring.operacao.insert(13,Operador("step4","0","1","r","step10")) 
    maquinaTuring.operacao.insert(14,Operador("step5","§","§","r","step5")) 
    maquinaTuring.operacao.insert(15,Operador("step5","_","_","r","step5")) 
    maquinaTuring.operacao.insert(16,Operador("step5","1","0","r","step7")) 
    maquinaTuring.operacao.insert(17,Operador("step5","0","0","r","step8")) 
    maquinaTuring.operacao.insert(18,Operador("step6","§","§","r","step6")) 
    maquinaTuring.operacao.insert(19,Operador("step6","_","_","r","step6")) 
    maquinaTuring.operacao.insert(20,Operador("step6","1","0","r","step9")) 
    maquinaTuring.operacao.insert(21,Operador("step6","0","0","r","step10")) 
    maquinaTuring.operacao.insert(22,Operador("step7","_","1","r","step11")) 
    maquinaTuring.operacao.insert(23,Operador("step7","1","1","r","step7")) 
    maquinaTuring.operacao.insert(24,Operador("step7","0","1","r","step8")) 
    maquinaTuring.operacao.insert(25,Operador("step8","_","1","r","step12")) 
    maquinaTuring.operacao.insert(26,Operador("step8","1","1","r","step9")) 
    maquinaTuring.operacao.insert(27,Operador("step8","0","1","r","step10")) 
    maquinaTuring.operacao.insert(28,Operador("step9","_","0","r","step11")) 
    maquinaTuring.operacao.insert(29,Operador("step9","1","0","r","step7")) 
    maquinaTuring.operacao.insert(30,Operador("step9","0","0","r","step8")) 
    maquinaTuring.operacao.insert(31,Operador("step10","_","0","r","step12")) 
    maquinaTuring.operacao.insert(32,Operador("step10","1","0","r","step9")) 
    maquinaTuring.operacao.insert(33,Operador("step10","0","0","r","step10")) 
    maquinaTuring.operacao.insert(34,Operador("step11","_","1","l","step13")) 
    maquinaTuring.operacao.insert(35,Operador("step12","_","0","l","step13")) 
    maquinaTuring.operacao.insert(36,Operador("step13","*","*","l","step13")) 
    maquinaTuring.operacao.insert(37,Operador("step13","_","_","r",maquinaTuring.estadoInicial+"1")) 
    #Retorna ao estado inicial
    #------------------------------------------------------------------------
    #Parte 2: verifica cada estado, caso de ler £ então move para a direita
    for estado in maquinaTuring.estados:
        maquinaTuring.operacao.append(Operador(estado,"§","§","r",str(estado)+"subr"))
        maquinaTuring.operacao.append(Operador(str(estado)+"subr","_","_","r",str(estado)+"subr"))
        maquinaTuring.operacao.append(Operador(str(estado)+"subr","1","_","r",str(estado)+"subr1")) 
        maquinaTuring.operacao.append(Operador(str(estado)+"subr","0","_","r",str(estado)+"subr2")) 
        maquinaTuring.operacao.append(Operador(str(estado)+"subr1","1","1","r",str(estado)+"subr1")) 
        maquinaTuring.operacao.append(Operador(str(estado)+"subr1","0","1","r",str(estado)+"subr2")) 
        maquinaTuring.operacao.append(Operador(str(estado)+"subr1","_","1","r",str(estado)+"subr3")) 
        maquinaTuring.operacao.append(Operador(str(estado)+"subr2","1","0","r",str(estado)+"subr1")) 
        maquinaTuring.operacao.append(Operador(str(estado)+"subr2","0","0","r",str(estado)+"subr2")) 
        maquinaTuring.operacao.append(Operador(str(estado)+"subr2","_","0","r",str(estado)+"subr3")) 
        maquinaTuring.operacao.append(Operador(str(estado)+"subr3","*","*","l",str(estado)+"subr3")) 
        maquinaTuring.operacao.append(Operador(str(estado)+"subr3","§","§","r",estado)) 
    return maquinaTuring

if __name__ == "__main__":

    tipoMT ="I"
    file_directory = Path("base/")
    for current_file in file_directory.iterdir():
        if current_file.is_file():
            with open(current_file, 'r') as data_file:
                linha = [linha[:-1] for linha in data_file]
                for linha in linha:
                    if linha[0] == ';':
                        tipoMT = linha[1]
                    else:
                        linha_arquivo = [x for x in linha.split(" ")]
                        Operador_lista.append(Operador(linha_arquivo[0],linha_arquivo[1],linha_arquivo[2],linha_arquivo[3],linha_arquivo[4]))
                estados = set([x.estadoAtual for x in Operador_lista])
                maquinaTuring = ControleMT(tipoMT, estados, Operador_lista)
                if(maquinaTuring.tipoMT == "I"):
                    novaMT = ItoS(maquinaTuring)
                elif(maquinaTuring.tipoMT == "S"):
                    novaMT = StoI(maquinaTuring)
                else:
                    print("Não é uma maquina de turing sipser pu duplamente infinita!!!!!!!!!!!!!!!!!!!!!!!")
                with open(current_file.name.split(".")[0] + "_new" + "." + current_file.name.split(".")[1], 'w') as novoArquivo:
                    sys.stdout = novoArquivo
                    for op in novaMT.operacao:
                        print(str(op.estadoAtual) + " " + str(op.simbVisitado) + " " + str(op.novoSimb) + " " + str(op.direcao) + " " + str(op.novoEstado))
                Operador_lista.clear()