FROM python:3.13
WORKDIR /app

RUN pip install uv
COPY ./pyproject.toml /app/pyproject.toml
RUN  uv sync 

COPY ./ave_test /app/ave_test
COPY ./deployment/logconfig.conf /app/logconfig.conf

EXPOSE 8000

CMD . .venv/bin/activate && gunicorn --log-config /app/logconfig.conf -b "0.0.0.0:8000" -k uvicorn.workers.UvicornWorker  ave_test.main:application

