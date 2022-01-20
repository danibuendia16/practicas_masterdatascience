FROM continuumio/anaconda3

COPY src/requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

RUN mkdir /app
COPY src /app
RUN chmod -R +rwx /app

WORKDIR /app

EXPOSE 5000

CMD ["python", "app.py"]
