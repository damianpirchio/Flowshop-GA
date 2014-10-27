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

    def evaluar_fitness2(self, datos):
        lista = self.secuencia
        resu = 0
        while len(lista) > 0:
            job = lista[0]
            for sub_lista in datos:
                resu = resu + datos[sub_lista[job]]
            lista.remove(job)
        self.fitness = resu

    def generar_secuencia(self):
        self.secuencia = [i for i in range(0, self.tamano)]
        random.shuffle(self.secuencia)


class Selection(object):
    def __init__(self):
        pass


class PBT(Selection):
    """docstring for Probabilistic Binary Tournament"""
    def __init__(self):
        super(PBT, self).__init__()

    def seleccionar(self, cromosoma1, cromosoma2):
        probabilidad = random.randint(1, 100)
        if probabilidad < 66:
            #Tomo el mejor fitness
            if cromosoma1.fitness >= cromosoma2.fitness:
                rta = cromosoma1
            else:
                rta = cromosoma2
        else:
            #Tomo el peor fitness
            if cromosoma1.fitness >= cromosoma2.fitness:
                rta = cromosoma2
            else:
                rta = cromosoma1
        return rta


class Crossover(object):
    """docstring for Crossover"""
    def __init__(self):
        super(Crossover, self).__init__()


class PMX(Crossover):
    """docstring for PMX"""
    def __init__(self):
        super(PMX, self).__init__()

    def cruzar(self, cromosoma1, cromosoma2):
        lista_respuesta = []
        padre1_secuencia = cromosoma1.secuencia
        print("padre1: " + str(padre1_secuencia))
        padre2_secuencia = cromosoma2.secuencia
        print("padre2: " + str(padre2_secuencia))
        #Genero dos posiciones al azar teniendo en cuenta el tamano del cromo
        #pos1 = random.randint(0, cromosoma1.tamano)
        #pos2 = random.randint(0, cromosoma1.tamano)
        pos1 = 2
        pos2 = 6
        if pos1 >= pos2:
            pos_inicial = pos2
            pos_final = pos1
        else:
            pos_inicial = pos1
            pos_final = pos2
        print("pos inicial: " + str(pos_inicial))
        print("pos final: " + str(pos_final))
        #Intercambio substrings entre los padres
        #---------------------------------------
        #1) Armo Substrings
        substring1 = padre1_secuencia[pos_inicial:pos_final]
        substring2 = padre2_secuencia[pos_inicial:pos_final]
        print("Substring 1: " + str(substring1))
        print("Substring 2: " + str(substring2))
        #2)Armo Protochilds
        padre1_secuencia[pos_inicial:pos_final] = substring2
        padre2_secuencia[pos_inicial:pos_final] = substring1
        print("protochild 1: " + str(padre1_secuencia))
        print("protochild 2: " + str(padre2_secuencia))
        #3)Armo Lista de Mapeo con los substrings
        lista_mapeo = []
        for i in range(len(substring1)):
            lista_mapeo.append([substring1[i], substring2[i]])
        print("lista de mapeo: " + str(lista_mapeo))
        #4)Elimino Transitividad de la Lista de Mapeo
        #5)Reemplazo Final con Lista De Mapeo
        #for el in padre1_secuencia:
            #if el not in substring1:

        return lista_respuesta


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
