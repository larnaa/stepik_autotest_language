import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_basket_button(browser):
    browser.get(link)
    time.sleep(5)
    try:
        browser.find_element_by_css_selector('.btn-add-to-basket')
    except:
        assert False, "not button 'basket' here"
