## Скачать проект с репозитория

Клонирование репозитоория:

```bash
$ git clone https://github.com/zayycev22/Flower-shop
```


Загрузить изменения с репозитория:

```bash
$ git pull
```

## Venv

Создание Venv'а:

```bash
$ python3 -m venv new_venv
```

Если получаем ошибку:
*"The virtual environment was not created successfully because ensurepip is not available... "*

Нужно дополнительно установить:

```bash
sudo apt-get install python3-venv
```

Вход в *venv*:

```bash
$ source new_venv/bin/activate
```

Для выхода из виртуального окружения *venv* наберите:

```bash
deactivate
```
## Миграция базы данных
```bash
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
## Запуск проекта
```bash
$ python3 manage.py runserver 0.0.0.0:8000
```
## Обновление css
```bash
Для создания css файла npx tailwindcss -i ./static/css/style.css -o ./static/css/output.css --watch
```
