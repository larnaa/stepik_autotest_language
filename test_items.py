import time
'''
По умолчанию установлен firefox, так что лучше использовать для запуска команду:
pytest --browser_name=chrome --language=fr test_items.py
'''
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_basket_button(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_element_by_css_selector('.btn-add-to-basket')
