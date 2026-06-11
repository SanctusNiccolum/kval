## Команды для работы с проектом

Скачиваем uv
```
pip install uv
```

Инициализация проекта через uv

```
uv init
```

Добавляем нужные зависимости
```
uv add 'название пакетов'
```

## Если не будет uv

```
pip install 'что тебе надо'
```
и не еби мозг виртуальным окружением

## Django

```
django-admin startprojet config
```
изменяешь settings.py, добавляешь подключение к бд. Потом Выносишь нужные переменные в .env. 
```
load_dotenv()

os.getenv('название переменной')
```

Создание приложения
```
python manage.py startapp core
```

Делаешь модельки, миграции, админку и тд

-----
создание админа
```
python manage.py createsuperuser
```

для запуска сервера

```
python manage.py runserver
```

для запуска тестов
```
python manage.py test
```