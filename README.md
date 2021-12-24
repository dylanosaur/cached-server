# cached-server

Project requires no environment variables, requires ports 4999 and 5000 for container services
- 4999: nginx listener with web cache enabled
- 5000: minimal python web server using Bottle
  - single route using query params /forum?page=pageNumber
  
start service with:
  - sudo docker-compose build
  - sudo docker-compose up
