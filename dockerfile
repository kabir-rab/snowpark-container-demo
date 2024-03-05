FROM python:3.11-slim-bookworm
RUN pip install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install -r requirements.txt
# Make port 5000 available to the world outside this container
EXPOSE 5000
CMD ["python3", "app.py"]