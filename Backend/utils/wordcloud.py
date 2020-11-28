import pathlib
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def generate_cloud(text):
    fig = plt.figure()
    plt.tight_layout(pad=0)
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig("cloud.png", dpi=fig.dpi, facecolor="w", format="png")
    plt.show()

def generate_mask(text, mask):
    stopwords = set(STOPWORDS)
    plt.tight_layout(pad=0)
    
    wordcloud = WordCloud(stopwords=stopwords, mask=mask, background_color="white", mode="RGBA", max_words=750).generate(text)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("cloud_with_mask.png", format="png", bbox_inches='tight')
    plt.show()