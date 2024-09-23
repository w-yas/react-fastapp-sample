FROM python:3.10

RUN apt-get update && apt-get install -y python3-venv

WORKDIR /app

RUN python3 -m venv .venv

COPY ./requirements.txt /app/requirements.txt
RUN . .venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# CMD ["sh", "-c", "tail -f /dev/null"]
CMD ["sh", "-c", ". .venv/bin/activate && uvicorn api.main:app --host 0.0.0.0 --port 8000"]
