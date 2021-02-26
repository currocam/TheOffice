#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

url_csv = "TheOfficeLines.csv"


def textoPersonaje(personaje_str):
    """
    Devuelve un str con todas las líneas de un personaje.
    """
    df_personaje = df.loc[df['speaker'] == personaje_str]['line']
    if df_personaje.empty:
        print("No hay registros para ese personaje")
    else:
        texto = df_personaje.to_string(na_rep=' ', header=False, index=False,)
        return texto


def wordcloudImagen(texto):
    """
    Genera una una imagen con las palabras más comunes del personaje.
    """
    wc = WordCloud(background_color="white", max_words=2000,
                   contour_width=3, contour_color='steelblue')
    wc.generate(texto)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv(url_csv)
    texto = textoPersonaje("Kevin")
    if texto:
        wordcloudImagen(texto)
