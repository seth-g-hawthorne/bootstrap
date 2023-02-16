# Jumpstart: stacks/nodejs/examples/docker

## Build and run the container

```
docker build . -t "your-name/node-web-app"
docker run -p 49160:8080 -d your-name/node-web-app
docker ps 
```

## Test
```
curl -i localhost:49160
```

## Kill the container
```
docker kill <container-id>