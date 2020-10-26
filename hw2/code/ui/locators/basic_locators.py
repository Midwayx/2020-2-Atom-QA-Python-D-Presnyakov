from selenium.webdriver.common.by import By


class BasePageLocators:
    AUTH_BUTTON = (By.CLASS_NAME, 'responseHead-module-button-1BMAy4')
    LOGIN = (By.XPATH, '//div[contains(text(),"Войти")]')
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    ACCEPT = (By.CLASS_NAME, 'authForm-module-button-2G6lZu')
    ERROR = (By.XPATH, '//div[contains(text(), "Неверный логин или пароль")]')


class MainPageLocators:
    ERROR = (By.XPATH, '//div[contains(@class, "formMsg_title")]')
    CHECK_AUTH = lambda self, x: (By.XPATH, f'//div[@title="{x}"]')
    ACCESS = (By.XPATH, '//div[@title="anonym.213555@mail.ru"]')
    LOGOUT = (By.XPATH, '//a[@href="/logout"]')
    LOGIN = (By.XPATH, '//div[contains(text(),"Войти")]')
    COMPANY = (By.XPATH, "//a[contains(@class,'center-module-button')]")
    CREATE = (By.XPATH, "//div[contains(text(),'Создать кампанию')]")
    FROM_FILE = (By.XPATH, '//div[contains(text(), "Импорт из файла")]/..')
    INPUT = (By.XPATH, "//div[contains(text(), 'Загрузить файл')/..")
    IMPORT_FILE = (By.XPATH, '//input[@name="import_file"]')
    SUBMIT = (By.XPATH, '//div[contains(text(), "Продолжить")]')
    CREATE_COMPANY_BUTTON = (By.XPATH, '//div[contains(text(), "Создать кампанию")]')
    DELETE = (By.XPATH, "//li[contains(text(), 'Удалить')]")
    FIRST_CREATE = (By.XPATH, '//a[@href="/campaign/new"]')
    ACTIONS = (By.XPATH, '//span[contains(text(), "Действия")]')
    SEARCH_FIELD = (By.XPATH, '//input[contains(@placeholder, "Поиск")]')
    SUCCESS = (By.XPATH, '//span[contains(text(), "из")]/following-sibling::span[text()="1"]')

    def CHECK(self, name):
        return By.XPATH, f'//a[contains(text(),"{name}")]'

    def SETTINGS(self, name):
        return By.XPATH, f'//a[@title="{name}"]/../../following-sibling::div[1]/div'

    def SEARCH_BUTTON(self, name):
        return By.XPATH, f'//span[contains(text(), "{name}")]'



class SegmentPageLocators:

    SEGMENTS = (By.XPATH, '//a[@href="/segments"]')
    CREATE_FIRST = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    CREATE = (By.XPATH, '//div[contains(text(), "Создать сегмент")]')
    APPS = (By.XPATH, '//div[contains(text(),"Приложения и игры в соцсетях")]')
    CHECKBOX = (By.XPATH, '//input[contains(@class, "adding-segments-source__checkbox")]')
    ADD_SEGMENT = (By.XPATH, '//div[contains(text(), "Добавить сегмент")]//..')
    INPUT_FIELD = (By.XPATH, '//input[@type="text" and @maxlength="60"]')
    APPLY = (By.XPATH, '//div[contains(text(), "Создать сегмент")]')
    DELETE = (By.XPATH, '//div[contains(text(), "Удалить")]')

    def NAME_LOCATOR(self, name):
        return By.XPATH, f'//a[@title="{name}"]'

    def X_LOCATOR(self, name):
        return By.XPATH, f'//a[@title="{name}"]//..//../following-sibling::div//span'
