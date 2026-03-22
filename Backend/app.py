from utils.wordcloud_utils import generate_mask, generate_cloud
from utils.imageCoding import decodeImageToArray, encodeImageToBase64

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CloudRequest(BaseModel):
    text: str


class MaskRequest(BaseModel):
    text: str
    mask: str

@app.post('/cloud')
def cloud(data: CloudRequest):
    text = data.text
    (cloud, width, height) = generate_cloud(text)
    cloud = encodeImageToBase64(cloud)
    return {'cloud': cloud, 'width': width, 'height': height}

@app.post('/mask')
def mask(data: MaskRequest):
    text = data.text
    mask = decodeImageToArray(data.mask.split(',')[1])
    (cloud, width, height) = generate_mask(text, mask)
    cloud = encodeImageToBase64(cloud)
    return {'cloud': cloud, 'width': width, 'height': height}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)