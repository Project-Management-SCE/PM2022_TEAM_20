FROM python:3-alpine
COPY . /IStudy
WORKDIR /Istudy

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD [ "python", "manage.py", "runserver" ]
