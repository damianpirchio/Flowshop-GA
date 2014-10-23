# -*- coding: utf-8 -*-

import random


class Poblacion(object):
    """docstring for Poblacion"""
    cromosomas = []

    def __init__(self, tamano=128):
        super(Poblacion, self).__init__()
        #self.cromosomas = cromosomas
        self.tamano = tamano

    def generar(self, tamano_cromosoma):
        """Genera Poblacion Inicial"""
        for i in range(self.tamano):
            cromosoma_actual = Cromosoma(tamano_cromosoma)
            cromosoma_actual.generar_secuencia()
            cromosoma_actual.evaluar_fitness()
            self.cromosomas.append(cromosoma_actual)

    def mostrar(self):
        for c in self.cromosomas:
            print c.secuencia
            print c.fitness
            print('----------------------')


class Cromosoma(object):
    fitness = 0
    secuencia = []

    def __init__(self, tamano):
        self.tamano = tamano

    def evaluar_fitness(self):
        self.fitness = random.randint(1, 100)

    def generar_secuencia(self):
        self.secuencia = [i for i in range(1, self.tamano + 1)]
        random.shuffle(self.secuencia)


class Selection(object):
    def __init__(self):
        pass


class PBT(Selection):
    """docstring for Probabilistic Binary Tournament"""
    def __init__(self):
        super(PBT, self).__init__()
        #def Seleccionar(self):


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
