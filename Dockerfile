FROM python:3.7-slim
RUN apt-get update
WORKDIR /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY app.py model.py model.pkl sales.csv /app/
EXPOSE 8000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]