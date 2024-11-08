import allure


@allure.title('Заполняем поле телефон на экране авторизации')
def test_fill_phone(page, open_browser):
    """Открываем сайт магазина Перекрёсток"""

    with allure.step('Step 1. Открываем страницу авторизации'):
        page.open_profile()

    with allure.step('Step 2. Нажимаем на кнопку Войти или создать X5ID'):
        page.create_account()

    with allure.step('Step 3. Проверяем, что кнопка Отправить код неактивна'):
        page.check_inactive_button_send_code()

    with allure.step('Step 4. Вводим номер телефона'):
        page.fill_phone('9150003000')

    with allure.step('Step 5. Проверяем, что кнопка Отправить код стала активна'):
        page.check_active_button_send_code()
