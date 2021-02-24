FROM python:3.8.7-slim-buster

COPY . .

RUN apt-get update && \
    pip install -r requirements.txt && \
    mkdir /root/.Checkmarx && \
    python3 create_checkmarx_ini_config.py 

RUN echo "PWD is: $PWD"
RUN echo $(ls)

ENTRYPOINT ["python3", "tag_project.py"]
