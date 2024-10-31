import pytest
from setting import name_user, psw_user
from pages.auth_page import AuthPage
import allure


@allure.feature('add_legal_entity')
@allure.story("Добавление нового юридического лица в разделе 'клиенты'")
@pytest.mark.parametrize('name', [name_user], ids=["positive_name"])
@pytest.mark.parametrize('password', [psw_user], ids=["positive_password"])
def test_add_legal_entity(driver, name, password):

    # Авторизация в системе с валидными данными
    with allure.step("Авторизация в системе"):
        page = AuthPage(driver)
        page.name.send_keys(name)
        page.password.send_keys(password)
        page.btn_input.click()
        catalog_title = page.title.get_text()

    # Проверка, что авторизация прошла успешно
    with allure.step("Проверка авторизации"):
        assert page.get_current_url() == "https://sf.leadupcrm.pro/service/clients", 'Ошибка, URL не совпадают'
        print('\n', "URL корректа")
        assert catalog_title == 'Клиенты', 'Название раздела не совпадает'
        print(catalog_title, '== Клиенты')
        print("Авторизация прошла успешно")

    #Создание нового юридического лица
    with allure.step("Открытие формы для создания нового юридического лица."):
        page.btn_plus.click()
        page.btn_icon_legal_entity.click()
        current_form_title = page.form_title.get_text()
    with allure.step("Проверка, что форма для добавления нового юридического лица открылась."):
        print([current_form_title])
        assert current_form_title == 'Новое юридическое лицо', 'Ошибка, название формы не совпадает'
    with allure.step("Добавление данных в форму."):
        page.search_field.click()
        page.search_field.send_keys('ПАО "ТГК-1"')
        page.search_field.click()
        page.choose_legal_entity.wait_until_not_visible()
        print(page.choose_legal_entity.get_text())
        page.choose_legal_entity.click()
        page.short_name.highlight_and_make_screenshot("../screen/screen.png")
    #Форма не отдает вносимые данные. Поэтому проверка скриншотом.
    #page.short_name.click()
    # get_short_name = page.short_name.get_text()
    # print(get_short_name)
    # assert get_short_name == 'Новое юридическое лицо', 'Ошибка, название формы не совпадает'
    main_tab = driver.current_window_handle
    print(main_tab)
    with allure.step("Сохранение добавленных данных."):
        page.btn_save.click()
        page.wait_page_loaded(5)
        list_of_tabs = driver.window_handles
        print(list_of_tabs)
        second_tab = driver.current_window_handle
        print(second_tab)
        driver.switch_to.window(list_of_tabs[1])  # Подставит дескриптор по индексу 1, т.е второй элемент списка
    with allure.step("Проверка, что данные в открытой вкладке, принадлежат добавленному клиенту."):
        page.title_page.highlight_and_make_screenshot("../screen/screen1.png")
        get_title_page = page.title_page.get_text()
        print(get_title_page)
        assert get_title_page == 'ПАО "ТГК-1"', 'Ошибка, название страницы не совпадает'

    with allure.step("Проверка, что новое юридическое лицо добавлено в таблицу."):
        # Проверка, что новое юридическое лицо добавлено в таблицу
        driver.switch_to.window(list_of_tabs[0])
        get_new_client_in_table = page.add_new_client_in_table.get_text()
        assert get_new_client_in_table == 'ПАО "ТГК-1"', 'Ошибка, название в таблице не совпадает'

    driver.switch_to.window(list_of_tabs[1])

    with allure.step("Переход на вкладку добавление расчетного счета для нового юридического лица."):
        # Добавление расчетного счета для нового юридического лица
        page.payment_accounts.click()
        page.btn_new_payment_account.click()
        current_form_title = page.form_title.get_text()
    with allure.step("Проверка, что открыта форма расчетного счета."):
        print(current_form_title)
        assert current_form_title == 'Новый расчетный счет', 'Ошибка, название формы не совпадает'
    with allure.step("Добавление данных расчетного счета для нового юридического лица."):
        page.field_name.click()
        page.field_name.send_keys('Новый расчетный счет')
        page.bank_payment_account.click()
        page.bank_payment_account.send_keys('ВТБ')
        page.bic_payment_account.click()
        page.bic_payment_account.send_keys('123456789')
        page.inn_payment_account.click()
        page.inn_payment_account.send_keys('1234567891')
        page.ogrn_payment_account.click()
        page.ogrn_payment_account.send_keys('1234567890123')
        page.kpp_payment_account.click()
        page.kpp_payment_account.send_keys('123456789')
        page.account_payment_account.click()
        page.account_payment_account.send_keys('12345678901234567890')
        page.correspondent_payment_account.click()
        page.correspondent_payment_account.send_keys('12345678901234567890')
        page.address_payment_account.click()
        page.address_payment_account.send_keys('12345, Mira')
    with allure.step("Проверка, что данные успешно сохранились."):
        page.btn_save.click()
        account_title = page.new_payment_account_title.get_text()
        print(account_title)
        assert account_title == 'Новый расчетный счет', 'Ошибка, название формы не совпадает'

    with allure.step("Добавление новой задачи."):
        # Добавление новой задачи
        page.link_tasks.click()
        page.btn_plus.click()
        current_form_title = page.form_title.get_text()
    with allure.step("Проверка, что открыта форма для добавления новой задачи."):
        print(current_form_title)
        assert current_form_title == 'Новая задача', 'Ошибка, название формы не совпадает'
    with allure.step("Внесение данных по новой задаче."):
        page.field_name.click()
        page.field_name.send_keys('Заключить договор с ООО "ГКП №1"')
        page.task_begin_date.click()
        page.task_begin_date.send_keys('19112024')
        page.task_begin_time.click()
        page.task_begin_time.send_keys('1200')
        page.task_deadline_date.click()
        page.task_deadline_date.send_keys('21112024')
        page.task_deadline_time.click()
        page.task_deadline_time.send_keys('1200')
        page.task_description.click()
        page.task_description.send_keys('Сроки заключения договора')
        page.type_task_select_box.click()
        page.type_task_select_box_choice.click()
        page.btn_save.click()

    with allure.step("Проверка, что данные сохранились."):    
        # Проверка, что задача добавлена
        page.wait_page_loaded(5)
        list_of_tabs = driver.window_handles
        print(list_of_tabs)
        third_tab = driver.current_window_handle
        print(third_tab)
        driver.switch_to.window(list_of_tabs[2])  # Подставит дескриптор по индексу 1, т.е второй элемент списка
        page.title_page.highlight_and_make_screenshot("../screen/screen2.png")
        get_name = page.name_check.get_text()
        print(get_name)
        assert get_name == 'Заключить договор с ООО "ГКП №1"', 'Ошибка, название страницы не совпадает'

    with allure.step("Проверка, что новая задача для юридического лица добавлена в таблицу."):
        # Проверка, что новая задача для юридического лица добавлена в таблицу
        driver.switch_to.window(list_of_tabs[1])
        driver.refresh()
        get_count_tasks = page.count_tasks.get_attribute("textContent")
        print(get_count_tasks)
        #assert get_new_task_in_table == 'ПАО "ТГК-1"', 'Ошибка, название в таблице не совпадает'
        get_new_task_in_table = page.table_task_name.get_text()
        page.title_page.highlight_and_make_screenshot("../screen/screen3.png")
        assert get_new_task_in_table == 'Заключить договор с ООО "ГКП №1"', 'Ошибка, название в таблице не совпадает'

    #driver.switch_to.window(list_of_tabs[1])

    with allure.step("Добавление новой сделки."):
    # Добавление новой сделки
        page.link_transactions.click()
        page.btn_plus.click()
        current_form_title = page.form_title.get_text()
    with allure.step("Проверка, что форма открылась."):
        print(current_form_title)
        assert current_form_title == 'Новая сделка', 'Ошибка, название формы не совпадает'
        page.field_name.click()
        page.field_name.send_keys('Закупка горного меда')
        page.select_box_client.click()
        page.select_box_choice_client.wait_until_not_visible()
        page.select_box_choice_client.click()
        client_name = page.select_box_client_name.get_text()
        print(client_name)
        page.btn_save.click()

    with allure.step("Проверка, что данные добавились."):
        # Проверка, что сделка добавлена
        page.wait_page_loaded(5)
        list_of_tabs = driver.window_handles
        print(list_of_tabs)
        third_tab = driver.current_window_handle
        print(third_tab)
        driver.switch_to.window(list_of_tabs[3])  # Подставит дескриптор по индексу 1, т.е второй элемент списка
        page.title_page.highlight_and_make_screenshot("../screen/screen4.png")
        get_name = page.name_check.get_text()
        print(get_name)
        assert get_name == 'Закупка горного меда', 'Ошибка, название страницы не совпадает'

    with allure.step("Проверка, что новая задача для юридического лица добавлена в таблицу."):
        # Проверка, что новая задача для юридического лица добавлена в таблицу
        driver.switch_to.window(list_of_tabs[1])
        get_count_tasks = page.count_tasks.get_text()
        print(get_count_tasks)
        # assert get_new_task_in_table == 'ПАО "ТГК-1"', 'Ошибка, название в таблице не совпадает'
        get_new_task_in_table = page.table_task_name.get_text()
        page.title_page.highlight_and_make_screenshot("../screen/screen5.png")
        assert get_new_task_in_table == 'Закупка горного меда', 'Ошибка, название в таблице не совпадает'
