FROM python:3-alpine

WORKDIR /Istudy

COPY . .

RUN apk add build-base
RUN apk update && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev

    
## INSTALL WITH PIP install
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pillow 
    

 
RUN adduser -D myuser
USER myuser
WORKDIR /home/myuser

COPY --chown=myuser:myuser requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

ENV PATH="/home/myuser/.local/bin:${PATH}"

COPY --chown=myuser:myuser . .


    
#COPY requirements.txt requirements.txt
    
#RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["python3", "manage.py", "runserver", "127.0.0.1:8000"]
EXPOSE 8000
