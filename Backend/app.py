import pathlib
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2


path = pathlib.Path.cwd() / 'lovecraft.txt'
print(path)

text = path.read_text()
wordcloud = WordCloud().generate(text)

# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.savefig("cloud.png", dpi=600, facecolor="w", format="png")
# plt.show()

mask = np.array(Image.open("mask.png").convert('RGB'))
stopwords = set(STOPWORDS)

# wordcloud = WordCloud(stopwords=stopwords, mask=mask, background_color="white", mode="RGB", max_words=1500, contour_width=0.25, contour_color='black').generate(text)
wordcloud = WordCloud(stopwords=stopwords, mask=mask, background_color="white", mode="RGBA", max_words=2500).generate(text)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("cloud_with_mask.png", dpi=750, facecolor="w", format="png")
plt.imshow(mask)