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
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# manifold learning
from sklearn.manifold import TSNE

# hdbscan
import hdbscan 

# For density validation
from DBCV import DBCV
from scipy.spatial.distance import euclidean
# From local files
from density_functions import (pre_processing, clustering_dbscan, 
                                find_best_min_samples, best_eps, 
                                plotting_two_vars, plotting_all_vars_hdbscan,
                                TSNE_manifold_plot)
import yaml

def main():
    print("-- Loading config file")
    with open("../density_based_clustering/config.yml", "r") as file:
        load_vars = yaml.safe_load(file)
    print("-- Pre-processing")
    df_person_var, df_current_investment = pre_processing()

    # Standardize the variables
    # Some have already decent values, while others do not.
    X = StandardScaler().fit_transform(df_person_var[load_vars["clustering_variables"]])

    # Define the algorithm and fir it.
    # The parameters are found as best matching for the 
    # task at hand.
    clusterer = hdbscan.HDBSCAN(metric = "euclidean", 
                            gen_min_span_tree=True,
                            min_cluster_size=60, 
                            min_samples=10).fit(X)

    print("-- Final number of clusters found", clusterer.labels_.max()+1)
    print('-- Number of noise points:', len(np.where(clusterer.labels_ == -1)[0]))

    print("-- 2D plots")
    plotting_all_vars_hdbscan(vars = load_vars["clustering_variables"], 
                            clusterer = clusterer,
                            data = df_person_var)

    print("-- Manifold Learning for 2D projection")
    TSNE_manifold_plot(clusterer=clusterer, X=X, cluster_name="HDBSCAN")

if __name__ == "__main__":
    main()
