import allure

from pages.page import Page

page = Page()


@allure.title('Добавляем товар в корзину')
def test_product_add_to_cart(open_browser):
    """Открываем сайт магазина Перекрёсток"""

    with allure.step('Step 1. Выполняем поиск товара'):
        page.do_search('Помидоры')

    with allure.step('Step 2. Проверяем что на странице поиска есть товар'):
        page.check_product('Помидоры')

    with allure.step('Step 3. Открываем страницу товара'):
        page.open_card()

    with allure.step('Step 4. Добавляем товар в корзину'):
        page.add_to_cart()
        with allure.step('Открылось окно с заполнением адреса для доставки'):
            page.fill_adress()
