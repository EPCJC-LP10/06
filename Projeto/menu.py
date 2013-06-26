# -*- coding: utf-8 -*-

def principal():
    print"_______________/\_______________"
    print      " **** Testes ****** "
    print      " Escolha uma opcao"
    print "   1. Gestao de Perguntas"
    print
    print "   2. JOGAR"  
    print "                               "  


    op = raw_input("Opçao: ")
  
    return op


def perguntas():
    print
    print " *** Menu Perguntas **** "
    print
    print "1. Inserir nova Pergunta"
    print "2. Listar todos perguntas"
    print "3. Pesquisar perguntas"
    print "4. Alterar "
    print "5. Eliminar pergunta"
    print 
    print "0. Menu Anterior"

    op = raw_input("Opçao: ")
    return op


def categorias():
    print
    print " Escolha a categoria "
    print
    print "1. Capitais"
    print "2. Futebol"
    
    op = raw_input("Opcão: ")
    return op


if __name__ == "__main__":
    print "Este programa nao deve ser executado diretamente"


