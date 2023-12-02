FROM python:3.8-slim

# Создаем рабочую директорию
WORKDIR /app

# Установка зависимостей
RUN pip install requests

# Копируем исходный Python скрипт, который будет скачивать favicon
COPY favicon.py /app

# Указываем команду, которая будет выполняться при запуске контейнера
CMD ["python", "favicon.py"]