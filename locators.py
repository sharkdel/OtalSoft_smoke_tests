from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class Locators(WebPage):

    def __init__(self, web_driver, url=''):
        super().__init__(web_driver, url)
        # url = url if url else 'https://sf.leadupcrm.pro/account/signin'


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

    short_name = WebElement(xpath="//input[@placeholder='Краткое наименование']")
    btn_save = WebElement(xpath="//button[@class='button']")

    title_page = WebElement(xpath="//div[@class='card-title-text-inner']")
    #t_page = ManyWebElements(xpath="(//div[@class='field-view-value'])[3]")

    # Новая вкладка: Клиент • Юридическое лицо
    payment_accounts = WebElement(xpath="//a[@class='tabs-item']")
    btn_new_payment_account = WebElement(xpath="//button[@class='button confirm full']")

    # Добавление нового расчетного счета
    #form_new_payment_account_title = WebElement(xpath="//div[@class='popup-title']")
    name_payment_account = WebElement(xpath="//input[@placeholder='Наименование расчетного счета']")
    bank_payment_account = WebElement(xpath="//input[@placeholder='Наименование банка']")
    bic_payment_account = WebElement(xpath="//input[@placeholder='БИК']")
    inn_payment_account = WebElement(xpath="//input[@placeholder='ИНН']")
    ogrn_payment_account = WebElement(xpath="//input[@placeholder='ОГРН']")
    kpp_payment_account = WebElement(xpath="//input[@placeholder='КПП']")
    account_payment_account = WebElement(xpath="//input[@placeholder='Расчетный счет']")
    correspondent_payment_account = WebElement(xpath="//input[@placeholder='Корреспондентский счет']")
    address_payment_account = WebElement(xpath="//input[@placeholder='Юридический адрес']")

    new_payment_account_title = WebElement(xpath="//div[@class='fieldblock-title']")

    # Добавление новой задачи
    link_tasks = WebElement(xpath="//a[@class='router-link-active router-link-exact-active tabs-item']")
    task_name = WebElement(xpath="//input[@name='title']")
    task_begin_date = WebElement(xpath="//input[@name='beginDate']")
    task_begin_time = WebElement(xpath="//input[@name='beginTime']")
    task_deadline_date = WebElement(xpath="//input[@name='deadlineDate']")
    task_deadline_time = WebElement(xpath="//input[@name='deadlineTime']")
    task_description = WebElement(xpath="//textarea[@class='customScroll']")
    type_task_select_box = WebElement(xpath="(//div[@class='selectbox-inner'])[2]")
    type_task_select_box_choice = WebElement(xpath="(//div[@class='selectbox-list-item'])[2]")

    table_task_name = WebElement(xpath="((//div[@class='link'])[2]")