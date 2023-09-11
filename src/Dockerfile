FROM python:3.9

WORKDIR /code
EXPOSE 80
ENV PORT=80

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./main.py /code/main.py

ENTRYPOINT [ "python", "main.py"]
