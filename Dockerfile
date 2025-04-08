# Download Base-image
FROM python:3.12-slim-bullseye

WORKDIR /app

COPY . /app

# INSTALL DEPENDECIES
RUN apt-get update
RUN apt-get --assume-yes install gcc

# INSTALL TOOLS
RUN pip install Flask pydantic Flask-Pydantic kafka-python

# Command

EXPOSE 9090

ENTRYPOINT [ "python" ]

CMD ["app.py"]