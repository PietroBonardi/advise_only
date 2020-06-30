# La funzione permette di valutare una serie di approcci al clustering
# Viene progettato per funzionare con algoritmi con centroidi (k means), 
# Oppure agglomerativi.
# La logica è: 
#   - Una volta fatto il ranking delle variabili, inizio dalla più importante
#   - Faccio clustering solo con quella, valuto il miglior set di parametri da usare
#   - Una volta trovato passo ad includere la seconda etc..
#   - Alla fine confronto tutti i sottoinsiemi valutati e trovo il migliore
import pandas as pd 
import numpy as np
from sklearn import cluster
from sklearn import metrics

#raccolgo in una classe tutte le cose utili
class cluster_meter:
    ########################
    # ha come input:
    #   - il dataset completo
    #   - i rankings, ossia un dataframe con due colonne: 
    #     'feature' e 'score_final' da SRANK algorithm
    # 
    ########################
    # costruttore          #
    ########################
    def __init__(self, dataframe, rankings):
        self.DATA = dataframe
        self.RANK = rankings
    
    #metodo per trovare la configurazione ottimale
    #date le features - K MEANS
    def kmeans_kselection(self, features):
        #dataframe con solo features
        X = self.DATA[features]
        #varie opzioni per il numero di clusters
        n_cluster = [x for x in range(1, 20)]
        #ora per ogni parametro applico l'algoritmo e valuto
        kmeans        
