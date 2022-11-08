FROM python:latest
COPY ./ /bot
WORKDIR /bot

RUN pip install -r requirements.txt

CMD python main.py

