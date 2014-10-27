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

    def eliminar_transitividad(self, lista):
        cambio = False
        seguir = True
        while seguir:
            for i in lista:
                for j in lista:
                    if j[0] == i[1]:
                        i[1] = j[1]
                        lista.remove(j)
                        cambio = True
            if cambio:
                seguir = True
                cambio = False
            else:
                seguir = False

    def mapear(self, protochild, lista_m, pos_inicial, pos_final):
        for i in range(len(protochild)):
            if (i < pos_inicial) or (i > pos_final):
                for j in range(len(lista_m)):
                    if protochild[i] in lista_m[j]:
                        if protochild[i] == lista_m[j][0]:
                            protochild[i] = lista_m[j][1]
                        else:
                            protochild[i] = lista_m[j][0]
        return protochild

    def cruzar(self, cromosoma1, cromosoma2):
        lista_respuesta = []
        padre1_secuencia = cromosoma1.secuencia
        padre2_secuencia = cromosoma2.secuencia
        #Genero dos posiciones al azar teniendo en cuenta el tamano del cromo
        pos1 = random.randint(0, cromosoma1.tamano)
        pos2 = random.randint(0, cromosoma1.tamano)
        if pos1 >= pos2:
            pos_inicial = pos2
            pos_final = pos1
        else:
            pos_inicial = pos1
            pos_final = pos2
        #Intercambio substrings entre los padres
        #---------------------------------------
        #1) Armo Substrings
        substring1 = padre1_secuencia[pos_inicial:pos_final + 1]
        substring2 = padre2_secuencia[pos_inicial:pos_final + 1]
        #2)Armo Protochilds
        padre1_secuencia[pos_inicial:pos_final + 1] = substring2
        padre2_secuencia[pos_inicial:pos_final + 1] = substring1
        #3)Armo Lista de Mapeo con los substrings
        lista_mapeo = []
        for i in range(len(substring1)):
            lista_mapeo.append([substring1[i], substring2[i]])
        #4)Elimino Transitividad de la Lista de Mapeo
        self.eliminar_transitividad(lista_mapeo)
        #5)Reemplazo Final con Lista De Mapeo
        sec_hijo1 = self.mapear(padre1_secuencia, lista_mapeo, pos_inicial, pos_final)
        sec_hijo2 = self.mapear(padre2_secuencia, lista_mapeo, pos_inicial, pos_final)
        #6) Creo 2 hijos y les asigno la secuencia
        h1 = Cromosoma(cromosoma1.tamano)
        h2 = Cromosoma(cromosoma1.tamano)
        h1.secuencia = sec_hijo1
        h2.secuencia = sec_hijo2
        # QUE HACEMOS CON EL FITNESS ACÁ ????
        lista_respuesta.aappend(h1)
        lista_respuesta.aappend(h2)
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
