FROM python:3-alpine

WORKDIR /Istudy

COPY . .


## INSTALL WITH PIP
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pillow && \
    pip install --no-cache-dir pandas && \
    pip install --no-cache-dir setuptools && \
    pip install --no-cache-dir cffi && \
    pip install --no-cache-dir GLIBC && \
    pip install --no-cache-dir /wheels/numpy-1.21.4-cp39-cp39-linux_armv7l.whl && \
    pip install --no-cache-dir /wheels/scipy-1.7.2-cp39-cp39-linux_armv7l.whl && \
    pip install --no-cache-dir /wheels/jupyterlab-4.0.0a15-py3-none-any.whl     
    


    
COPY requirements.txt requirements.txt
    
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver" ]
