from selene import browser, be


class MainPage:

    def do_search(self, value):
        browser.element('.lazyload-wrapper .section__top .products-slider__title').should(be.visible)
        browser.element(".Input__InputStyled-sc-1kqlv3u-0[name='search']").click()
        browser.element(".Input__InputStyled-sc-1kqlv3u-0[name='search']").should(be.blank).type(value)
        browser.element("button[type='submit']").press_enter()

    def open_profile(self):
        browser.element('a[href="/profile"].sc-eCstlR.jeYPke').click()
