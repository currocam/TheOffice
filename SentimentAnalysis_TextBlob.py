#!/usr/bin/env python
from textblob import TextBlob
import TheOffice
from TheOffice import url_csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def TextBlob_Sentimientos(texto):
    """Devuelve un DataFrame con cada frase analizada con su respectivo valor de polaridad del sentimiento y subjetividad.

    Parameters
    ----------
    texto : str
        Texto a analizar.

    Returns
    -------

        df : DataFrame

    """
    blob = TextBlob(texto)
    rows = [[str(sentence), sentence.polarity, sentence.subjectivity]
            for sentence in blob.sentences]
    df = pd.DataFrame(
        rows,
        columns=[
            "Frase",
            "Polaridad sentimiento",
            "Subjetividad"])
    return df


def graph_Sentimientos(df):
    """Genera un gráfico representando subjetividad Vs polaridad del sentimiento.

    Parameters
    ----------
    df : DataFrame

    """
    sns.set_theme(style="ticks")
    ax = sns.jointplot(
        x=df['Polaridad sentimiento'],
        y=df.Subjetividad,
        hue=df.Personaje,
        kind="kde",
        palette='rocket')
    plt.savefig('TextBlob_AnalisisSentimientos.png')
    plt.show()


def test_Analisis(df):
    """Devuelve una línea aleatoria del DataFrame formateada adecuadamente para comprobar el buen funcionamiento del script.

    Parameters
    ----------
    df : DataFrame

    """
    row = df.sample()
    print("Personaje: {0}".format(str(row['Frase'])))
    print("Polaridad del sentimiento: {0}".format(
        float(row['Polaridad sentimiento'])))
    print("Subjetividad: {0} \n".format(float(row['Subjetividad'])))


if __name__ == '__main__':
    lista_per = ['Jim', 'Pam']
    df_raw = pd.read_csv(url_csv)
    lista_df = []
    for personaje_str in lista_per:
        texto = TheOffice.textoPersonaje(personaje_str, df_raw)
        df_per = TextBlob_Sentimientos(texto)
        lista_df.append(df_per)
    df = TheOffice.generarDataFramePersonajes(lista_df, lista_per)
    graph_Sentimientos(df)
