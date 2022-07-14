
FROM python:3.8-slim-buster

WORKDIR /pythonflask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /pythonflask

EXPOSE 8080

CMD [ "python3", "main.py" ]

#  syntax=docker/dockerfile:1

# FROM python:3.8

# ADD main.py .

# WORKDIR /app
# COPY . /app
# # COPY requirements.txt .

# # RUN pip install -r requirements.txt
# RUN pip3 install --upgrade pip
# RUN pip3 install Flask 
# RUN pip3 install --upgrade google-cloud-datastore
# RUN pip3 install --upgrade google-cloud

# EXPOSE 5000

# CMD [ "python3", "main.py" ]


