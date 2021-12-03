FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV APP_DIR /app

COPY . ${APP_DIR}/
WORKDIR ${APP_DIR}

RUN pip install pipenv
RUN pipenv install --skip-lock --deploy --system

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]