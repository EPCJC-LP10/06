# -*- coding: utf-8 -*-

def principal():
    print
    print " **** MENU ****** "
    print
    print "   1. Gestão de Alunos"
    print "   2. Registar Presença (não implementado)"
    print 
    print "   0. Sair"
    print 

    op = raw_input("Opção: ")
  
    return op


def alunos():
    print
    print " *** Menu Alunos **** "
    print
    print "1. Inserir novo aluno"
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
    
    op = raw_input("Opcão: ")
    return op


if __name__ == "__main__":
    print "Este programa nao deve ser executado diretamente"


