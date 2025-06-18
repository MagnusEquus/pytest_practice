# Используем официальный образ Python
FROM python:3.11-slim

# Создаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект внутрь контейнера
COPY . .

# Команда по умолчанию: запуск pytest
CMD ["pytest"]
