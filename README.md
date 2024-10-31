# Smoke-tests для проверки пользовательских сценариев в CRM LeadupCRM с использованием Python pytest + Selenium и генерацией отчетов в Allure


Настройка окружения:

1. Создаем виртуальное окружение командой:
    python -m venv venv
2. Активируем виртуальное окружение командой (MacOS/Linux):
    source venv/bin/activate
   для Windows другая команда:
    \venv\Scripts\activate.bat
3. Установка зависимостей:
    pip install -r requirements.txt
4. Настроить в IDE(Pycharm) текущий интерпритатор, выбрав текущее виртуальное окружение


Структура проекта:
Проект содержит следующие файлы:

1. Папка pages
    - auth_page.py - локаторы
    - base_page.py - методы
    - elements.py - методы локаторов
2. Папка tests
    - test_add_businessman.py
    - test_add_legal_entity.py
    - test_add_merchandise.py
    - test_add_person.py
3. Папка screen (содержит скриншоты ошибок)
4. Папка results (результаты генерации allure)
5. Папка allure_report (сгенерированный allure html-отчет)
6. .env — записан логин и пароль
    - name_user = 'имя пользователя'
    - psw_user = 'пароль'
7. requirements.txt — файл с зависимостями.
8. Conftest - настройки webdriver
9. Settigs - переопределие логина и пароля
10. README.md — инструкция по установке и запуску.


Запуск теста:

1. Копируем репозиторий на компьютер
2. Открываем проект в PyCharm
3. Если слева от названия теста нет зеленой стрелочки, значит вы не установили библиотеку pytest.
   Установите командой: pip install pytest.
4. Для генерации allure-отчета запуск теста происходит из терминала.
5. В терминале написать: pytest --browser "название браузера", где
6. Для генерации allure-отчета, в терминале написать: pytest -v -s --alluredir results
7. Для генерации html allure-отчета в терминале написать: allure generate results
   

