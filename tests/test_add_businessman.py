import pytest
from setting import name_user, psw_user
from pages.auth_page import AuthPage
import allure


@allure.feature('add_businessman')
@allure.story("Добавление нового ИП в разделе 'клиенты'")
@pytest.mark.parametrize('name', [name_user], ids=["positive_name"])
@pytest.mark.parametrize('password', [psw_user], ids=["positive_password"])
def test_add_businessman(driver, name, password):

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
    with allure.step("Открытие формы для создания нового ИП."):
        page.btn_plus.click()
        page.btn_icon_businessman.click()
        current_form_title = page.form_title.get_text()
    with allure.step("Проверка, что форма для создания нового ИП открылась."):
        print([current_form_title])
        assert current_form_title == 'Новый индивидуальный предприниматель', 'Ошибка, название формы не совпадает'
    with allure.step("Добавление данных в форму."):
        page.btn_manually.click()
        page.fio_field.click()
        page.fio_field.send_keys('Симонов Петр Иванович')
        page.short_name.click()
        page.short_name.send_keys('Симонов П. И.')
        page.inn_payment_account.click()
        page.inn_payment_account.send_keys('466806489800')
        page.ogrn_payment_account.click()
        page.ogrn_payment_account.send_keys('346545767657889')

    main_tab = driver.current_window_handle
    print(main_tab)
    with allure.step("Сохранение добавленных данных."):
        page.btn_save.click()
        page.wait_page_loaded(5)
        page.fio_field.highlight_and_make_screenshot("../screen/add_businessman_screen1.png")
        list_of_tabs = driver.window_handles
        print(list_of_tabs)
        second_tab = driver.current_window_handle
        print(second_tab)
        # driver.switch_to.window(list_of_tabs[1])  # Подставит дескриптор по индексу 1, т.е второй элемент списка

    with allure.step("Проверка, что данные в открытой вкладке, принадлежат добавленному клиенту."):
        #page.title_page.highlight_and_make_screenshot("../screen/add_businessman_screen2.png")
        get_title_page = page.title_page.get_text()
        #print(get_title_page, 0)
        assert get_title_page == 'Иван Петрович', 'Ошибка, название страницы не совпадает'

    with allure.step("Проверка, что новое физическое лицо добавлено в таблицу."):
        # Проверка, что новое юридическое лицо добавлено в таблицу
        driver.switch_to.window(list_of_tabs[0])
        get_new_client_in_table = page.add_new_client_in_table.get_text()
        assert get_new_client_in_table == 'Иван Петрович', 'Ошибка, название в таблице не совпадает'