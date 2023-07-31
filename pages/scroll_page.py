from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ScrollPage(BasePage):

    SCROLL_PAGE_URL = "https://the-internet.herokuapp.com/infinite_scroll"
    TITLE_ELEMENT = (By.CSS_SELECTOR, "h3")
    CONTENT_ELEMENT = (By.CLASS_NAME, "row")

    def navigate_to_page(self):
        self.driver.get(self.SCROLL_PAGE_URL)

    def get_title_text(self):
        return self.get_element_text(self.TITLE_ELEMENT)
