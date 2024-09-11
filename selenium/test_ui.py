from playwright.sync_api import sync_playwright

def test_code():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            page.goto('https://www.saucedemo.com/')

            page.fill('input[name="user-name"]', 'standard_user')
            page.fill('input[name="password"]', 'secret_sauce')
            page.click('input[id="login-button"]')

            page.click('button[name="add-to-cart-sauce-labs-backpack"]')

            page.click('a.shopping_cart_link')

            page.click('button[name="checkout"]')

            page.fill('input[name="firstName"]', 'Михаил')
            page.fill('input[name="lastName"]', 'Горшенев')
            page.fill('input[name="postalCode"]', '2014')

            page.click('input[name="continue"]')

            page.click('button[name="finish"]')

            assert page.inner_text('h2.complete-header').lower() == 'thank you for your order!'.lower()

            print("Успешное выполнение тестирования")

        finally:
            browser.close()

if __name__ == "__main__":
    test_code()
