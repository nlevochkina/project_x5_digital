import allure


@allure.title('Выполнение поиска товара')
def test_search_product(main_page, search_page, open_browser):
    'Открываем сайт магазина Перекрёсток'

    with allure.step('Step 1. Выполняем поиск товара'):
        main_page.do_search('Молоко')

    with allure.step('Step 2. Проверяем что на странице поиска есть товар'):
        search_page.check_product('Молоко питьевое')
