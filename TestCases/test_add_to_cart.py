
from playwright.sync_api import Page,expect
from Pages.loginPage import LoginPage
from Pages.addTocart import AddToCart

def test_add_to_cart(set_up_tear_down):
    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_page = LoginPage(page)

    login_done = login_page.perform_login(credentials)
    expect(login_done.product_header).to_have_text("Products")

    add_to_cart_page = AddToCart(page)
    add_to_cart_page.add_bike_light()

def test_remove_from_cart(set_up_tear_down):
    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_page = LoginPage(page)
    login_done = login_page.perform_login(credentials)
    expect(login_done.product_header).to_have_text("Products")

    add_to_cart_page = AddToCart(page)
    add_to_cart_page.add_bike_light()
    add_to_cart_page.remove_bike_light()