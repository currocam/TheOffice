#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import TheOffice
from TheOffice import url_csv

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
    texto = TheOffice.textoPersonaje("Kevin", df)
    if texto:
        wordcloudImagen(texto)
