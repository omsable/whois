FROM          python:alpine
COPY          app.py /app.py
RUN           pip install pythonwhois
ENTRYPOINT    ["python", "app.py"]
