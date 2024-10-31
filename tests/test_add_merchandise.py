import pytest
from setting import name_user, psw_user
from pages.auth_page import AuthPage
import allure


@allure.feature('add_merchandise')
@allure.story("Добавление нового товара в разделе 'товара, услуги'")
@pytest.mark.parametrize('name', [name_user], ids=["positive_name"])
@pytest.mark.parametrize('password', [psw_user], ids=["positive_password"])
def test_add_merchandise(driver, name, password):

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

    page.link_product.click()
    with allure.step("Проверка, что перешли на страницу 'Товары'"):
        page.btn_plus.click()
        get_header = page.header_title.get_text()
        print(get_header)
        assert get_header == 'Продукты', 'Ошибка, название страницы не совпадает'

    #Добавление товара
    with allure.step("Открытие формы для добавления нового товара."):
        page.btn_plus.click()
        page.btn_merchandise.click()
        current_form_title = page.form_title.get_text()
    with allure.step("Проверка, что форма для добавления нового товара открылась."):
        print(current_form_title)
        assert current_form_title == 'Новый товар', 'Ошибка, название формы не совпадает'
    with allure.step("Добавление данных в форму."):
        page.field_title.click()
        page.field_title.send_keys('Мед горный')
        page.field_price.click()
        page.field_price.send_keys('750')
        page.select_box_category.click()
        page.select_box_category.wait_until_not_visible()
        page.select_box_choice_category.click()
        page.field_title.highlight_and_make_screenshot("../screen/add_merchandise_screen.png")

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
    with allure.step("Проверка, что данные в открытой вкладке, принадлежат добавленному товару."):
        page.title_page.highlight_and_make_screenshot("../screen/add_merchandise_screen1.png")
        get_title_page = page.title_page.get_text()
        print(get_title_page, 0)
        assert get_title_page == 'Мед горный', 'Ошибка, название страницы не совпадает'

    with allure.step("Проверка, что новый товар добавлен в таблицу."):
        # Проверка, что новый товар добавлен в таблицу
        driver.switch_to.window(list_of_tabs[0])
        get_new_merchandise_in_table = page.add_merchandise_in_table.get_text()
        assert get_new_merchandise_in_table == 'Мед горный', 'Ошибка, название в таблице не совпадает'
