from behave import *

use_step_matcher('re')

@when('I click the link with id "(.*)"')
def step_impl(context,link_id):
    link = context.driver.find_element_by_id(link_id)
    link.click()

