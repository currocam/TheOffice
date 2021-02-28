#!/usr/bin/env python
from SentimentAnalysis_TextBlob import TextBlob_Sentimientos
from TheOffice import url_csv
import matplotlib.pyplot as plt
import TheOffice
import pandas as pd
import seaborn as sns
import numpy as np


def intervencionComun(lista_per, dfEscena):
    """Devuelve True si todos los personajes de la lista participan en la escena.

    Parameters
    ----------
    lista_per : list
        Lista de personajes de interés.
    dfEscena : DataFrame
        Filas del DataFrame de la escena en cuestión.

    Returns
    -------
    Boolean
        True si todos los eprsonajes de la lista participan en la escena, False en el caso contrario.

    """
    figurantes = dfEscena.speaker
    boolean_list = [[per in figurantes] for per in lista_per]
    return all(boolean_list)


def escenasCompartidas(lista_per):
    """Devuelve un índice con todas las escenas compartidas por una lista de personajes..

    Parameters
    ----------
    lista_per : list
        Lista de personajes de interés.
    Returns
    -------
    index : list
        Índice de escenas compartidas.

    """
    index = []
    for escena in df_raw.scene.unique():
        dfEscena = df_raw.loc[(df_raw['scene'] == escena)]
        if intervencionComun(lista_per, dfEscena):
            index.append(escena)
    return index


def AnalisisEscena(escena, lista_per):
    """Devuelve valores promedio de la polaridad del sentimiento y subjetividad de cierto grupo de personajes en una escena.

    Parameters
    ----------
    escena : int
        Número de escena.
    lista_per : list
        Lista de personajes de interés

    Returns
    -------
    Polaridad del sentimiento : float
    Subjetividad : float

    """
    dfEscena = df_raw.loc[(df_raw['scene'] == escena)]
    dfEscena = dfEscena.loc[dfEscena['speaker'].isin(lista_per)]
    texto = dfEscena['line'].to_string(
        na_rep=' ', header=False, index=False,)
    df = TextBlob_Sentimientos(texto)
    return np.mean(df['Polaridad sentimiento']), np.mean(df['Subjetividad'])


def generarDataFrameAfinidad(lista_per):
    """Genera un DataFrame con los sentimientos y subjetividad promedio de las escenas compartidas por un grupo de personajes.

    Parameters
    ----------
    lista_per : list
        Lista de personajes de interés
    Returns
    -------
    df : DataFrame
        DataFrame con la información de afinidad entre varios personajes.

    """
    df_raw = pd.read_csv(url_csv)
    index = escenasCompartidas(lista_per)
    rows = [[i, *AnalisisEscena(i, lista_per)]
            for i in index]
    df = pd.DataFrame(
        rows,
        columns=[
            "Escena",
            "Polaridad sentimiento",
            "Subjetividad"])
    return df


def graphAfinidad(df, lista_per):
    """Genera un gráfico adecuado para ver la afinidad entre dos personajes.

    Parameters
    ----------
    df : DataFrame
        DataFrame con la información de afinidad entre varios personajes.
    lista_per : list
        Lista de personajes de interés

    """
    g = sns.jointplot(
        data=df,
        x="Polaridad sentimiento",
        y="Subjetividad",
        dropna=True,
        kind="kde",
        color="#4CB391")
    g.set_axis_labels("Polaridad sentimiento", "Subjetividad")
    plt.show()
    g.savefig('Afinidad de {0}.png'.format(','.join(lista_per)))


if __name__ == '__main__':
    df_raw = pd.read_csv(url_csv)
    lista_per = ['Pam', 'Jim']
    df = generarDataFrameAfinidad(lista_per)
    graphAfinidad(df, lista_per)
