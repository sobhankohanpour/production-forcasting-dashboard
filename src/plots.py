import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def scatterplot(dataset, x, y, hue=None, title="Scatter Plot"):
    fig, ax = plt.subplots()
    sns.scatterplot(data=dataset, x=x, y=y, hue=hue, ax=ax)
    ax.set_title(title)
    st.pyplot(fig)


def lineplot(dataset, x, y, hue=None, title="Line Plot"):
    fig, ax = plt.subplots()
    sns.lineplot(data=dataset, x=x, y=y, hue=hue, ax=ax)
    ax.set_title(title)
    st.pyplot(fig)


def distplot(dataset, x, hue=None, title="Distribution Plot"):
    g = sns.displot(data=dataset, x=x, hue=hue)
    plt.suptitle(title)
    st.pyplot(g.fig)


def histplot(dataset, x, hue=None, bins=30, title="Histogram"):
    fig, ax = plt.subplots()
    sns.histplot(data=dataset, x=x, hue=hue, bins=bins, ax=ax)
    ax.set_title(title)
    st.pyplot(fig)


def kdeplot(dataset, x, hue=None, fill=True, title="KDE Plot"):
    fig, ax = plt.subplots()
    sns.kdeplot(data=dataset, x=x, hue=hue, fill=fill, ax=ax)
    ax.set_title(title)
    st.pyplot(fig)


def ecdfplot(dataset, x, hue=None, title="ECDF Plot"):
    fig, ax = plt.subplots()
    sns.ecdfplot(data=dataset, x=x, hue=hue, ax=ax)
    ax.set_title(title)
    st.pyplot(fig)


def rugplot(dataset, x, hue=None, title="Rug Plot"):
    fig, ax = plt.subplots()
    sns.rugplot(data=dataset, x=x, hue=hue, ax=ax)
    ax.set_title(title)
    st.pyplot(fig)


def catplot(dataset, x, y, hue=None, kind="strip", title="Categorical Plot"):
    g = sns.catplot(data=dataset, x=x, y=y, hue=hue, kind=kind)
    plt.suptitle(title)
    st.pyplot(g.fig)


def stripplot(dataset, x, y, hue=None, title="Strip Plot"):
    fig, ax = plt.subplots()
    sns.stripplot(data=dataset, x=x, y=y, hue=hue, ax=ax)
    ax.set_title(title)
    st.pyplot(fig)


def swarmplot(dataset, x, y, hue=None, title="Swarm Plot"):
    fig, ax = plt.subplots()
    sns.swarmplot(data=dataset, x=x, y=y, hue=hue, ax=ax)
    ax.set_title(title)
    st.pyplot(fig)


def boxplot(dataset, x, y, hue=None, title="Box Plot"):
    fig, ax = plt.subplots()
    sns.boxplot(data=dataset, x=x, y=y, hue=hue, ax=ax)
    ax.set_title(title)
    st.pyplot(fig)


def violinplot(dataset, x, y, hue=None, split=False, title="Violin Plot"):
    fig, ax = plt.subplots()
    sns.violinplot(data=dataset, x=x, y=y, hue=hue, split=split, ax=ax)
    ax.set_title(title)
    st.pyplot(fig)


def pointplot(dataset, x, y, hue=None, title="Point Plot"):
    fig, ax = plt.subplots()
    sns.pointplot(data=dataset, x=x, y=y, hue=hue, ax=ax)
    ax.set_title(title)
    st.pyplot(fig)


def barplot(dataset, x, y, hue=None, title="Bar Plot"):
    fig, ax = plt.subplots()
    sns.barplot(data=dataset, x=x, y=y, hue=hue, ax=ax)
    ax.set_title(title)
    st.pyplot(fig)
