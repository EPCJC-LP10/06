11# -*- coding: utf-8 -*-

import menu
import perguntas
import jogar
import util


# nome dos ficheiros
fxPerguntas = "perguntas.dat"

def ler_ficheiros():
	# adicionar todos ficheiros a ler
	perguntas.listaPerguntas = util.ler_ficheiro(fxPerguntas)


def escrever_ficheiros():
	# adicionar todos ficheiros a guardar
	util.escrever_ficheiro(fxPerguntas, perguntas.listaPerguntas)



# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()
    
    if op == '1':
        perguntas.gerir()
    elif op == '2':
        jogar.gerir()
    elif op == '0':
        terminar = True


escrever_ficheiros()


