import matplotlib
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import cv2

def encodeFig(fig: matplotlib.pyplot.figure) -> tuple:
    """Tranform a matplotlib plot to an image array

    Args:
        fig (matplotlib.pyplot.figure): Plot to be transformed

    Returns:
        tuple: (img, width, height)
    """
    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=fig.dpi)
    buf.seek(0)
    img_arr = np.frombuffer(buf.getvalue(), dtype=np.uint8)
    buf.close()
    img = cv2.imdecode(img_arr, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    (width, height) = fig.canvas.get_width_height()
    return (img, width, height)

def generate_cloud(text: str) -> tuple:
    """Generate a word cloud using the provided tesxt

    Args:
        text (str): Text of word cloud

    Returns:
        tuple: (img, width, height)
    """
    fig = plt.figure()
    plt.tight_layout(pad=0)
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    return encodeFig(fig)

def generate_mask(text: str, mask: any) -> tuple:
    """Transform the text to a word cloud in the shape of the mask

    Args:
        text (str): Text of the word cloud
        mask (any): Mask to shape the cloud

    Returns:
        tuple: (img, width, height)
    """
    fig = plt.figure()
    stopwords = set(STOPWORDS)
    plt.tight_layout(pad=0)
    
    wordcloud = WordCloud(stopwords=stopwords, mask=mask, background_color="white", mode="RGBA", max_words=750).generate(text)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")

    return encodeFig(fig)