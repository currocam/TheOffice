#!/usr/bin/env python
import TheOffice
from TheOffice import url_csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nltk import tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def Vader_Sentimientos(texto_frases):
    """Devuelve un DataFrame con cada frase analizada con su respectivo valor de sentimiento positivo, negativo, neutral y el valor compuesto de estos.

    Parameters
    ----------
    texto : str
        Texto a analizar.

    Returns
    -------

        df : DataFrame

    """
    analyzer = SentimentIntensityAnalyzer()
    a = analyzer.polarity_scores(texto_frases[0])
    rows = [[str(sentence), analyzer.polarity_scores(sentence)['pos'], analyzer.polarity_scores(sentence)['neu'], analyzer.polarity_scores(sentence)['neg'], analyzer.polarity_scores(sentence)['compound']]
            for sentence in texto_frases]
    df = pd.DataFrame(
        rows,
        columns=[
            "Frase",
            "Positividad sentimiento",
            "Neutralidad sentimiento",
            "Negatividad sentimiento",
            "Compuesto"])
    return df


def procesarPersonaje(personaje_str, df_raw):
    texto = TheOffice.textoPersonaje(personaje_str, df_raw)
    texto_frases = tokenize.sent_tokenize(texto)
    df_per = Vader_Sentimientos(texto_frases)
    return df_per


def graph_Sentimientos(df):
    """Genera disintos gráficos representando la posibles combiaciones de variables.

    Parameters
    ----------
    df : DataFrame

    """
    sns.set_theme(style="ticks")
    sns.pairplot(df, hue="Personaje", palette='rocket')
    plt.show()


def graph_SentimientosCompuesto(df):
    """Genera un gráfico representando la distribución del valor compuesto de sentimientos positivos/negativos.

    Parameters
    ----------
    df : DataFrame

    """
    sns.set_theme(style="ticks")
    sns.kdeplot(
        data=df,
        x="Compuesto",
        hue="Personaje",
        shade=True,
        palette='pastel')
    plt.title('Distribución sentimientos personajes en The Office')
    plt.savefig('Vader_AnalisisSentimientos.png')
    plt.show()


if __name__ == '__main__':
    lista_per = ['Kevin', 'Ryan', 'Michael']
    df_raw = pd.read_csv(url_csv)
    lista_df = []
    for personaje_str in lista_per:
        df_per = procesarPersonaje(personaje_str, df_raw)
        lista_df.append(df_per)
    df = TheOffice.generarDataFramePersonajes(lista_df, lista_per)
    graph_SentimientosCompuesto(df)
