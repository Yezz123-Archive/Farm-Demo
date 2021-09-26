FROM tiangolo/uvicorn-gunicorn:python3.7

COPY ./backend/requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app/backend

COPY ./backend /app/backend