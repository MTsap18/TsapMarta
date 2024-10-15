from pages.home_page import HomePage

def test_homepage(browser):
    page = browser.new_page()
    home_page = HomePage(page)
    home_page.navigate()
    assert "GitHub" in home_page.get_title()  # Перевірка, чи містить заголовок слово "GitHub"
    page.close()




