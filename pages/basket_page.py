from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
            "Empty basket message is not presented, but should be"
    def should_be_no_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_AT_BASKET), \
            "Goods in basket is presented, but should not be"