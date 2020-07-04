# General purpose
import pandas as pd
import numpy as np
# visualization tools
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import plotly.express as px
# manifold learning
from sklearn.manifold import TSNE


def pre_processing():
#     Load data
    df = pd.read_csv("../dataset/DatasetClientClustering.csv",
                 engine='c',
                 sep=',',
                 encoding='latin-1')
#     Drop the first 8 columns. They do not contain any data
    df = df.drop(df.columns[list(np.arange(8))], axis=1)

#     We do not use the ClientID for any analysis
    df = df.drop(columns=["ClientID"])

#     Division in the two main categories
    current_investment = ["PortfolioRisk", "PortfolioHorizon", "AuM", "BondInvestments", "EquityInvestments",
                         "MoneyMarketInvestments", "OtherInvestments", "Cash"]
    person_var = ["RiskPropension", "ClientInvestmentHorizon", "ClientKnowledgeExperience", "ClientPotentialIndex",
                 "IncomeHighLow", "Sex", "Age", "IncomeNeed", "LongTermCareNeed", "ProtectionNeed",
                 "InheritanceIndex", "PanicMood", "ClientDateStart", "NoTrustInBanks"]
#     creation of separate dataset
    df_person_var = df[person_var]
    df_current_investment = df[current_investment]
#     return as a toople of dataframes
    return(df_person_var, df_current_investment)

def plot_all_vars(clusterer = None, variables = [], data = None, cluster_name = None):
    # !!! This plot is not optimized and some
    # graphs are repeated. !!!
    # Define the size of the canvas and the
    # distance between points
    fig = plt.figure(figsize = (30, 30))
    fig.subplots_adjust(hspace=0.8, wspace=0.8)
    # Define color palette
    palette = sns.color_palette('husl', (max(clusterer.labels_)+1))
    # Variable to keep track of the plot
    i = 0
    for colname1 in variables[:(len(variables)-1)]:
        for colname2 in variables:
            if colname1 == colname2:
                pass
            else:
                i += 1
                try:
                    cluster_colors = [sns.desaturate(palette[col], sat)
                                    if col >= 0 else (0.5, 0.5, 0.5, 0.5)
                                    for col, sat in zip(clusterer.labels_, clusterer.probabilities_)]
                except:
                    cluster_colors = [sns.desaturate(palette[col], 1)
                                    if col >= 0 else (0.5, 0.5, 0.5, 0.5)
                                    for col in clusterer.labels_]
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

def TSNE_manifold_plot(clusterer = None, X = None, cluster_name = None, transform = True):
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
    palette = sns.color_palette('husl', (max(clusterer.labels_)+1))
    try:
        cluster_colors = [sns.desaturate(palette[col], sat)
                        if col >= 0 else (0.5, 0.5, 0.5)
                        for col, sat in zip(clusterer.labels_, clusterer.probabilities_)]
    except:
        cluster_colors = [sns.desaturate(palette[col], 1)
                        if col >= 0 else (0.5, 0.5, 0.5)
                        for col in clusterer.labels_]
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
