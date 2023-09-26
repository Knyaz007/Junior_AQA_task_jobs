# Используем базовый образ Python
FROM python:3.10

# Копируем текущий каталог в /app внутри контейнера
WORKDIR /app
COPY . /app

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Запускаем тесты и сохраняем отчет
CMD ["pytest", "Python_Junior_AQA_task.py", "--html=report.html"]
