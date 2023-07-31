from behave import *

@given('I am on the scroll page')
def step_impl(context):
    context.scroll_page.navigate_to_page()