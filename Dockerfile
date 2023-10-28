FROM python:3.11.0
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH="${PYTHONPATH}:/usr/local/lib/python3.11/site-packages"

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/