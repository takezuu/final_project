# Поект: "Автоматизация тестов интернет магазина Open cart"

Использованные библиотеки:
Allure,
Pytest,
Requests,
Selenium,
Pytest-xdist

Структура проекта:

Всего в проекте 38 тестов. Тестами было покрыто 7 страниц приложения.
В проекте применен паттерн PageObject для написания тестов. Библиотека Allure
использована для создания отчетности по итогам тестов. Пароли и данные в проекте хранятся
отдельно в файле config.py

Запуск тестов:

Тесты запускаются с помощью pytest с использованием следующих параметров:
1. --base_url - указывается основной адрес приложения
2. --browser_name - указывается браузер для выполнения тестов chrome или firefox
3. --executor - указывается адрес машины, на которой выполняются тесты
4. --bv - указывается версия браузера для выполнения тестов
