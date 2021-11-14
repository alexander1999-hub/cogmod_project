# Простое приложение для распознавания слов

Приложение использует Docker, Flask, PostgreSQL
В качестве модели, распознающей текст, использована модель из репозитория https://github.com/githubharald/SimpleHTR

## Запуск приложения

Запустить приложение можно с помощью команды:
```
docker-compose up
```
Возможна ситуация, что при первом запуске возникают ошибки, связанные с PostgreSQL и сборка зависает на строках

```
...
service3_1  |   File "/script.py", line 13, in <module>
service3_1  |     conn = psycopg2.connect(database="postgres", user="postgres", password="pswd", host="service1", port="5432")
service3_1  |   File "/usr/local/lib/python3.7/site-packages/psycopg2/__init__.py", line 122, in connect
service3_1  |     conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
service3_1  | psycopg2.OperationalError: connection to server at "service1" (172.20.0.2), port 5432 failed: Connection refused
service3_1  | 	Is the server running on that host and accepting TCP/IP connections?
...
...
service2_1  | psql:/init.sql:1: NOTICE:  table "dataset" does not exist, skipping
service2_1  | DROP TABLE
service2_1  | CREATE TABLE
service2_1  | COPY 1
cogmod_project_service2_1 exited with code 0
```
Решить эту проблему можно нажав Сtrl+C и выполнив команду 
```
docker-compose up --build
```

## Использование приложения 
* На странице с адресом '/' отображаются все сохранённые в базу данных распознанные слова.
* Для того, чтобы загрузить картинку с изображением написанного от руки слова, надо перейти на страницу '/upload', нажать на кнопку 'Choose a file', затем на 'Upload'.
* Для того, чтобы сеть распознала слово на загруженной картинке, надо перейти на страницу '/recognize'
* Для того, чтобы увидеть результат работы SimpleHTR, надо перейти на страницу '/'
