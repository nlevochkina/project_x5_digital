import time

from selene import browser, be


class Page:

    def do_search(self, value):
        browser.element('.products-slider__title').should(be.visible)
        browser.element("[name='search']").click()
        browser.element("[name='search']").should(be.blank).type(value)
        browser.element("button[type='submit']").press_enter()

    def open_profile(self):
        browser.element('a[href="/profile"]').click()

    def check_product(self, value):
        browser.driver.implicitly_wait(20)
        browser.element(f".product-card__title:contains('{value}')")

    def open_card(self):
        browser.element('.product-card__link').click()

    def add_to_cart(self):
        browser.element('#price-card [class*="cart-add-button"]').click()
        time.sleep(5)

    def fill_adress(self):
        browser.element('.delivery-modal__content-container').click()

    def create_account(self):
        browser.element('.login-x5__button.primary').click()

    def check_inactive_button_send_code(self):
        browser.element('.btn-primary.disabled-submit').should(be.visible)

    def fill_phone(self, value):
        browser.element('.input').clear()
        browser.element('.input').should(be.blank).type(value)

    def check_active_button_send_code(self):
        browser.element('.submit-button.btn.btn-primary').should(be.visible)

