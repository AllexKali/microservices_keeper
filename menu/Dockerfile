FROM python:3.12-slim
LABEL authors="naidy_rb5bqow"
WORKDIR /app
#ENTRYPOINT ["python"]
COPY menu.py menu.py
COPY requirements.txt requirements.txt
COPY menu.db menu.db

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5003
# Запускаем приложение
CMD ["python", "menu.py"]