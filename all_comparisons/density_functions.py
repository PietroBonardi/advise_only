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

def best_eps(X = None):
    neigh = NearestNeighbors(n_neighbors=2)
    nbrs = neigh.fit(X)
    distances, indices = nbrs.kneighbors(X)
    distances = np.sort(distances, axis=0)
    distances = distances[:,1]

    plt.plot(distances)
    plt.ylabel("Distances")
    plt.savefig("Distances_for_eps.pdf")
    plt.show()

def find_best_min_samples(X = None, START = 1, END = 100, EPS = 0.5):
#     Scale the data. Makes the algorithm more correct
    # Devo partire da 0.3, altrimenti da un sacco di problemi

    sils = []
    N_clusters = []
    SAMPLES = np.arange(START, END)
    for MIN_SAMPLE in SAMPLES:
        print("-- Progress: "+str(int(((MIN_SAMPLE-START)/(END-START))*10000)/100)+"%\r", end='')
#         Clustering
        clusterer = DBSCAN(eps=EPS,
                    min_samples=MIN_SAMPLE).fit(X)
#         Get the labels (-1 is noise points)
        labels = clusterer.labels_

        # Number of clusters in labels, ignoring noise if present.
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise_ = list(labels).count(-1)

#         Keeps trace of the number of clusters
        N_clusters.append(n_clusters_)
#         Keeps trace of the silhouette results
        X_score = X[np.where(labels > 0)]
        labels_score = labels[np.where(labels > 0)]

        sils.append(ms.silhouette_score(X_score, labels_score))


#     Save the best Silhouette and its position
    position_of_best = np.where(sils == max(sils))[0][0]
    print("Best Silhouette:", sils[position_of_best])
    print("Number of Clusters for it:", N_clusters[position_of_best])
    print("Min_sample value for it:", SAMPLES[position_of_best])

#     Plor the MIN_SAMPLE value (step) to the Silhouette coefficient
    plt.plot(SAMPLES, sils)
    plt.axhline(y = 0, c = 'red')
    plt.show()
    return {"Silhouette": sils[position_of_best],
            "N_cluster": N_clusters[position_of_best],
            "Min": SAMPLES[position_of_best]}

def clustering_dbscan(X = None, EPS = None, BEST_MIN = None):
    db = DBSCAN(eps=EPS,
                min_samples=BEST_MIN).fit(X)
    labels = db.labels_

    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)

    print('Estimated number of clusters: %d' % n_clusters_)
    print('Estimated number of noise points: %d' % n_noise_)
    print("Silhouette Coefficient: %0.3f" % ms.silhouette_score(X, labels))
    return db, n_clusters_, n_noise_, labels

def plotting_two_vars(attr1 = None, attr2 = None, data = None, n_clusters_ = None, labels = None):
    # Example of plot
    attr1 = "ProtectionNeed"
    attr2 = "RiskPropension"
    colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
    for j in range(n_clusters_):
            plt.plot(data[attr1][labels == j],
                    data[attr2][labels == j], '.', color=colors[j])
    # plt.plot(DF[attr1][labels == -1],
    #          DF[attr2][labels == -1], '.', color='grey')
    plt.xlabel(attr1)
    plt.ylabel(attr2)
    plt.savefig("clustering_res.pdf")
    plt.show()

def plotting_all_vars_hdbscan(vars = [], clusterer = None, data = None):
    # !!! This plot is not optimized and some
    # graphs are repeated. !!!
    # Define the size of the canvas and the
    # distance between points
    fig = plt.figure(figsize = (30, 30))
    fig.subplots_adjust(hspace=0.8, wspace=0.8)
    # Define color palette
    palette = sns.color_palette()
    # Variable to keep track of the plot
    i = 0
    for colname1 in vars[:(len(vars)-1)]:
        for colname2 in vars:
            if colname1 == colname2:
                pass
            else:
                i += 1

                cluster_colors = [sns.desaturate(palette[col], sat)
                                if col >= 0 else (0.5, 0.5, 0.5, 0.5)
                                for col, sat in zip(clusterer.labels_, clusterer.probabilities_)]
                ax = plt.subplot(len(vars), len(vars), i)
                ax.scatter(data[colname1],
                            data[colname2],
                            c=cluster_colors,
                            marker='.')
                plt.xlabel(colname1)
                plt.ylabel(colname2)
    plt.savefig("hdbscan_res.png")
    plt.close()

def plotting_all_vars_dbscan(vars = [], clusterer = None, data = None):
    # !!! This plot is not optimized and some
    # graphs are repeated. !!!
    # Define the size of the canvas and the
    # distance between points
    fig = plt.figure(figsize = (30, 30))
    fig.subplots_adjust(hspace=0.8, wspace=0.8)
    # Define color palette
    palette = sns.color_palette()
    # Variable to keep track of the plot
    i = 0
    for colname1 in vars[:(len(vars)-1)]:
        for colname2 in vars:
            if colname1 == colname2:
                pass
            else:
                i += 1

                cluster_colors = [sns.desaturate(palette[col], 1)
                                if col >= 0 else (0.5, 0.5, 0.5, 0.5)
                                for col in clusterer.labels_]
                ax = plt.subplot(len(vars), len(vars), i)
                ax.scatter(data[colname1],
                            data[colname2],
                            c=cluster_colors,
                            marker='.')
                plt.xlabel(colname1)
                plt.ylabel(colname2)
    plt.savefig("dbscan_res.png")
    plt.close()


def find_best_min_samples_optics(X = None, START = 1, END = 100, EPS = 0.5):
#     Scale the data. Makes the algorithm more correct
    # Devo partire da 0.3, altrimenti da un sacco di problemi

    sils = []
    N_clusters = []
    SAMPLES = np.arange(START, END)
    for MIN_SAMPLE in SAMPLES:
        print("-- Progress: "+str(int(((MIN_SAMPLE-START)/(END-START))*10000)/100)+"%\r", end='')
#         Clustering
        clusterer = cl.OPTICS(max_eps=EPS,
                    min_samples=MIN_SAMPLE).fit(X)
#         Get the labels (-1 is noise points)
        labels = clusterer.labels_

        # Number of clusters in labels, ignoring noise if present.
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise_ = list(labels).count(-1)

#         Keeps trace of the number of clusters
        N_clusters.append(n_clusters_)
#         Keeps trace of the silhouette results
        X_score = X[np.where(labels > 0)]
        labels_score = labels[np.where(labels > 0)]
        try:
            sils.append(ms.silhouette_score(X_score, labels_score))
        except:
            print("All points labelled as noise. Stopping.")
            break

#     Save the best Silhouette and its position
    position_of_best = np.where(sils == max(sils))[0][0]
    print("Best Silhouette:", sils[position_of_best])
    print("Number of Clusters for it:", N_clusters[position_of_best])
    print("Min_sample value for it:", SAMPLES[position_of_best])

#     Plor the MIN_SAMPLE value (step) to the Silhouette coefficient
    plt.plot(SAMPLES, sils)
    plt.axhline(y = 0, c = 'red')
    plt.show()
    return {"Silhouette": sils[position_of_best],
            "N_cluster": N_clusters[position_of_best],
            "Min": SAMPLES[position_of_best]}
