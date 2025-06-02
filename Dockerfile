# syntax=docker/dockerfile:1.4
FROM python:3.10-alpine AS builder

WORKDIR /app
EXPOSE 80 

COPY requirements.txt /app
# RUN --mount=type=cache,target=/root/.cache/pip \
#     pip3 install -r requirements.txt

RUN pip3 install -r requirements.txt

COPY ./app /app

ENTRYPOINT ["python3"]
CMD ["app.py"]
