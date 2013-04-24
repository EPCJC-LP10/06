# -*- coding: utf-8 -*-

#
# Exemplo utilização de array de registos
# Os elementos da lista NÃO são mantidos ordenados
# (a inserção é feita depois da última posição anterior)
# © EPCJC
#

def menu():
    print
    print "1: Inserir novo contato"
    print "2: Listar todos os contatos"
    print "3: Alterar dados de um contato"
    print "4: Eliminar contato"
    print "5: Pesquisar  por código"
    
    print "0: Terminar"
    print

def posicao_livro(codigo):
    ''' Encontra a posicao onde se encontra o livro com o código recebido
    
        Pesquisa por um código de livro nos livros
        já inseridos. Se NÃO encontra o código, devolve o valor -1; 
        caso contrário, devolve a posicão do livro dentro da lista
        
    '''
    
    for pos in range(len(Livros)):
        if Livros[pos].codigo == codigo:
            return pos
                    
    return -1   # não encontrou
    
    

def inserir():
    codigo = input("Introduza código: ")
    posicao = posicao_livro(codigo)
    if posicao != -1:
        print("Código já existente.\n")
        return
    
    # ler os restantes dados do registo
    titulo = raw_input("Introduza titulo: ")
    ano = raw_input("Ano de lançamento: ")
    autor = raw_input("Introduza autor: ")
    
    
    # Criar o novo registo
    novo_registo = Livro(codigo, titulo, ano, autor)

    # Adicionar o registo à lista 
    Livros.append(novo_registo)
    
    
def apresentar_registo(registo):
        print "Código: ", registo.codigo
        print "Titulo: ", registo.titulo
        print "   Ano: ", registo.ano
        print " Autor: ", registo.autor
        print "-------------------------------"


def listar_todos():
    if len(Livros) == 0:
        print "Não existem livros inseridos"
        return

    for registo in Livros:
        apresentar_registo(registo)
        

#Outra maneira de fazer a listagem
def listar_todos_alternativa():
    if len(Livros) == 0:
        print "Não existem livros inseridos"
        return

    for i in range(len(Livros)):
        apresentar_registo(Livros[i])



def pesquisar():
    codigo = input("Introduza código do livro: ")
    posicao = posicao_livro(codigo)
    if posicao == -1:
        print "Esse código não existe."
        return

    apresentar_registo(Livros[posicao])
    
def alterar():
    codigo = input("Introduza código do livro: ")
    posicao = posicao_livro(codigo)
    if posicao == -1:
        print "Esse código não existe."
        return

    apresentar_registo(Livros[posicao])

    # A melhorar: perguntar qual o campo que se pretende alterar
    # Assim altera todos os campos com exceção do código

    #ler os novos dados
    novo_titulo = raw_input("Introduza novo titulo: ")
    novo_ano = raw_input("Novo ano de lançamento: ")
    novo_autor = raw_input("Introduza novo autor: ")
    

    # Substituir o registo
    Livros[posicao] = Livros[posicao]._replace(titulo=novo_titulo, 
    	ano=novo_ano, autor=novo_ano)

    
    
def eliminar():
    codigo = input("Introduza código do livro: ")
    posicao = posicao_livro(codigo)
    if posicao == -1:
        print "Esse código não existe."
        return

    apresentar_registo(Livros[posicao])
    opcao = raw_input("Tem a certeza que deseja eliminar este registo (S/N)? ")
    if opcao.lower() == "s":
        #eliminar registo na posição posicao
        Livros.pop(posicao)
        print "Registo eliminado"
    else:
        print "Registo não eliminado"





##################################

from collections import namedtuple

ContatoReg = namedtuple("ContatoReg", "codigo, nome, telefone")

Contatos = []
	
quero_sair = False
while not quero_sair:
    menu()
    op = raw_input("Introduza opção: ")
    if op == '1':
        inserir()           
    elif op == '2':
        listar_todos()		
    elif op == '3':
        alterar()
    elif op == '4':
        eliminar()
    elif op == '5':
        pesquisar()        # NAO ESTA FEITO
    elif op == '0': 
        quero_sair = True
    else:
		print "Opção inválida"
        
print 

