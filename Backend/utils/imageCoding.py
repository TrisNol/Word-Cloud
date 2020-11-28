import base64
import cv2
import numpy as np

def decodeImageToArray(image):
    im_bytes = base64.b64decode(image)
    im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
    frame = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    return frame

def encodeImageToBase64(image):
    (flag, encodedImage) = cv2.imencode(".jpg", image)
    return base64.b64encode(encodedImage).decode('utf-8')