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
RUN pip install pandas
RUN pip install numpy
RUN pip install pillow

RUN python manage.py makemigrations
RUN python manage.py migrate
CMD [ "python", "manage.py", "runserver" ]
