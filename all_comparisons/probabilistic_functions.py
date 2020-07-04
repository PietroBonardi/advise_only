# general purpose
import pandas as pd
import numpy as np

# standard clustering
import sklearn.cluster as cl
import sklearn.metrics as ms
from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture

# visualization tools
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import plotly.express as px

def find_n_clusters_gaussian(X = None, START = 1, END = 10, cv = None):

    N_clusters = np.arange(START, END)

    bics = [GaussianMixture(n_components=N,
                            covariance_type=cv).fit(X).bic(X) for N in N_clusters]

    position_of_best = np.where(bics == min(bics))[0][0]
    print("Best (lowest) BIC:", bics[position_of_best])
    print("Number of Clusters for it:", N_clusters[position_of_best])

    plt.plot(N_clusters, bics)
    plt.axhline(y = 0, c = 'red')
    plt.xlabel("Number of Clusters")
    plt.ylabel("BIC")
    plt.show()
    return {"BIC": bics[position_of_best],
            "N_cluster": N_clusters[position_of_best]}

def plot_all_vars_prob(labels = None, variables = [], data = None, cluster_name = None):
    # !!! This plot is not optimized and some
    # graphs are repeated. !!!
    # Define the size of the canvas and the
    # distance between points
    fig = plt.figure(figsize = (30, 30))
    fig.subplots_adjust(hspace=0.8, wspace=0.8)
    # Define color palette
    palette = sns.color_palette('husl', (max(labels)+1))
    # Variable to keep track of the plot
    i = 0
    for colname1 in variables[:(len(variables)-1)]:
        for colname2 in variables:
            if colname1 == colname2:
                pass
            else:
                i += 1
                cluster_colors = [sns.desaturate(palette[col], 1)
                                if col >= 0 else (0.5, 0.5, 0.5, 0.5)
                                for col in labels]
                ax = plt.subplot(len(variables), len(variables), i)
                ax.scatter(data[colname1],
                            data[colname2],
                            c=cluster_colors,
                            marker='.')
                plt.xlabel(colname1)
                plt.ylabel(colname2)

    if cluster_name is not None:
        plt.savefig("plots/mutliplot_"+str(cluster_name)+".pdf")
    plt.show()

def TSNE_manifold_plot_prob(labels = None, X = None, cluster_name = None, transform = True):
    N_projection = 2
    # Transform using Manifold Learning
    if transform == True:
        X_transformed = TSNE(n_components = N_projection).fit_transform(X)
    else:
        if(X.shape[1] > 2):
            print("GIVE 2 DIMENSIONAL DATA")
            return -1
        else:
            X_transformed = X
    #
    palette = sns.color_palette('husl', (max(labels)+1))
    cluster_colors = [sns.desaturate(palette[col], 1)
                    if col >= 0 else (0.5, 0.5, 0.5)
                    for col in labels]
    plt.scatter(X_transformed[:,0],
                X_transformed[:,1],
                c=cluster_colors,
                marker='.')
    plt.title("TSNE Manifold projection for the clustering")
    plt.xlabel("X₁")
    plt.ylabel("X₂")
    if cluster_name is not None:
        plt.savefig("plots/TSNE_"+str(cluster_name)+".pdf")
    plt.show()
