import pytest
import time


def test_add_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    assert browser.find_element_by_css_selector('.btn-add-to-basket'), 'Кнопка не найдена'
