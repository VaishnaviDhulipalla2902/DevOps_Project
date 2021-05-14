FROM python:3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
WORKDIR /app
ADD . /app
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:9010"]


# docker run --name personal_library -d -p 9010:9010 vaishnavi2902/personal_library:latest
# docker stop <container_id>
# docker start <container_id>