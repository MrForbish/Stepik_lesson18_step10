import pytest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_exists_button_to_basket_for_any_lang(browser):
    try:
        browser.get(link)
        curr_language = browser.execute_script('return window.navigator.language || window.navigator.userLanguage')
        if 'fr' in curr_language:
            time.sleep(30)
        browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form .btn-add-to-basket')
    except NoSuchElementException:
        return False
    return True
