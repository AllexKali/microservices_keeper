FROM python:3.12-slim
LABEL authors="naidy_rb5bqow"
WORKDIR /app
#ENTRYPOINT ["python"]
COPY finance.py finance.py
COPY requirements.txt requirements.txt
COPY model.py model.py
COPY transactions.db transactions.db
EXPOSE 5004
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "finance.py"]