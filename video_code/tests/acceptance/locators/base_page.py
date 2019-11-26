from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.TAG_NAME,'h1'
    NAVIGATION_LINK = By.ID, 'blog-link'
