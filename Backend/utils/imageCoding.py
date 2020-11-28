import base64
from PIL import Image
import io
import numpy as np

def decodeImageToArray(image):
    image = base64.decodebytes(image)
    image = Image.open(io.BytesIO(image))
    return np.array(image)

def encodeImageToBase64(image):
    return base64.b64encode(image)