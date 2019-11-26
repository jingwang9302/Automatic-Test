from behave import *
from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')

@then('There is a title on the page')
def step_impl(context):
    page = HomePage(context.driver)
    assert page.title.is_displayed()

@step('Title content is "(.*)"')
def step_impl(context,content):
    page = HomePage(context.driver)
    assert page.title == content