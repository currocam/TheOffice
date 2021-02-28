![https://es.wikipedia.org/wiki/The_Office#/media/Archivo:The_Office_US_logo.svg](The_Office_US_logo.svg)
# Natural Language Processing with Python for The Office
This following scripts explore different aspects of Natural Language Processing using the transcription of the The Office series. It was created with **educational purposes**. I have used this dataset [The Office (US) - Complete Dialogue/Transcript](https://www.kaggle.com/nasirkhalid24/the-office-us-complete-dialoguetranscript/).

## Features
1. Character Wordcloud generator using the [wordcloud library](https://pypi.org/project/wordcloud/).
2. Get a character n-grams from his/her text lines. 
3. Analyse a character sentiments expressed in The Office using the [VADER (Valence Aware Dictionary and sEntiment Reasoner) library](https://github.com/cjhutto/vaderSentiment). We quantify sentiment polarity (positive/negative) on a scale from -1 to 1. 
4.  Analyse a character sentiments expressed in The Office using the [TextBlob library](https://github.com/sloria/TextBlob). We quantify sentiment polarity (positive/negative) on a scale from -1 to 1 and subjectivity (objective/subjective) on a scale from 0 to 1.
5. Research affinity between characters from the the sentiment analysis of their lines during the scene where they appear. 
 
## Technologies
- Python 3.8.5

## Example of use

```
python nubePalabras.py Pam 
```
![Pam_nube.png](Pam_nube.png)

```
python ngram_TheOffice.py
```
![Jim_n-gramas.png](Jim_n-gramas.png)

```
python SentimentAnalysis_TextBlob.py 
```
![TextBlob_AnalisisSentimientos.png](TextBlob_AnalisisSentimientos.png)

```
python afinidadPersonajes.py
```

![Afinidad_Pam_Jim.png](Afinidad_Pam_Jim.png)








