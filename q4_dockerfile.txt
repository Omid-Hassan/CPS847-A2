http://127.0.0.1:5000/
to test after running app.py. Allows to render webpage locally

Dockerfile for this is:
FROM python:3.6.1
# define the present working directory
WORKDIR /docker-flask-test
# copy the contents into the working dir
ADD . /docker-flask-test
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# define the command to start the container

EXPOSE 5000

CMD ["python","app.py"]