FROM python:3-alpine

WORKDIR /Istudy

COPY . .

RUN apk add build-base


## INSTALL WITH APK
RUN apt-get update && apt-get install -y \
    g++ \
    gcc \
    python3-dev \ 
    libjpeg-dev \
    zlib1g-dev \
    make \
    wget \
    libatlas-base-dev \
    libffi-dev  
    
    
## INSTALL WITH PIP
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pillow && \
    pip install --no-cache-dir cffi && \

 
    


    
COPY requirements.txt requirements.txt
    
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver" ]
