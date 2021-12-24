docker kill some-nginx
docker rm some-nginx
docker build -t some-content-nginx:latest .
docker run --name some-nginx -d -p 80:80 -p 4999:4999 --add-host=host.docker.internal:host-gateway -t some-content-nginx:latest
