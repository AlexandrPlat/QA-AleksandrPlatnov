﻿# Тесты на проверку параметра name при создании наборов с продуктами в Яндекс.Прилавок с помощью API Яндекс.Прилавок #

Для запуска пакета тестов должны быть установлены: 
- интерпретатор `Python` и среда разработки `PyCharm`
- среда тестирования `Pytest`, библиотека `requests`
- запущен сервер `url.serverhub.praktikum-services.ru` в локальном режиме 
- после запуска сервера url должен быть указан в файле `configuration.py` в следующую строку:
```
URL_SERVICE = 'https://c14b2685-8711-44a1-8cbc-354eb47d4a80.serverhub.praktikum-services.ru'
```

При выполнении каждого теста в этом пакете:
- выполняется запрос на создание нового пользователя и запомнить токен авторизации `authToken`
- выполняется запрос на создание личного набора для этого пользователя. Передача заголовка `Authorization` обязательна

Запуск всех тестов выполняется командой `pytest create_kit_name_kit_test.py`
