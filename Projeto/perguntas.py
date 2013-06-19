# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


perguntaReg = namedtuple("perguntaReg", "id, categoria, enunciado, hip1, hip2, hip3, certa")
listaPerguntas = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaPerguntas)):
        if listaPerguntas[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir():
    cod = input("Qual o codigo? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "C�digo j� existe"
        return

    #ler dados
    print "Introduza categoria:"
    print "1. Capitais"
    print "2. Futebol"
    print
    categoria = raw_input("Qual a categoria? ")
    
    
    enunciado = raw_input ("        Enunciado da Pergunta: ")
    hip1 = raw_input      ("Primeira hip�tese de resposta: ")
    hip2 = raw_input      (" Segunda hip�tese de resposta: ")
    hip3 = raw_input      ("Terceira hip�tese de resposta: ")
    print
    certa = raw_input("Qual a hip�tese correta ( 1 / 2 / 3 ): ")
    
    registo = perguntaReg(cod, categoria, enunciado, hip1, hip2, hip3, certa)
    listaPerguntas.append(registo)


def pesquisar_aluno():
    cod = input("Qual o codigo do aluno a pesquisar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "N�o existe aluno com esse c�digo"
        return

    print "C�digo: ", listaPerguntas[pos].id
    print "Nome: ", listaPerguntas[pos].nome
    


def listar():
    for i in range (len(listaPerguntas)):
        print "C�digo: ", listaPerguntas[i].id
        if listaPerguntas[i].categoria == 1:
            print "Categoria: Capitais"
        else:
            print "Categoria: Futebol"
        print "\t", listaPerguntas[i].enunciado
        print "\t\t1: ", listaPerguntas[i].hip1
        print "\t\t2: ", listaPerguntas[i].hip2
        print "\t\t3: ", listaPerguntas[i].hip3
        print "\tHip�tese correta: ", listaPerguntas[i].certa
        
  

def eliminar_aluno():
    cod = input ("C�digo do aluno a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "N�o existe aluno com esse c�digo"
        return

    # TODO: Confirmar elimina��o
    listaPerguntas.pop(pos)


    
def alterar_aluno():
    cod = input ("C�digo do aluno a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "N�o existe aluno com esse c�digo"
        return

    # s� altera o nome
    novonome = raw_input("Qual o nome? ")
    listaPerguntas[pos] = listaPerguntas[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.perguntas()

        if op == '1':
            inserir()
        elif op =='2':
            listar()
        elif op == '3':
            pesquisar_aluno()
        elif op == '4':
            alterar_aluno()
        elif op == '5':
            eliminar_aluno()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa n�o deve ser executado diretamente"
