## Python Hello World App using Docker and Flask
To run locally run the following:
```
docker build -t python-hello-world:latest .
docker run --publish 8080:8080 python-hello-world:latest
```
