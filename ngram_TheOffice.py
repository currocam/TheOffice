#!/usr/bin/env python
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import RegexpTokenizer
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
url_csv = "TheOfficeLines.csv"
ADDITIONAL_STOPWORDS = ['oh', 'na', 'uh', 'boo', 'ha', 'mm',
                        'hmm', 'wow', 'uhm', 'um', 'th', 'hi', 'shh', 'bye', 'okay', 'ok', 'speech', 'whoa', 'ooh' ]


def cleanTexto(texto_raw):
    """Devuelve el texto sin signos de puntuación, tokenizado, en minúsculas y filtradas las palabras consideradas stopWords.

    Parameters
    ----------
    texto_raw : str
        Texto en bruto de un personaje.

    Returns
    -------
    textoFiltrado : str
        Texto filtrado.

    """
    stopWords = nltk.corpus.stopwords.words('english') + ADDITIONAL_STOPWORDS
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    textoTokens = tokenizer.tokenize(texto_raw)
    textoMin = [t.lower() for t in textoTokens]
    textoFiltrado = [word for word in textoMin if not word in stopWords]
    return textoFiltrado


def Lematizacion(textoFiltrado):
    """Devuelve el texto lemantizado.

    Parameters
    ----------
    textoFiltrado : str
        Texto filtrado.

    Returns
    -------
    textoProcesado: str
        Texto procesado.

    """
    lemmatizer = WordNetLemmatizer()
    textoProcesado = [lemmatizer.lemmatize(word) for word in textoFiltrado]
    return textoProcesado


def textoPersonaje(personaje_str):
    """
    Devuelve un str con todas las líneas de un personaje.
    """
    df_personaje = df.loc[df['speaker'] == personaje_str]['line']
    if df_personaje.empty:
        print("No hay registros para ese personaje")
    else:
        texto_raw = df_personaje.to_string(
            na_rep=' ', header=False, index=False,)
        return texto_raw


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
    print(type(serie))
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
    df = pd.read_csv(url_csv)
    texto_raw = textoPersonaje(personaje_str)
    textoFiltrado = cleanTexto(texto_raw)
    textoProcesado = Lematizacion(textoFiltrado)
    serie_Ngrams = getNgrams(textoProcesado, 3)
    nGrams_graph(serie_Ngrams[:25])
