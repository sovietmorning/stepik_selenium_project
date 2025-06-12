## :robot: Selenium Web Test Automation: Stepik Course Final Project

Проект создан при выполнении финального задания курса ["Автоматизация тестирования с помощью Selenium и Python"](https://stepik.org/course/575) на платформе Stepik. Реализован для страниц учебного интернет-магазина [Oscar Sandbox](https://selenium1py.pythonanywhere.com/)

#### :white_check_mark: **Стек технологий**

- Pyhton 3.13.0
- Selenium WebDriver 4+
- Pytest (с фикстурами, параметризацией и ожидаемо падающими тестами)

#### :white_check_mark: **Архитектура**

- Паттерн Page Object Model

#### :white_check_mark: **Покрытие тестами**

- Навигация по страницам (login page, main page, product page, basket page) и валидация UI
- Проверка корректности уведомлений после добавления товара в корзину
- Валидация пустой корзины при переходе с главной страницы и со страницы продукта
- Параметризированный тест проверки 10 вариантов промо-предложений в модальных окнах alert (включая xfail-кейс)

#### :white_check_mark: **Команды для запуска тестов**

- запуск всех тестов:
  `pytest -v --tb=line --language=ru`
- запуск тестов с пометкой "need_review":
  `pytest -v --tb=line --language=en -m need_review`
