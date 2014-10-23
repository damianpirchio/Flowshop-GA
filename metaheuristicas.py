# -*- coding: utf-8 -*-

import random

class Poblacion(object):
	"""docstring for Poblacion"""
	cromosomas = []
	def __init__(self, tamano = 128):
		super(Poblacion, self).__init__()
		#self.cromosomas = cromosomas
		self.tamano = tamano


	def generar(self):
		"""Genera Poblacion Inicial"""
		pass

class Cromosoma(object):
	fitness = 0
	secuencia = []
	def __init__(self, tamano):
		self.tamano = tamano

	def evaluar(self):
		return self.fitness
	def generar_secuencia(self):
		self.secuencia = [i for i in range(1, self.tamano + 1) ]
		random.shuffle(self.secuencia)

class Gen(object):
	def __init__(self):
		pass

class Selection(object):
	def __init__(self):
		pass

class Roulette(Selection):
	"""docstring for Roulette"""
	def __init__(self, arg):
		super(Roulette, self).__init__()
		self.arg = arg
		
class Crossover(object):
			"""docstring for Crossover"""
			def __init__(self, arg):
				super(Crossover, self).__init__()
				self.arg = arg

class PMX(Crossover):
	"""docstring for PMX"""
	def __init__(self, arg):
		super(PMX, self).__init__()
		self.arg = arg
		
class CX(Crossover):
	"""docstring for CX"""
	def __init__(self, arg):
		super(CX, self).__init__()
		self.arg = arg

class Mutation(object):
	"""docstring for Mutation"""
	def __init__(self, arg):
		self.arg = arg

class Invertion(Mutation):
	"""docstring for Invertion"""
	def __init__(self, arg):
		super(Invertion, self).__init__()
		self.arg = arg

class Displacement(Mutation):
	"""docstring for Displacement"""
	def __init__(self, arg):
		super(Displacement, self).__init__()
		self.arg = arg
		
						