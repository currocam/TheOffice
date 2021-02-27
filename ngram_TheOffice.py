#!/usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from TheOffice import ProcesarPersonaje
import nltk



def getNgrams(textoProcesado, N):
    """Devuelve una serie con el nº de veces que aparece cada n-grama con el n-grama en cuestión como índice.

    Parameters
    ----------
    textoProcesado: str
        Texto procesado.
    N : int
        Valor N del n-grama.

    Returns
    -------
    serie: pandas.core.series.Series
        Description of returned object.

    """
    serie = pd.Series(nltk.ngrams(textoProcesado, N)).value_counts()
    return serie


def nGrams_graph(serie_Ngrams):
    index = [', '.join(tup)for tup in serie_Ngrams.index]
    sns.barplot(y=index, x=serie_Ngrams, color="b", orient='h', palette="deep")
    plt.xticks([])
    plt.title(
        "Trigramas más frecuentes de {0} en The Office".format(personaje_str),
        fontweight='bold')
    plt.xlabel("Frecuencia")
    plt.show()


if __name__ == '__main__':
    personaje_str='Oscar'
    textoProcesado=ProcesarPersonaje(personaje_str)
    serie_Ngrams = getNgrams(textoProcesado, 3)
    nGrams_graph(serie_Ngrams[:25])
