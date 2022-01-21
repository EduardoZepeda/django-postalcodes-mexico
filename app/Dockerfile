FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY app .
RUN mkdir -p django_postalcodes_mexico
COPY django_postalcodes_mexico django_postalcodes_mexico