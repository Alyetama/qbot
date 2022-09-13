FROM python:3.9.14-slim

COPY bot.py db.py requirements.txt app/

RUN pip install -r app/requirements.txt && \
    rm -rf ~/.cache src

ENTRYPOINT ["python", "app/bot.py"]
