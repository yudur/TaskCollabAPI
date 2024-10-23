FROM python:3.12-slim

WORKDIR /usr/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install --ignore-pipfile --deploy --system

COPY . .

EXPOSE 8080

CMD ["pipenv", "run", "start"]