FROM          jfloff/alpine-python:recent
COPY          app.py /app.py
RUN           pip install --upgrade pip && pip install whois
ENTRYPOINT    ["python", "app.py"]
