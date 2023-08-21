import pytest
import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_exists_button_to_basket_for_any_languages(browser):
    browser.get(link)
    curr_language = browser.execute_script('return window.navigator.language || window.navigator.userLanguage')
    if 'fr' in curr_language:
        time.sleep(30)
    button_basket = browser.find_elements(By.CSS_SELECTOR, '#add_to_basket_form .btn-add-to-basket')
    print("Count ", len(button_basket))
    assert len(button_basket) > 0, 'Не найдена кнопка добавления в корзину'
    assert len(button_basket) < 2, 'Кнопка добавления в корзину не уникальна'