# -*- coding: utf-8 -*-

import random
import copy


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
            print (c.secuencia)
            print (c.fitness)
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
        #Tomo el mejor fitness
        if cromosoma1.fitness >= cromosoma2.fitness:
            rta = cromosoma1
        else:
            rta = cromosoma2
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
        lista_respuesta.append(h1)
        lista_respuesta.append(h2)
        return lista_respuesta


class CX(Crossover):
    """docstring for CX"""
    def __init__(self):
        super(CX, self).__init__()

    def esta_en_lista(self, elemento, lista):
        """Devuelve verdadero si un elemento pertenece a una lista de listas"""
        rta = False
        for sublista in lista:
            if elemento in sublista:
                rta = True
        return rta

    def armar_ciclo(self, pos, cromosoma1, cromosoma2):
        """Funcion que encuentra el ciclo (en caso de existir )para
        el elemnto de la posicion recibida y agrega ese ciclo a la lista
        de ciclos"""

        # Setea el valor inicial para el corte
        inicio_ciclo = cromosoma1[pos]
        ciclo = []
        i = pos
        seguir = True
        # Recorre el cromosoma1
        while seguir:
            valor2 = cromosoma2[i]
            ciclo.append(i)
            for j in range(len(cromosoma1)):
                if cromosoma1[j] == valor2:
                    i = j
            if cromosoma2[i] == inicio_ciclo:
                ciclo.append(i)
                seguir = False
        return ciclo

    def generar_hijos(self, lista_ciclos, padre1, padre2):
        lista_hijos = []
        print ("lista ciclos" + str(lista_ciclos))
        if len(lista_ciclos) == 1:
            h1 = Cromosoma(len(padre1))
            h2 = Cromosoma(len(padre1))
            h1.secuencia = padre1
            h2.secuencia = padre2
            lista_hijos.append(h1)
            lista_hijos.append(h2)
        else:
            for i in range(0, 2):
                ciclo_actual = lista_ciclos[i]
                hijo = Cromosoma(len(padre1))
                hijo.secuencia = copy.deepcopy(padre2)
                #print "hijo secuencia = " + str(hijo.secuencia)
                for j in range(hijo.tamano):
                    if j in ciclo_actual:
                        hijo.secuencia[j] = padre1[j]

                lista_hijos.append(hijo)
            """
            ciclo1 = lista_ciclos[0]
            print "ciclo1" + str(ciclo1)
            ciclo2 = lista_ciclos[1]
            print "ciclo2" + str(ciclo2)
            hijo1 = Cromosoma(len(padre1))
            print "padre2 1 vez: " + str(padre2)
            hijo1.secuencia = copy.deepcopy(padre2)
            print "padre2 2 vez: " + str(padre2)
            print "hijo1 secuencia inicial: " + str(hijo1.secuencia)
            for j in range(hijo1.tamano):
                print "padre 2 for 1: " + str(padre2)
                if j in ciclo1:
                    hijo1.secuencia[j] = padre1[j]

            hijo2 = Cromosoma(len(padre1))
            print "padre2 3 vez: " + str(padre2)
            hijo2.secuencia = copy.deepcopy(padre2)
            print "padre2 4 vez: " + str(padre2)
            print "hijo2 secuencia inicial: " + str(hijo2.secuencia)
            for k in range(hijo2.tamano):
                if k in ciclo2:
                    hijo2.secuencia[k] = padre1[k]
        print "hijo1 secuencia final: " + str(hijo1.secuencia)
        print "hijo2 secuencia final: " + str(hijo2.secuencia)
        lista_hijos.append(hijo1.secuencia)
        lista_hijos.append(hijo2.secuencia)
        """
        #print "lista hijos: " + str(lista_hijos)
        return lista_hijos

    def buscar_ciclos(self, cromosoma1, cromosoma2):
        """ Esta funcion arma una lista de listas donde cada sublista
        esta formada, por las posiciones de los elementos que forman
        parte de un ciclo.De esta manera obtendremos:
        [[p1c1,p2c1,pnc1],[p1c2,p2c2,pnc2],....,[p1cn,p2cn,pncn]]
        Donde pncn representa la posición n del ciclo n
        """
        lista_ciclos = []
        for i in range(len(cromosoma1)):
            if cromosoma2[i] != cromosoma1[i]:
                if not self.esta_en_lista(i, lista_ciclos):
                    c = self.armar_ciclo(i, cromosoma1, cromosoma2)
                    lista_ciclos.append(c)
        return lista_ciclos

    def cruzar(self, cromosoma1, cromosoma2):
        lista_rta = []
        #Reviso que los padres sean diferentes
        if cromosoma1.secuencia != cromosoma2.secuencia:
            #Busco ciclos entre los dos padres
            lista_ciclos = self.buscar_ciclos(cromosoma1.secuencia,
            cromosoma2.secuencia)
            lista_rta = self.generar_hijos(lista_ciclos, cromosoma1.secuencia,
            cromosoma2.secuencia)
        # Si los padres son iguales los hijos iguales
        else:
            h1 = Cromosoma(cromosoma1.tamano)
            h2 = Cromosoma(cromosoma1.tamano)
            h1.secuencia = cromosoma1.secuencia
            h2.secuencia = cromosoma1.secuencia
            lista_rta.append(h1)
            lista_rta.append(h2)
        return lista_rta


class Mutation(object):
    """docstring for Mutation"""
    def __init__(self):
        pass

    def mutar():
        pass


class Invertion(Mutation):
    """This is a very simple mutation operator.
    Select two random points (i.e.; positions 2 through 5)
    and reverse the genes between them.

    0 1 2 3 4 5 6 7

    becomes

    0 4 3 2 1 5 6 7

    """
    def __init__(self):
        super(Invertion, self).__init__()

    def mutar(self, cromosoma):
        pos1 = random.randint(0, cromosoma.tamano - 1)
        pos2 = random.randint(0, cromosoma.tamano - 1)
        if pos1 < pos2:
            revlist = cromosoma.secuencia[pos1:pos2 + 1]
            revlist = revlist[::-1]
            cromosoma.secuencia[pos1:pos2 + 1] = revlist
        else:
            revlist = cromosoma.secuencia[pos2:pos1 + 1]
            revlist = revlist[::-1]
            cromosoma.secuencia[pos2:pos1 + 1] = revlist
        return None


class Displacement(Mutation):
    """Select two random points (i.e.; positions 4 and 6),
    grab the genes between them as a group, then reinsert
    the group at a random position displaced from the original.

    0 1 2 3 4 5 6 7

    becomes

    0 3 4 5 1 2 6 7
    """
    def __init__(self):
        super(Displacement, self).__init__()

    def mutar(self, cromosoma):
        pos1 = random.randint(0, cromosoma.tamano - 1)
        pos2 = random.randint(0, cromosoma.tamano - 1)
        if pos1 < pos2:
            group = cromosoma.secuencia[pos1:pos2 + 1]
            del(cromosoma.secuencia[pos1:pos2 + 1])
            randpos = random.randint(0, len(cromosoma.secuencia))
            cromosoma.secuencia.insert(randpos, group)
        if pos2 < pos1:
            group = cromosoma.secuencia[pos2:pos1 + 1]
            del(cromosoma.secuencia[pos2:pos1 + 1])
            randpos = random.randint(0, len(cromosoma.secuencia))
            cromosoma.secuencia.insert(randpos, group)
        cromosoma.secuencia = list(flatten(cromosoma.secuencia))
        return None


def flatten(*args):
    for x in args:
        if hasattr(x, '__iter__'):
            for y in flatten(*x):
                yield y
        else:
            yield x