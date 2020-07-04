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

# manifold learning
from sklearn.manifold import TSNE

# standard clustering
import sklearn.cluster as cl
import sklearn.metrics as ms
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn import decomposition
from sklearn.cluster import DBSCAN

# hdbscan
import hdbscan

# For density validation
from DBCV import DBCV
from scipy.spatial.distance import euclidean

# To read external config file
import yaml

def find_n_clusters_kmeans(X = None, START = 2, END = 20, mode = 'silhouette'):
    if(mode == "silhouette"):
        N_clusters = np.arange(END) + START

        # Most efficient why to do this calculation
        sils = [metrics.silhouette_score(X,
                                        cl.KMeans(n_clusters=N,
                                                    n_init=int(1e2),
                                                    init='k-means++',
                                                    max_iter=int(1e2),
                                                    tol=1e-2,
                                                    verbose=False
                                                    ).fit(X).labels_)
                for N in N_clusters
                ]

        # Save the best Silhouette and its position
        position_of_best = np.where(sils == max(sils))[0][0]
        print("Best Silhouette:", sils[position_of_best])
        print("Number of Clusters for it:", N_clusters[position_of_best])

    #     Plor the N_clusters value (step) to the Silhouette coefficient
        plt.plot(N_clusters, sils)
        plt.axhline(y = 0, c = 'red')
        plt.xlabel("Number of clusters")
        plt.ylabel("Silhouette value")
        plt.show()
        return {"Silhouette": sils[position_of_best],
                "N_cluster": N_clusters[position_of_best]}
