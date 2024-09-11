from playwright.sync_api import sync_playwright

def test_code():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            # Переход на сайт
            page.goto('https://www.saucedemo.com/')

            # Авторизация
            page.fill('input[name="user-name"]', 'standard_user')
            page.fill('input[name="password"]', 'secret_sauce')
            page.click('input[id="login-button"]')

            # Добавление товара в корзину
            page.wait_for_selector('button[name="add-to-cart-sauce-labs-backpack"]')
            page.click('button[name="add-to-cart-sauce-labs-backpack"]')

            # Переход в корзину
            page.wait_for_selector('a.shopping_cart_link')
            page.click('a.shopping_cart_link')

            # Оформление заказа
            page.wait_for_selector('button[name="checkout"]')
            page.click('button[name="checkout"]')

            # Заполнение данных для доставки
            page.fill('input[name="firstName"]', 'Михаил')
            page.fill('input[name="lastName"]', 'Горшенев')
            page.fill('input[name="postalCode"]', '2014')

            # Продолжение оформления
            page.wait_for_selector('input[name="continue"]')
            page.click('input[name="continue"]')

            # Завершение заказа
            page.wait_for_selector('button[name="finish"]')
            page.click('button[name="finish"]')

            # Проверка успешности завершения покупки
            page.wait_for_selector('h2.complete-header')
            assert page.inner_text('h2.complete-header').lower() == 'thank you for your order!'.lower()

            print("Успешное выполнение тестирования")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            browser.close()

if __name__ == "__main__":
    test_code()
