from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class BasePage():

    def __init__(self, url):
        self.driver = webdriver.Firefox()
        self.base_url = url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        self.driver.get(self.base_url)

    def close_browser(self):
        self.driver.quit()

    def get_title(self):
        print(self.driver.title)

    def check_status(self, web_element, title_element):
        if web_element is not None:
            print(f"The element: {title_element} was found")
        else:
            print(f"The element: {title_element} not found")

    def wait(self, sec=10):
        return WebDriverWait(self.driver, sec)
