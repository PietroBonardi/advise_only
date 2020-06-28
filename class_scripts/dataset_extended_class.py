#creo una classe con tutto il necessario per l'operazione di 
#feature ranking
import numpy as np
import pandas as pd 
import math
class dataframe_ext:
    #attributi: 
    #   - dataframe df
    #   - matrice delle distanze D
    #   - matrice delle similarità S
    #   - parametro similarità alpha
    #   - valore di entropia (float) E

    #########################################
    # COSTRUTTORE - easy                    #
    #########################################
    def __init__(self, dataframe):
        self.df = dataframe
        self.D = None
        self.S = None
        self.alpha = None
        self.E = None

    #########################################
    # DETERMINA TUTTI I PARAMETRI           #
    # -chiama nel giusto ordine i metodi    # 
    #########################################
    def complete(self):                       
        self.dist_matrix()
        self.set_alpha()
        self.sim_matrix()
        self.simmatrix_entropy()

    #########################################
    #   METODI - chiamati in complete       #
    #########################################
    #funzione per il calcolo di distanza 
    #fra istanze
    @staticmethod 
    def dist_measure(x1, x2):
        return np.linalg.norm(x1 - x2)

    #funzione per il calcolo della matrice 
    #delle distanze
    def dist_matrix(self):
        #se il dataframe viene da un sample
        #funziona comunque
        df = self.df.reset_index(drop = True)
        self.D =[
                    [
                        self.dist_measure(row1, row2) 
                        for _, row1 in df.iterrows()
                    ]
                    for _, row2 in df.iterrows()
                ]
        self.D = np.asmatrix(self.D)
    
    #funzione per il calcolo di alpha
    #richiede D
    def set_alpha(self):
        self.alpha = -math.log(0.5) / np.matrix.mean(self.D)

    #converte una distanza in similarità 
    #richiede alpha
    def sim(self, dist_value):
        return math.exp(- self.alpha * dist_value)

    #funzione per il calcolo della matrice 
    #delle similarità (richiede D e alpha)
    def sim_matrix(self):
        #vettorizzo la funzione di similarità 
        vsim = np.vectorize(self.sim)
        #calcolo la similarità fra ogni elemento
        self.S = vsim(self.D)
    
    #converte un valore di similarità
    #in entropia
    @staticmethod
    def sim_to_entropy(sv):
        if sv != 1:
            return - ((sv * math.log2(sv)) + ((1-sv)*math.log2(1-sv)))
        else:
            return float('nan')
    
    #funzione per il calcolo dell'entropia associata
    #al dataset
    def simmatrix_entropy(self):
        entropies = [self.sim_to_entropy(x) for x in np.nditer(self.S)]
        self.E = np.nansum(entropies)/2 #FLOAT
