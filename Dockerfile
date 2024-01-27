FROM python:3.9

WORKDIR /app

RUN apt-get update && \
    apt-get install -y pandoc jupyter

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --deploy --ignore-pipfile --system

COPY . .
   
ENTRYPOINT ["python3", "src/batch_prediction.py"]
