#### Зависимости, которые надо установить для работы
* Python version > 3.0
* pip
* virtualenv
* node.js > v6.9
* npm > v3.10

#### Установка (для Windows)
1. git clone https://vtertyshnyi@bitbucket.org/vtertyshnyi/recruitment2.0.git
2. cd recruitment2.0/
3. virtualenv venv
4. cd venv/Scripts
5. activate.bat (и возвращаемся в корень проекта)
6. cd src/
7. pip install -r requirements.txt
8. python manage.py migrate
9. python manage.py createsuperuser (создаем пользователя)
10. python manage.py runserver
11. Переходим по URL 127.0.0.1:8000