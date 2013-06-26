# -*- coding: utf-8 -*-

import pickle

def ler_ficheiro(ficheiro):
	lista = []
	try:
		f = open(ficheiro, "rb")
		lista = pickle.load(f)		
		f.close
	except:
<<<<<<< HEAD
		print "Ficheiro %s não existe!" % (ficheiro)
=======
		print "Ficheiro %s nao existe!" % (ficheiro)
>>>>>>> 7ac8ecabc138a778ec054bf187668b24e2288c5f

	return lista


def escrever_ficheiro(ficheiro, lista):
	try:
		f = open(ficheiro, "wb")
		pickle.dump(lista, f)		
		f.close
		print "Escrevi ficheiro %s" % (ficheiro)
	except:
		print "Erro a gravar ficheiro %s!" % (ficheiro)
