FROM python:3.13-slim

ARG PROJECT_PATH=/app
RUN mkdir -p $PROJECT_PATH
WORKDIR $PROJECT_PATH

RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

ADD src $PROJECT_PATH

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
