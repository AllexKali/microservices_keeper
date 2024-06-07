FROM python:3.12-slim
LABEL authors="naidy_rb5bqow"
WORKDIR /app
#ENTRYPOINT ["python"]
COPY autentification.py autentification.py
COPY requirements.txt requirements.txt
COPY roles.db roles.db
COPY users.db users.db
EXPOSE 5001
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "autentification.py"]