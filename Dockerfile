FROM python:3.8-slim

WORKDIR /app

COPY ./app /app
COPY wait-for-it.sh /wait-for-it.sh

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["./wait-for-it.sh", "db:3306", "--", "flask", "run", "--host=0.0.0.0", "--reload", "--debugger"]

