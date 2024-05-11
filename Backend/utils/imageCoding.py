import base64
import cv2
import numpy as np

def decodeImageToArray(image: str) -> np.array:
    """Transform a base64 encoded image to an array

    Args:
        image (str): Base64 image

    Returns:
        np.array: Array representation of image
    """
    im_bytes = base64.b64decode(image)
    im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
    frame = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    return frame

def encodeImageToBase64(image: np.array, img_format: str = ".jpg") -> str:
    """Transform an array representation of an image to a base64 encoded string.

    Args:
        image (np.array): Image to be transformed
        img_format (str, optional): Image format of output (e.g. png or jpg). Defaults to ".jpg".

    Returns:
        str: Base64 image
    """
    (flag, encodedImage) = cv2.imencode(img_format, image)
    return base64.b64encode(encodedImage).decode('utf-8')