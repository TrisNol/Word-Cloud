from utils.wordcloud_utils import generate_mask, generate_cloud
from utils.imageCoding import decodeImageToArray, encodeImageToBase64

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/cloud', methods=['POST'])
def cloud():
    data = request.json
    text = data['text']
    (cloud, width, height) = generate_cloud(text)
    cloud = encodeImageToBase64(cloud)
    return {'cloud': cloud, 'width': width, 'height':height}

@app.route('/mask', methods=['POST'])
def mask():
    data = request.json
    text = data['text']
    mask = decodeImageToArray(data['mask'].split(',')[1])
    (cloud, width, height) = generate_mask(text, mask)
    cloud = encodeImageToBase64(cloud)
    return {'cloud': cloud, 'width': width, 'height':height}

if __name__ == "__main__":
    # TODO Read port from ENV
    app.run(host="0.0.0.0", port=3000)