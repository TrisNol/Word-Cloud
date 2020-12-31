from .utils.wordcloud import generate_mask, generate_cloud
from .utils.imageCoding import decodeImageToArray, encodeImageToBase64

from flask import Flask, request, send_from_directory
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
    if path.endswith(".js"): 
        return send_from_directory('./static', path, mimetype="application/javascript")
    return send_from_directory('./static', path)


@app.route('/')
def root():
  return send_from_directory('./static', 'index.html')

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
    app.run(debug=True, port=3000, host='0.0.0.0')