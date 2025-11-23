Тестирование API микросервиса объявлений Авито

Описание
Автоматизированные тесты для REST API микросервиса объявлений Авито.

Эндпоинты
- POST /api/1/item - Создать объявление
- GET /api/1/item/{id} - Получить объявление по ID
- GET /api/1/{sellerID}/item - Получить все объявления продавца  
- GET /api/1/statistic/{id} - Получить статистику по объявлению

Установка

pip install -r requirements.txt


Запуск тестов

Быстрый запуск
python run_tests.py

Или ручной запуск
pytest test_bdd.py -v -s

С HTML отчетом
pytest test_bdd.py -v -s --html=report.html --self-contained-html

Структура проекта

- test_bdd.py - BDD тесты 

- avito_api.feature - сценарии тестирования

- config.py - конфигурация
- run_tests.py - скрипт запуска
- TESTCASES.md - тест-кейсы
- BUGS.md - баг-репорты

Важно!

Некоторые тесты могут показывать FAILED статус из-за багов в API, которые указаны в файле BUGS.md:

GET запросы возвращают 400 вместо ожидаемых 200/404
