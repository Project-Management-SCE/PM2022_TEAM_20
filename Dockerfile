FROM python:3-alpine
COPY . /IStudy
WORKDIR /Istudy

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN pip install django_jenkins
RUN pip install Selenium
RUN pip install chromedriver-py
RUN pip install chromedriver-binary
RUN pip install chromedriver-binary-auto



RUN python manage.py makemigrations
RUN python manage.py migrate
RUN BUILD_ID=dontKillMe nohup python manage.py runserver host_server &
RUN python manage.py test ./WebIStudy
CMD [ "python", "manage.py", "runserver" ]
