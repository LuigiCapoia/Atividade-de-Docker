FROM python:3.9

RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip install pandas

WORKDIR /teste-python

COPY seu_script.py /app/

CMD ["python", "teste1.py"]
