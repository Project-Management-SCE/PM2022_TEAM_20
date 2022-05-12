FROM python:3-alpine

WORKDIR /Istudy

COPY . .

RUN apk add build-base

    
## INSTALL WITH PIP
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pillow && \
    pip install Cmake && \ 
    pip install --no-cache-dir cffi

 
    


    
COPY requirements.txt requirements.txt
    
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver" ]
