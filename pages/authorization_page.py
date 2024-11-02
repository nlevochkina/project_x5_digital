from selene import browser, be


class AuthorizationPage:

    def create_account(self):
        browser.element('.sc-eCstlR.gPywZE.login-x5__button.primary').click()

    def check_inactive_button_send_code(self):
        browser.element('.submit-button.btn.btn-primary.disabled-submit').should(be.visible)

    def fill_phone(self, value):
        browser.element('.input').clear()
        browser.element('.input').should(be.blank).type(value)

    def check_active_button_send_code(self):
        browser.element('.submit-button.btn.btn-primary').should(be.visible)
