FROM python:3-alpine

WORKDIR /Istudy

COPY . .

RUN apk add build-base
RUN apk update && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev
RUN sudo apt install python3-cffi

    
## INSTALL WITH PIP install
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pillow 
    

 

    
COPY requirements.txt requirements.txt
    
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver" ]
