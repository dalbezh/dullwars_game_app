# DULLWARS
___

#### Technology stack:
[![Python](https://img.shields.io/badge/python-v3.9-orange)](https://www.python.org/downloads/release/python-394/)
[![Flask](https://img.shields.io/badge/Flask-v2.0.2-blue)](https://flask.palletsprojects.com/en/2.3.x/changes/#version-2-0-2)
___

#### Описание:
Маленькая игра с веб-интерфейсом о битве героев в стиле олдскульных браузерных игр. 
___
#### Локально запустить приложение:

Запуск через Docker Compose:
```shell
docker-compose -f infra/docker-compose.yaml up -d
```
Доступ через браузер:

http://localhost:80
___
#### По структуре приложения:

* Вся логика находится в [/classes](./classes)
    * в [arena.py](./classes/arena.py) игровой процесс
    * в [equipment.py](./classes/equipment.py) всё для экипировки
    * в [skills.py](./classes/skills.py) классы умений
    * в [unit.py](./classes/unit.py) классы юнитов игрока и противника
    * [unit_classes.py](./classes/unit_classes.py) в основном нужен для хранения данных о классе персонажей
* Представления в [app.py](app.py)
* Данные берутся из [JSON файла](./data/equipment.json)
