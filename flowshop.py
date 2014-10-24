# -*- coding: utf-8 -*-

#from ..geneticos import metaheuristicas
from metaheuristicas import *
import sys

## ESQUEMA DE REPRESENTACION

""" 3 maquinas y 3 trabajos

      m1      m2    m3
t1    14      23    34
t2    16      12    10
t3    23      07    29


datos [[j1], [j2], [j3] ]

datos = [[j1m1, j1m2, j1m3], [j2m1, j2m2, j2m3], [j3m1, j3m2, j3m3]]


datos = [[14, 23, 34], [16, 12, 10], [23, 7, 29]]

"""


class Problema(object):
    """docstring for Problema"""

    datos = []
    jobs = 0
    maquinas = 0
    upper_bound = 0
    lower_bound = 0
    max_iterations = 500

    seleccion = None
    padres = None
    hijos = None
    hijos_mutados = None

    def __init__(self):
        super(Problema, self).__init__()

    def parsear(self, archivo):
        """ Toma la entrada de Tailard y la transforma en algo
        con el formato lista de listas que podamos utilizar """

        with open(archivo, "r") as f:

            lines = map(str.strip, f.readlines())
            data = [map(int, line.split()) for line in lines]

        info = data.pop(0)
        self.jobs = info[0]
        self.maquinas = info[1]
        self.upper_bound = info[2]
        self.lower_bound = info[3]

        return data

    def evolucionar():
        #-----------  SELECCION -----------
        pbt = PBT()
        self.seleccion = pbt.seleccionar()  # Devuelve un cromosoma

        #-----------  CROSSOVER  ----------

        #-----------  MUTACIÓN  ----------

        #-----------  REEMPLAZO  ----------
        pass

    def resolver():

        problema = self

        if len(sys.argv) == 2:
            problema.datos = problema.parsear(sys.argv[1])
        else:
            print "\nUsage: python flow.py <Taillard problem file>\n"
            sys.exit(0)

        #-----------  GENERACIÓN POBLACIÓN INICIAL  ----------

        poblacion_inicial = Poblacion()
        poblacion_inicial.generar(problema.jobs)
        poblacion_inicial.mostrar()

        self.padres = Poblacion()
        self.hijos = Poblacion()
        self.hijos_mutados = Poblacion()

        iteracion = 0
        while iteracion < max_iterations:
            evolucionar()
            iteracion += 1

if __name__ == "__main__":
    p = Problema()
    p.resolver()