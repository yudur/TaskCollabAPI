FROM ghcr.io/owl-corp/python-poetry-base:3.12-slim

WORKDIR /usr/app
COPY . .

RUN poetry install --no-interaction --no-ansi

RUN poetry run prisma generate

EXPOSE 8000

ENTRYPOINT [ "/bin/bash", "-c" ]
CMD [ "poetry run prisma db push --schema prisma/schema.prisma && poetry run uvicorn taskcollabapi.app:app --host 0.0.0.0 --port 8000" ]