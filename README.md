# CatShare

### Описание
CatShare — социальная сеть для обмена фотографиями любимых питомцев. Состоит из бэкенд-приложения на Django и фронтенд-приложения на React. Поддерживает регистрацию и авторизацию, можно добавить нового котика на сайт или изменить существующего, а также просмотреть записи других пользователей.

### Используемые технологии
- Python 3.10
- Django
- Django REST Framework
- Node.js
- React
- Gunicorn
- Nginx
- Docker
- GitHub Actions

### Как развернуть проект локально
1. Клонировать репозиторий:
    ```bash
    git clone git@github.com:monk-time/catshare.git
    cd catshare/
    ```

2. Создать в папке catshare/ файл `.env` с переменными окружения (см. [.env.example](.env.example)).

3. Собрать и запустить докер-контейнеры через Docker Compose:
    ```bash
    docker compose up --build
    ```

### Как развернуть проект на сервере
1. Создать папку catshare/ с файлом `.env` в домашней директории сервера (см. [.env.example](.env.example)).
    ```bash
    cd ~
    mkdir catshare
    nano catshare/.env
    ```
2. Настроить в nginx перенаправление запросов на порт 9000:
    ```nginx
    server {
        server_name <...>;
        server_tokens off;

        location / {
            proxy_pass http://127.0.0.1:9000;
        }
    }
    ```
3. Добавить в GitHub Actions следующие секреты:
    - DOCKER_USERNAME - логин от Docker Hub
    - DOCKER_PASSWORD - пароль от Docker Hub
    - SSH_KEY - закрытый ssh-ключ для подключения к серверу
    - SSH_PASSPHRASE - passphrase от этого ключа
    - USER - имя пользователя на сервере
    - HOST - IP-адрес сервера
    - TELEGRAM_TO - ID телеграм-аккаунта для оповещения об успешном деплое
    - TELEGRAM_TOKEN - токен телеграм-бота
4. При первом коммите в main будет выполнен полный деплой проекта.

### Об авторе
Дмитрий Богорад [@monk-time](https://github.com/monk-time)
