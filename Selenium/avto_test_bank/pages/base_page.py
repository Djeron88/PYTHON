from selenium.webdriver.support.ui import  WebDriverWait as wait
from selenium.webdriver.support import  expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        """создаем функцию поиска по локатору с таймом 5
        для того что бы все елементы cnhfybws успели прогрузиться"""

        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout=5):
        """для всех элементов видимости """
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_presents(self, locator, timeout=5):
        """позволяет искать именно по дом дереву какой либо текст и необязательно скролить"""
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_presents(self, locator, timeout=5):
        """"""
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        """элемент не видемый"""
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_visible(self, locator, timeout=5):
        """Элемент кликабельный"""
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        """благодаря этой функции мы будим перемещаться к нужному нам элементу"""
        self.driver.execute_script("argument[0].scrollintoView();", element)
        # execute_script - метод позволяет запускать скрипты