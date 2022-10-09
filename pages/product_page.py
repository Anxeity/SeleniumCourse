import math

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        login_link = self.browser.find_element(
            By.XPATH, "//button[@value='Добавить в корзину']")
        login_link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def return_book_name(self):
        book_name = self.browser.find_element(
            *ProductPageLocators.MAIN_BOOK_NAME)
        return book_name.text

    def return_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        return book_price.text

    def should_be_thing_in_basket(self, book_name):
        alert_book_name = self.browser.find_element(
            *ProductPageLocators.ALERT_BOOK_NAME)
        assert book_name == alert_book_name.text, "book name is {}, but alert book name is {}".format(
            book_name, alert_book_name.text)

    def should_be_same_price(self, book_price):
        basket_price = self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE)
        assert basket_price.text == book_price, "basket prise is {}, but book price is {}".format(
            basket_price.text, book_price)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is no presented, but should be"
