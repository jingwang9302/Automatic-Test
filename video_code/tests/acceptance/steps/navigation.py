from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    options = Options()
    chromedriver = '/Users/apple/PycharmProjects/Automated_software_testing/video_code/chromedriver'
    context.driver=webdriver.Chrome(chromedriver,chrome_options=options)
    page = HomePage(chromedriver)
    context.driver.get(page.url)

@given('I am on the blog page')
def step_impl(context):
    options = Options()
    chromedriver = '/Users/apple/PycharmProjects/Automated_software_testing/video_code/chromedriver'
    context.driver = webdriver.Chrome(chromedriver, chrome_options=options)
    page = BlogPage(context.driver)
    context.driver.get(page.url)

@then('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(context.driver)
    assert context.driver.current_url == expected_url


@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url
