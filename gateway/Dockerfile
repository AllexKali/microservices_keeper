FROM python:3.12-slim
LABEL authors="naidy_rb5bqow"
WORKDIR /app
#ENTRYPOINT ["python"]
COPY gateway.py gateway.py
COPY requirements.txt requirements.txt
EXPOSE 5000
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "gateway.py"]