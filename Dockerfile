FROM python:alpine
WORKDIR /backend
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["sh", "run.sh"]
