FROM python:3-alpine

WORKDIR /Istudy

COPY . .

# INSTALL APK

RUN apk add build-base
RUN apk update && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev

    
## INSTALL WITH PIP install
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pillow 

# CSS
RUN pip install whitenoise
   
# requirments of the project
COPY requirements.txt requirements.txt

RUN pip install gunicorn
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD gunicorn --bind 0.0.0.0:$PORT IStudy.wsgi

