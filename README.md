# Микроблог

## Описание
Учебный проект. Сервис представляет собой микроблог с возможностью регистрации и авторизации, написания постов на своей личной страничке, просмотр постов людей, на которых подписан, т.е. есть возможность подписаться на других людей.
## Требования
* Python 3.13+
* Git
## Работа с проектом 
* Создайте рабочую папку и в ней выполните команду: git clone https://github.com/Olga-who/Flask_book.git
* Сменить папку на Flask_book - cd Flask_book
* Создание  и активация виртуального окружения:
* * python -m venv venv
  * source venv/bin/activate  # для Linux/MacOS
  * venv\Scripts\activate     # для Windows
* Установка зависимостей - pip install -r requirements.txt
* Настройка БД:
* * flask db init
  * flask db migrate
  * flask db upgrade
## Запуск сервиса
flask run или запуск файла begin.py
