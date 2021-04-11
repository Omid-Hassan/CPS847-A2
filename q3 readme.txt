======= setup =======

https://www.dailysmarty.com/posts/steps-for-deploying-a-static-html-site-with-docker-and-nginx

Create a file called Dockerfile

Inside put in:
FROM nginx:alpine
COPY . /usr/share/nginx/html

Build the docker image with the command:
docker build -t html-server-image:v1 .

Run the command to let the image run on port 80:
docker run -d -p 80:80 html-server-image:v1

Create an index.html file

If the container is running it can now be viewed in localhost:80 from the browser.

======= setup =======

======= demo =======

To show the list of containers to run:
docker ps -a

Run the container by taking the [name] from the list:
docker start [name]

Open browser at localhost:80

Stop container:
docker stop [name]

======= demo =======