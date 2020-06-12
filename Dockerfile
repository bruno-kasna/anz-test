FROM python:3.8.1

WORKDIR /app
COPY myapp /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

ARG VERSION
ARG LAST_COMMIT_SHA

ENV FLASK_APP=/myapp/api.py
ENV VERSION=${VERSION}
ENV LAST_COMMIT_SHA=${LAST_COMMIT_SHA}

EXPOSE 5000
CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "5000"]