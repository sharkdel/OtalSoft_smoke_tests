from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = url if url else 'https://sf.leadupcrm.pro/account/signin'
        super().__init__(web_driver, url)

# Указываю локаторы по мере их появления в тестах

    # Авторизация
    name = WebElement(xpath="//input[@name='username']")
    password = WebElement(xpath="//input[@name='password']")
    btn_input = WebElement(xpath="//button[@class='button full']")
    title = WebElement(xpath="//div[@class='header-title']")

    # Создание нового юридического лица
    btn_plus = WebElement(xpath="//div[@class ='add-button-inner']")
    btn_icon_legal_entity = WebElement(xpath="//div[@class='add-button-actions-item company']")
    form_title = WebElement(xpath="//div[@class='popup-title']")
    search_field = WebElement(xpath="//input[@placeholder='Искать по ИНН, ОГРН, названию организации']")
    choose_legal_entity = WebElement(xpath="//div[@class='data-grid-row']")

    short_name = WebElement(xpath="//input[@name='name']")
    btn_save = WebElement(xpath="//button[@class='button']")

    title_page = WebElement(xpath="//div[@class='card-title-text-inner']")
    #t_page = ManyWebElements(xpath="(//div[@class='field-view-value'])[3]")
    add_new_client_in_table = WebElement(xpath="(//div[@class='text'])[5]")
    # Новая вкладка: Клиент • Юридическое лицо
    payment_accounts = WebElement(xpath="//a[@class='tabs-item']")
    btn_new_payment_account = WebElement(xpath="//button[@class='button confirm full']")

    # Добавление нового расчетного счета
    #form_new_payment_account_title = WebElement(xpath="//div[@class='popup-title']")
    field_name = WebElement(xpath="//input[@name='title']")
    bank_payment_account = WebElement(xpath="//input[@placeholder='Наименование банка']")
    bic_payment_account = WebElement(xpath="//input[@placeholder='БИК']")
    inn_payment_account = WebElement(xpath="//input[@name='inn']")
    ogrn_payment_account = WebElement(xpath="//input[@name='ogrn']")
    kpp_payment_account = WebElement(xpath="//input[@placeholder='КПП']")
    account_payment_account = WebElement(xpath="//input[@placeholder='Расчетный счет']")
    correspondent_payment_account = WebElement(xpath="//input[@placeholder='Корреспондентский счет']")
    address_payment_account = WebElement(xpath="//input[@placeholder='Юридический адрес']")

    new_payment_account_title = WebElement(xpath="//div[@class='fieldblock-title']")

    # Добавление новой задачи
    link_tasks = WebElement(xpath="(//a[@class='tabs-item'])[3]")
    task_name = WebElement(xpath="//input[@name='title']")
    task_begin_date = WebElement(xpath="//input[@name='beginDate']")
    task_begin_time = WebElement(xpath="//input[@name='beginTime']")
    task_deadline_date = WebElement(xpath="//input[@name='deadlineDate']")
    task_deadline_time = WebElement(xpath="//input[@name='deadlineTime']")
    task_description = WebElement(xpath="//textarea[@class='customScroll']")
    type_task_select_box = WebElement(xpath="(//div[@class='selectbox-inner'])[2]")
    type_task_select_box_choice = WebElement(xpath="(//div[@class='selectbox-list-item'])[2]")

    name_check = WebElement(xpath="//div[@class='field-view-value']")
    count_tasks1 = WebElement(xpath="((//div[@class='data-grid-counter-item-count']/span)[1]")
    count_tasks = WebElement(xpath="//*[@id='app']/div[1]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/span[1]")
    table_task_name = WebElement(xpath="(//div[@class='link'])[2]")

    # Добавление новой сделки
    link_transactions = WebElement(xpath="(//a[@class='tabs-item'])[4]")
    select_box_client = WebElement(xpath="(//div[@class='selectbox-inner'])[2]")
    select_box_choice_client = WebElement(xpath="(//div[@class='selectbox-list-item'])[1]")
    select_box_client_name = WebElement(xpath="(//div[@class='selectbox-text-value'])[2]")

    # Test add_person

    # Создание нового физического лица
    btn_icon_individual = WebElement(xpath="//div[@class='add-button-actions-item individual']")
    fio_field = WebElement(xpath="//input[@name='fullname']")

    # Test add_businessman

    # Создание нового ИП
    btn_icon_businessman = WebElement(xpath="//div[@class='add-button-actions-item businessman']")
    btn_manually = WebElement(xpath="//button[@class='button']")

    # Test add_product

    # Добавление нового продукта
    link_product = WebElement(xpath="(//span[@class='main-menu-item-text'])[8]")
    header_title = WebElement(xpath="//div[@class='header-title']")
    btn_merchandise = WebElement(xpath="//div[@class='add-button-actions-item-label']")
    field_title = WebElement(xpath="//input[@name='title']")
    field_price = WebElement(xpath="//input[@name='price']")
    select_box_category = WebElement(xpath="//div[@class='selectbox-inner']")
    select_box_choice_category = WebElement(xpath="//div[@class='selectbox-list-item']")
    add_merchandise_in_table = WebElement(xpath="(//div[@class='text'])[9]")



