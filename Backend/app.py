import pathlib
import numpy as np
from PIL import Image
from utils.wordcloud import generate_mask, generate_cloud

from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
@cross_origin()
def hello_world():
    return 'Hello, World!'

@app.route('/cloud', methods=['POST'])
@cross_origin()
def cloud():
    data = request.data
    return {'message':'Cloud'}

@app.route('/mask', methods=['POST'])
@cross_origin()
def mask():
    data = request.data
    return {'message':'Mask'}

if __name__ == "__main__":
    app.run(debug=True, port=3000)


path = pathlib.Path.cwd() / 'lovecraft.txt'
print(path)

text = path.read_text()
generate_cloud(text)

mask = np.array(Image.open("mask.png").convert('RGB'))
# generate_mask(text, mask)