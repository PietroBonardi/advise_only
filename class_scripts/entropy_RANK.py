import pandas as pd 
import numpy as np 
import math
from entropy_selection_class import dataframe_ext
##############################################################################
#                                                                            #
#                   RANK ALGORITHM                                           #
#       non adatto a grossi dataset (anche non troppo grossi)                #
##############################################################################
def RANK(df):
    #ottengo il vettore dei nomi delle colonne
    features = list(df.columns)

    #creo un dizionario per ora vuoto che conterrà i valori
    #dell'entropia per ogni colonna
    entropy_values = []
    
    #ciclo per ogni feature
    print("\t", "features: ")
    for F in features:
        print("\t\t", F)
        #genero un nuovo oggetto togliendo 
        #una colonna dal dataset
        feature_partial = dataframe_ext(df.drop(columns = [F]))
        feature_partial.complete()
        #ottengo l'entropia del dataset senza
        #la colonne F e la salvo nel dizionario
        entropy_values.append(feature_partial.E)
    
    #creo un dataframe a partire dal dizionario
    #e ranko dall'entropia più alta alla più bassa
    rankings = pd.DataFrame({
                                "feature" : features, 
                                "entropy" : entropy_values
                            })

    #faccio alcune operazioni sul dataset
    rankings = (rankings.sort_values(by = "entropy")                    #sorto secondo i valori di entropia
                       .reset_index(drop = True)                        #resetto l'indice 
                       .reset_index()                                   #resetto di nuovo per avere la colonna dei rankings
                       .rename(columns = {"index" : "ranking"})         #rinomino index con rankings
                       .set_index("feature"))                          #metto l'indice sul nome delle features
    return rankings

##############################################################################
#                                                                            #
#                   SRANK ALGORITHM                                          #
#       Adatto a grossi dataset (grossi a piacere) - usa RANK                #
##############################################################################
def SRANK(df_big):
    #parametro per il numero di sample
    N_SAMPLE = 4
    SAMPLE_SIZE = 10

    #inizializzo il dataframe con i ranking e l'entropia, inizialmente a 0
    features = list(df_big.columns)
    orankings = [0 for x in features]
    tot_rankings = pd.DataFrame({
                                    "feature" : features, 
                                    "rank_final" : orankings,
                               }, index = "feature")
    
    #ora faccio random sampling e applico il RANK
    for i in range(N_SAMPLE):
        print("SAMPLE: ", i)
        #random sampling del dataframe grande
        df_sample = df_big.sample(n = SAMPLE_SIZE, replace = True)
        sample_ranking = RANK(df_sample)
        #ora sommo i ranking in sample con il valore di rank_final
        tot_rankings["rank_final"] = tot_rankings["rank_final"] + sample_ranking["ranking"]
    
    #ora restitusco il dataframe dei ranking sortato
    return tot_ranking.sort(by = "rank_final")
