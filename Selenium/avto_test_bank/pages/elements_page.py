import time

from locator.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locator = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locator.FULL_NAME).send_keys('Maksim')
        self.element_is_visible(self.locator.EMAIL).send_keys('Maksim@mail.ru')
        self.element_is_visible(self.locator.CURRENT_ADDRESS).send_keys('Teplichnay_1')
        self.element_is_visible(self.locator.PERMANENT_ADDRESS).send_keys('Teplichnay_1')
        self.element_is_visible(self.locator.SUBMIT).click()
