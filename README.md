# Word-Cloud
This project was inspired by a video from Python Programmer showing how to generate Word Clouds in pyhon with minimal effort: https://www.youtube.com/watch?v=MTvHQ6YjfjE

Adding an Angular frontend improves usability and hosting.

## Backend
The Python based backend hosts a REST API which receives the neccessary data to create a word cloud. On the one hand an API to send a bulk of text is hosted on the other hand an extension including a 'mask' can be used.

## Frontend
The Angular frontend enables the user to upload .txt-files or write his own text for later use in the word cloud generation. If a .png is uploaded it will be regarded as the 'mask' and can be used to generate a masked word cloud. Neither the images nor the text files are stored on cloud storage during processing, they are simply encoded in the frontend and sent to the backend.