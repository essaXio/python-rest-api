
FROM python:3-onbuild
COPY . /app
WORKDIR /app
EXPOSE 8000

CMD ["gunicorn", "--bind","0.0.0.0:8000","app:app"]


