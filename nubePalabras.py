#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import TheOffice
from TheOffice import url_csv
import sys

def wordcloudImagen(texto, personaje):
    """
    Genera una una imagen con las palabras más comunes del personaje.
    """
    wc = WordCloud(background_color="white", max_words=2000,
                   contour_width=3, contour_color='steelblue')
    wc.generate(texto)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    ruta='{0}_nube.png'.format(personaje)
    plt.savefig(ruta)
    plt.show()
    

if __name__ == '__main__':
    df = pd.read_csv(url_csv)
    personaje=sys.argv[1]
    texto = TheOffice.textoPersonaje(personaje, df)
    if texto:
        wordcloudImagen(texto, personaje)
