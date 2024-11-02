from selene import browser


class SearchPage:
    def check_product(self, value):
        browser.driver.implicitly_wait(20)
        browser.element(f".product-card__title:contains('{value}')")

    def open_card(self):
        browser.element('.product-card__link').click()
