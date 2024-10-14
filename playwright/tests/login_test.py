from playwright.sync_api import sync_playwright


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Перейти на сторінку логіну
        page.goto('https://www.saucedemo.com/')
        
        # Заповнити форму логіну
        page.fill('input[data-test="username"]', 'standard_user')
        page.fill('input[data-test="password"]', 'secret_sauce')
        page.click('input[data-test="login-button"]')
        
        # Зачекати на завантаження сторінки з товарами
        page.wait_for_selector('h1')
        assert page.is_visible('h1'), 'Логін не вдалася'

        context.close()
        browser.close()


if __name__ == "__main__":
    test_login()
