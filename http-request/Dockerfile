FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV TZ Asia/Tokyo

RUN apt-get update
RUN apt-get install -y vim && \
  apt-get install -y curl

# Make working directory.
RUN mkdir /app
WORKDIR /app
ADD . /app

# Install python packages.
RUN pip install -r requirements.txt

CMD ["/bin/bash"]
