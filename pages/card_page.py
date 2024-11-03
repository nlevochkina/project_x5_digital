from selene import browser

class CardPage:

    def add_to_cart(self):
        browser.element('.sc-eCstlR.gPywZE.cart-add-button').click()

