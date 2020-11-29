import pathlib
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image
from io import BytesIO
import cv2

def encodeFig(fig):
    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=fig.dpi)
    buf.seek(0)
    img_arr = np.frombuffer(buf.getvalue(), dtype=np.uint8)
    buf.close()
    img = cv2.imdecode(img_arr, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    (width, height) = fig.canvas.get_width_height()
    return (img, width, height)

def generate_cloud(text):
    fig = plt.figure()
    plt.tight_layout(pad=0)
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    return encodeFig(fig)

def generate_mask(text, mask):
    fig = plt.figure()
    stopwords = set(STOPWORDS)
    plt.tight_layout(pad=0)
    
    wordcloud = WordCloud(stopwords=stopwords, mask=mask, background_color="white", mode="RGBA", max_words=750).generate(text)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("cloud_with_mask.png", format="png", bbox_inches='tight')

    return encodeFig(fig)