# WebWeatherForecastApp

WebWeatherForecastApp - это веб-приложение, которое позволяет пользователю вводить название города и получать прогноз погоды на ближайшее время.

## Используемые технологии

- **FastAPI**: Веб-фреймворк для создания API.
- **Jinja2**: Шаблонизатор для генерации HTML.
- **httpx**: Клиент HTTP для асинхронных запросов.
- **geopy**: Библиотека для геокодирования.
- **Docker**: Контейнеризация приложения.
- **Docker Compose**: Инструмент для запуска многоконтейнерных Docker приложений.

## Запуск приложения

### Локально

1. Убедитесь, что у вас установлен Python3 и выше.
2. Склонируйте репозиторий и перейдите в директорию проекта:

    ```bash
    git clone <URL вашего репозитория>
    cd WebWeatherForecastApp
    ```

3. Создайте виртуальное окружение и активируйте его:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

5. Запустите приложение:

    ```bash
    uvicorn main:app --reload
    ```

6. Приложение будет доступно по адресу `http://localhost:8000`.

### В Docker

1. Убедитесь, что у вас установлены [Docker](https://www.docker.com/get-started) и [Docker Compose](https://docs.docker.com/compose/install/).
2. Склонируйте репозиторий и перейдите в директорию проекта:

    ```bash
    git clone https://github.com/anemon-a/WebWeatherForecastApp.git
    cd WebWeatherForecastApp
    ```

3. Постройте и запустите контейнеры:

    ```bash
    docker-compose up --build
    ```

4. Приложение будет доступно по адресу `http://localhost:8000`

## Что сделано

- Реализовано веб-приложение на FastAPI.
- Используется API для получения прогноза погоды от Open Meteo.
- Вывод данных в удобно читаемом формате.
- Приложение контейнеризировано с помощью Docker.
