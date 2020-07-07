# General purpose
import pandas as pd
import yaml
import numpy as np

# To scale data
from sklearn.preprocessing import StandardScaler

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

def multiple_barplots(variables = [], data = None, name = None, title='', format='pdf'):
    # Define the environment for the plot
    # More than 3 plots for row is too much
    # so the number of columns is fixed
    NCOL = int(len(variables)/3+0.5)
    NROW = 3
    fig, axes = plt.subplots(nrows=NCOL,
                            ncols=NROW,
                            figsize=(15,12))
    # Easier for looping over
    axes = axes.ravel()
    # Loop over variablws
    for i, var in enumerate(variables):
        data.boxplot(column = var,
                                by='Clusters',
                                ax = axes[i])
    fig.delaxes(axes[
                    (len(variables)-NCOL*NROW)
                    ])
    plt.tight_layout()
    plt.suptitle(title,
                size=20,
                y=1.05)
    if name is not None:
        plt.savefig("plots/barplot_"+str(name)+"."+str(format))
    plt.show()

def multiple_violins(variables = [], data = None, name = None, palette = None, title='', format='pdf'):
    if palette is None:
        palette = sns.color_palette('husl', 5)
    # Define the environment for the plot
    # More than 3 plots for row is too much
    # so the number of columns is fixed
    NCOL = int(len(variables)/3+0.5)
    NROW = 3
    fig, axes = plt.subplots(nrows=NCOL,
                            ncols=NROW,
                            figsize=(15,12))
    # Easier for looping over
    axes = axes.ravel()
    # Loop over variablws
    for i, var in enumerate(variables):
        sns.violinplot(x = "Clusters",
                        y = var,
                        data = data,
                        palette = palette,
                        ax = axes[i])
    fig.delaxes(axes[
                    (len(variables)-NCOL*NROW)
                    ])
    plt.tight_layout()
    plt.suptitle(title,
                size=20,
                y=1.05)
    if name is not None:
        plt.savefig("plots/violins_"+str(name)+"."+str(format))
    plt.show()

# This function is not well written
def distribution_histograms(variables = [], data = None, name = None, palette = None, format='pdf'):
    if palette is None:
        palette = sns.color_palette('husl', 5)
    # Define the environment for the plot
    # More than 3 plots for row is too much
    # so the number of columns is fixed
    NCOL = int(len(variables)/3+0.5)
    NROW = 3
    fig, axes = plt.subplots(nrows=NCOL,
                            ncols=NROW,
                            figsize=(20,12))
    # Easier for looping over
    axes = axes.ravel()
    for i, var in enumerate(variables):
        for cluster in range(-1, 4):
            sns.distplot(data.iloc[np.where(data['Clusters'] == cluster)][var],
                         label=(cluster),
                         hist_kws=dict(alpha=0.2),
                         ax = axes[i],
                         color = palette[cluster+1])
            axes[i].legend()
            # axes[i].title(str(var)+" distribution in the clusters", size=20)
            axes[i].grid(True, 'major')

    fig.delaxes(axes[
                    (len(variables)-NCOL*NROW)
                    ])
    plt.tight_layout()
    if name is not None:
        plt.savefig("plots/distributions_"+str(name)+"."+str(format))
    plt.show()

def error_plot(variables = [], data = None, name = None, palette = None, size=(5,5), format='pdf'):
    if palette is None:
        palette = sns.color_palette('husl', 5)
    x = variables[:-1]
    plt.figure(figsize=size)
    for i in range(5):
        # exclude the noise cluster
        if i != 0:
            y = list(data[variables].groupby("Clusters").mean().reset_index().iloc[i,1:])
            err = list(data[variables].groupby("Clusters").std().reset_index().iloc[i,1:]/np.sqrt(data[variables].groupby("Clusters").count().reset_index().iloc[i,1:]))
            plt.errorbar(x,
                        y,
                        marker='.',
                        linewidth=0,
                        yerr = err,
                        elinewidth=50,
                        c=palette[i],
                        alpha=0.6,
                        label=i-1)
    plt.suptitle('Clustering Variables standardized, grouped by Clusters',
                size=20,
                y=1.03)
    plt.legend(loc='best')
    plt.tight_layout()
    if name is not None:
        plt.savefig("plots/errorplot_"+str(name)+"."+str(format))
    plt.show()
