# -*- coding: utf-8 -*-

#from ..geneticos import metaheuristicas
from metaheuristicas import *
import random
import sys

## ESQUEMA DE REPRESENTACION

""" 3 maquinas y 3 trabajos 

      m1      m2	m3
t1    14      23    34            
t2    16      12 	10
t3    23      7		29


datos [[j1], [j2], [j3] ]

datos = [[j1m1, j1m2, j1m3], [j2m1, j2m2, j2m3], [j3m1, j3m2, j3m3]]


datos = [[14, 23, 34], [16, 12, 10], [23, 7, 29]]

"""

#posibles_secuencias = [123, 132, 213, 231, 312, 321]

class Problema(object):
    """docstring for Problema"""
     
    
    datos = []
    jobs = 0
    maquinas = 0
    upper_bound = 0
    lower_bound = 0
    max_iterations = 500

    def __init__(self):
        super(Problema, self).__init__()
        
        


    def parsear(self, archivo):

        """ Toma la entrada de Tailard y la transforma en algo con el formato lista de listas
            que podamos utilizar """
    	
        
        with open(archivo, "r") as f:

            lines = map(str.strip, f.readlines())
            data = [map(int, line.split()) for line in lines]
        
        info = data.pop(0)
        self.jobs = info[0]
        self.maquinas = info[1]
        self.upper_bound = info[2]
        self.lower_bound = info[3]

        


        return data	

def evaluar_fitness(cromosoma):
    cromosoma.fitness = random.randint(1, 100)


#def evolucionar():

#def resolver():

if __name__ == "__main__":      

    problema = Problema()

    if len(sys.argv) == 2:
        problema.datos = problema.parsear(sys.argv[1])
    else:
        print "\nUsage: python flow.py <Taillard problem file> [<instance number>]\n"
        sys.exit(0)

    # ---- Variables---------
    
    
    print problema.jobs  
    print problema.maquinas  
    print problema.upper_bound  
    print problema.lower_bound
    print problema.max_iterations

    #-----------  GENERACIÓN POBLACIÓN INICIAL  ---------- 
      
    poblacion_inicial = Poblacion()
    print ('Tamano de la poblacion inicial: %d ') % poblacion_inicial.tamano
      
    # Debería venir de la cant de jobs del parseo de tailard
    tamano_cromosoma = problema.jobs
    for i in range(poblacion_inicial.tamano):
        cromosoma_actual = Cromosoma(tamano_cromosoma)
        cromosoma_actual.generar_secuencia()
        evaluar_fitness(cromosoma_actual)
        poblacion_inicial.cromosomas.append(cromosoma_actual) 
      	print cromosoma_actual.fitness

    #print poblacion_inicial.cromosomas[13].secuencia

    #while i < max_iterations:
        #pass




      #-----------  CROSSOVER  ----------



      #-----------  MUTACIÓN  ----------




      #-----------  REEMPLAZO  ----------


