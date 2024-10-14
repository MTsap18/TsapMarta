from playwright.sync_api import sync_playwright


def test_checkout_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Логін
        page.goto('https://www.saucedemo.com/')
        page.fill('input[data-test="username"]', 'standard_user')
        page.fill('input[data-test="password"]', 'secret_sauce')
        page.click('input[data-test="login-button"]')

        # Додавання товару до кошика
        page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
        
        # Перехід до кошика
        page.locator("[data-test='shopping-cart-link']").click()
        
        # Оформлення замовлення
        page.locator("[data-test='checkout']").click()
        page.fill("[data-test='firstName']", "Іван")
        page.fill("[data-test='lastName']", "Іванов")
        page.fill("[data-test='postalCode']", "12345")
        page.click("[data-test='continue']")
        page.click("[data-test='finish']")
        
        # Перевірка наявності заголовка на головній сторінці
        assert page.is_visible('h1'), 'Перехід до продуктів не вдалася'

        context.close()
        browser.close()


if __name__ == "__main__":
    test_checkout_flow()
