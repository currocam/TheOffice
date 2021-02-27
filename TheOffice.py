#!/usr/bin/env python
import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import RegexpTokenizer
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

def textoPersonaje(personaje_str, df):
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
