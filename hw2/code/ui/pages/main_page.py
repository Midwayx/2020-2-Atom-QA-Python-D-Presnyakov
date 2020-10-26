from selenium.common.exceptions import TimeoutException
from ui.locators.basic_locators import MainPageLocators
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    locator = MainPageLocators()

    def create_company(self, path):
        self.click(self.locator.COMPANY)
        try:
            self.click(self.locator.FIRST_CREATE)
        except TimeoutException:
            self.click(self.locator.CREATE)
        self.click(self.locator.FROM_FILE)
        a = self.find(self.locator.IMPORT_FILE)
        a.send_keys(path)
        self.click(self.locator.SUBMIT)
        self.click(self.locator.CREATE_COMPANY_BUTTON)

    def delete_company(self, name):
        self.click(self.locator.SETTINGS(name), timeout=12)
        self.click(self.locator.DELETE, timeout=12)

    def check_company_created(self, name):
        self.find(self.locator.SEARCH_FIELD, timeout=12).send_keys(name)
        self.click(self.locator.SEARCH_BUTTON(name), timeout=12)
        self.find(self.locator.SUCCESS, timeout=12)

