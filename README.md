HTTP server accepts requests from the website

#### Local test
docker run -p 8080:8080 -p 12500:12500 http_socket_comm
docker buildx build --platform linux/amd64 -t http_socket_comm .

docker run -p 8080:8080 -p 12500:12500 tayvens24/http_socket_comm:V-0.1.1