import allure


@allure.title('Добавляем товар в корзину')
def test_product_add_to_cart(main_page, search_page, card_page, open_browser):
    'Открываем сайт магазина Перекрёсток'

    with allure.step('Step 1. Выполняем поиск товара'):
        main_page.do_search('Помидоры')

    with allure.step('Step 2. Проверяем что на странице поиска есть товар'):
        search_page.check_product('Помидоры')

    with allure.step('Step 3. Открываем страницу товара'):
        search_page.open_card()

    with allure.step('Step 4. Добавляем товар в корзину'):
        card_page.add_to_cart()
        with allure.step('Открылось окно с заполнением адреса для доставки'):
            card_page.fill_adress()
