FROM python:3.7
WORKDIR /app
ADD . /app
RUN pip install requests
CMD ["python", "app.py"]
