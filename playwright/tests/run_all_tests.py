from playwright.sync_api import sync_playwright


def test_login(page):
    page.goto('https://www.saucedemo.com/')
    page.fill('input[data-test="username"]', 'standard_user')
    page.fill('input[data-test="password"]', 'secret_sauce')
    page.click('input[data-test="login-button"]')
    
    # Зачекайте на появу елемента, який підтверджує успішний логін
    page.wait_for_selector('.title')  # Перевіряємо наявність заголовка товарів
    assert page.is_visible('.title'), 'Логін не вдалася'


def test_checkout_flow(page):
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator("[data-test='shopping-cart-link']").click()
    page.locator("[data-test='checkout']").click()
    page.fill("[data-test='firstName']", "Іван")
    page.fill("[data-test='lastName']", "Іванов")
    page.fill("[data-test='postalCode']", "12345")
    page.click("[data-test='continue']")
    page.click("[data-test='finish']")
    assert page.is_visible('.complete-header'), 'Перехід до продуктів не вдалася'


def run_all_tests():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        test_login(page)
        print("Тест логіну пройшов успішно.")
        
        test_checkout_flow(page)
        print("Тест оформлення замовлення пройшов успішно.")

        context.close()
        browser.close()


if __name__ == "__main__":
    run_all_tests()

