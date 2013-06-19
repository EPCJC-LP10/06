# -*- coding: utf-8 -*-

def principal():
    print"_______________/\_______________"
    print      " **** Testes ****** "
    print      " Escolha uma opcao"
    print "   1. Gestao de Perguntas"
    print
    print "   2. JOGAR"
    print
    print"--------------------------------"
    print
    print "   0. Sair" 
    print"________________________________"
    op = raw_input("Opçao: ")
    return op


def perguntas():
    print
    print " *** Menu Perguntas **** "
    print
    print "1. Inserir nova pergunta"
    print "2. Listar todos alunos"
    print "3. Pesquisar aluno"
    print "4. Alterar dados de um aluno"
    print "5. Eliminar aluno"
    print 
    print "0. Menu Anterior"
    op = raw_input("Opção: ")
    return op


def categorias():
    print
    print " Escolha a categoria "
    print
    print "1. Capitais"
    print "2. Futebol"
    
    op = raw_input("Opção: ")
    return op

if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"



