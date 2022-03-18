FROM python:3.9-slim

RUN pip install --upgrade pip

ENV PYTHONBUFFERED 1

COPY  requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt \
    && rm -rf /app/requirements.txt

COPY project/blog /app/blog
COPY project/config /app/config
COPY project/scape /app/scape
COPY project/manage.py /app/manage.py
COPY entrypoint.sh /app/entrypoint.sh
COPY project/templates/ /app/templates
COPY project/static/ /app/static
RUN chmod +x /app/entrypoint.sh

WORKDIR /app

ENTRYPOINT ["sh", "entrypoint.sh"]