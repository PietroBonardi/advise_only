#lo script serve per calcolare l'entropia associata ad un dataset per poi
#applicare l'algoritmo RANK. Tutte le info sono contenute nel pdf all'interno 
#della repository

#QUESTO SCRIPT RACCOGLIE SOLO LE FUNZIONI NECESSARIE
#PER ORA FUNZIONA SOLO CON DATI DI TIPO NUMERICO (LA MAGGIOR PARTE)
import math
import pandas as pd 
import scipy 
import numpy as np
import sklearn.metrics 

#definisco la normale distanza euclidea
#fra due series numpy
def dist_measure(x1, x2):
    return np.linalg.norm(x1- x2)

#definisco una funzione che prende in input un dataframe pandas
#e restituisce la matrice delle distanze
def dist_matrix(df):
    df = df.reset_index(drop = True)
    MATRIX = [
        [dist_measure(row1, row2) if index1 >= index2 else None for index1, row1 in df.iterrows()]
        for index2, row2 in df.iterrows()
    ]
    return MATRIX

#definisco una funzione che presa la matrice delle distanze mi restituisce
#la matrice di similarità

#definisco una funzione che data una una matrice delle distanze definisce una matrice delle
#similarità, con misura esponenziale
def sim_matrix(dist_matrix):
    #calcolo di alpha 
    alpha = -math.log(0.5) / np.matrix.mean(dist_matrix)
    #funzione per calcolo della similarità dalla distanza
    def sim(dist_value, alpha):
        return math.exp(-alpha * dist_value)
    vsim = np.vectorize(sim)
    #sostituisco ogni elemento della matrice con la similarità
    MATRIX = vsim(dist_matrix, alpha)
    return MATRIX

#definisco una funzione che data una matrice di similarità calcola l'entropia del dataset
def simmatrix_entropy(sim_matrix):
    #funzione per trasformare valori di similarità in valori di entropia
    def sim_to_entropy(sv):
        if sv != 1:
            sv = (sv * math.log2(sv)) + ((1-sv)*math.log2(1-sv))
            return sv
        else:
            return float('nan')
    entropies = [sim_to_entropy(x) for x in np.nditer(sim_matrix)]
    return np.nansum(entropies)/2 #FLOAT

########################################################################
#                                                                      #
#           RANK ALGORITHM                                             #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#           SCALABLE RANKING                                           #
#                                                                      #
########################################################################
