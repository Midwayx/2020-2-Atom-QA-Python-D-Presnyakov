from selenium.common.exceptions import TimeoutException
from ui.locators.basic_locators import SegmentPageLocators

from ui.pages.base_page import BasePage


class SegmentPage(BasePage):
    locator = SegmentPageLocators()

    def create_segment(self, name):
        self.click(self.locator.SEGMENTS)
        try:
            self.click(self.locator.CREATE)
        except TimeoutException:
            self.click(self.locator.CREATE_FIRST)
        self.click(self.locator.APPS)
        self.click(self.locator.CHECKBOX)
        self.click(self.locator.ADD_SEGMENT)
        element = self.find(self.locator.INPUT_FIELD)
        element.clear()
        element.send_keys(name)
        self.click(self.locator.APPLY)

    def delete_segment(self, name):
        self.click(self.locator.X_LOCATOR(name))
        self.click(self.locator.DELETE)


