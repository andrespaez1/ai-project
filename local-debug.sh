docker rmi -f ai-project
docker build -t ai-project .
docker run -p 8000:80 ai-project
