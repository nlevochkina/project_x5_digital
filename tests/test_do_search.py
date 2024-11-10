import allure

from pages.page import Page

page = Page()


@allure.title('Выполнение поиска товара')
def test_search_product(open_browser):
    """Открываем сайт магазина Перекрёсток"""

    with allure.step('Step 1. Выполняем поиск товара'):
        page.do_search('Молоко')

    with allure.step('Step 2. Проверяем что на странице поиска есть товар'):
        page.check_product('Молоко питьевое')
