import pathlib
import numpy as np
from PIL import Image
from utils.wordcloud import generate_mask, generate_cloud
from utils.imageCoding import decodeImageToArray, encodeImageToBase64

from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route('/cloud', methods=['POST'])
@cross_origin()
def cloud():
    data = request.json
    text = data['text']
    (cloud, width, height) = generate_cloud(text)
    cloud = encodeImageToBase64(cloud)
    return {'cloud': cloud, 'width': width, 'height':height}

@app.route('/mask', methods=['POST'])
@cross_origin()
def mask():
    data = request.json
    text = data['text']
    mask = decodeImageToArray(data['mask'].split(',')[1])
    (cloud, width, height) = generate_mask(text, mask)
    cloud = encodeImageToBase64(cloud)
    return {'cloud': cloud, 'width': width, 'height':height}

if __name__ == "__main__":
    app.run(debug=True, port=3000)


path = pathlib.Path.cwd() / 'lovecraft.txt'
print(path)

text = path.read_text()
generate_cloud(text)

mask = np.array(Image.open("mask.png").convert('RGB'))
# generate_mask(text, mask)