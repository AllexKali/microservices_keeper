FROM python:3.12-slim
LABEL authors="naidy_rb5bqow"
WORKDIR /app
#ENTRYPOINT ["python"]
COPY orders.py orders.py
COPY requirements.txt requirements.txt
COPY instance/orders.db orders.db

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5002
# Запускаем приложение
CMD ["python", "orders.py"]