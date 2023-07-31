from driver import Driver
from pages.login_page import LoginPage
from pages.scroll_page import ScrollPage


def before_all(context):
    context.browser = Driver()
    context.login_page = LoginPage()
    context.scroll_page = ScrollPage()


def after_all(context):
    context.browser.close()