FROM python

COPY ./ /app

RUN pip3 install -r /app/requirements.txt

WORKDIR /app
ENTRYPOINT ["python3", "-m", "src.api.api"]