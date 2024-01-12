FROM python:3.11

RUN pip install sqlalchemy fastapi uvicorn scrapy psycopg2 jinja2

WORKDIR /app/src

ENTRYPOINT python reset_db.py && python init_app.py && scrapy runspider --nolog scraper.py && python -m server