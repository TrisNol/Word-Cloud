docker build . -t word-cloud
docker run --name word-cloud-container -p 3000:3000 word-cloud