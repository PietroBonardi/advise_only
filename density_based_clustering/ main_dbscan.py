# general purpose
import pandas as pd
import numpy as np
import time
import scipy

# visualization tools
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import plotly.express as px

# standard clustering
import sklearn.cluster as cl
import sklearn.metrics as ms
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# Fuzzy clustering
import skfuzzy as fuzz

# For density validation
from DBCV import DBCV
from scipy.spatial.distance import euclidean

from density_functions import (pre_processing, clustering_dbscan, 
                                find_best_min_samples, best_eps, 
                                plotting_two_vars, plotting_all_vars_dbscan,
                                TSNE_manifold_plot)
import yaml

def main():
    print("-- Loading config file")
    with open("../density_based_clustering/config.yml", "r") as file:
        load_vars = yaml.safe_load(file)
    print("-- Pre-processing")

    df_person_var, df_current_investment = pre_processing()

    X = StandardScaler().fit_transform(df_person_var[load_vars["clustering_variables"]])
    print("-- Determining optimal eps")
    best_eps(X = X)
    print("Please insert the current number of eps.")
    BEST_EPS = input()

    print("-- Determining optimal min_samples")
    RESULTS = find_best_min_samples(X = X, START = 1, END = 70, EPS = 0.65)
    BEST_MIN = RESULTS["Min"]

    model, n_clusters, n_noise, labels = clustering_dbscan(X = X,
                                                    EPS = float(BEST_EPS),
                                                    BEST_MIN = BEST_MIN)
    print("-- 2D plots")
    plotting_all_vars_dbscan(vars=load_vars['clustering_variables'], 
                            clusterer=model, 
                            data=df_person_var)

    print("-- TSNE manifold learning projection plot")
    TSNE_manifold_plot(clusterer=model, 
                        X=X, 
                        cluster_name="DBSCAN")
if __name__ == "__main__":
    main()
