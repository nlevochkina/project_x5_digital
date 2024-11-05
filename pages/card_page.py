import time

from selene import browser


class CardPage:

    def add_to_cart(self):
        browser.element('#price-card [class*="cart-add-button"]').click()
        time.sleep(5)

    def fill_adress(self):
        browser.element('.delivery-modal__content-container').click()
