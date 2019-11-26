from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.locators.blog_page import BlogPageLocators

class BlogPage(BasePage):

    def url(self):
        return super(BlogPage,self).url + '/blog'