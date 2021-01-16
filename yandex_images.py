from base_page import BasePage
from locators import YaNavLoc
from selenium.webdriver.support import expected_conditions as EC


class SearchImages(BasePage):

    def check_search_bar(self):
        search_bar = self.find_element(YaNavLoc.ById.SEARCH_BAR)

    def check_menu_images(self):
        image_icon = self.find_element(YaNavLoc.ByXpath.SEARCH_MENU_IMAGE)
        image_icon.click()

    def open_new_tab(self):
        wait = self.wait(10)
        wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait.until(EC.url_contains("https://yandex.ru/images/"), "can't find new tab")

    def open_first_category_of_images(self):
        category = self.find_element(YaNavLoc.ByCss.IMAGE_CATEGORY)
        self.check_status(category, "first category")
        text_category = self.find_element(YaNavLoc.ByClass.IMAGE_CATEGORY_TEXT).text
        category.click()
        self._check_text_search_bar(text_category)

    def _check_text_search_bar(self, text_category):
        search_bar_text = self.find_element(YaNavLoc.ByCss.IMAGE_SEARCH_BAR).get_attribute("value")
        if text_category in search_bar_text:
            print("search bar contains text of first category")
        else:
            print("search bar contains text of first category")

    def open_image(self):
        image = self.find_element(YaNavLoc.ByClass.IMAGE)
        image.click()
        image_before_nav = self._get_src_image()
        self._open_next_image()
        self._open_prev_image()
        image_after_nav = self._get_src_image()
        if image_after_nav in image_before_nav:
            print("Same image")
        else:
            print("Not same image")

    def _open_next_image(self):
        next_btn = self.find_element(YaNavLoc.ByXpath.MODAL_NEXT)
        next_btn.click()

    def _open_prev_image(self):
        next_btn = self.find_element(YaNavLoc.ByXpath.MODAL_PREV)
        next_btn.click()

    def _get_src_image(self):
        return self.find_element(YaNavLoc.ByClass.IMAGE_SRC).get_attribute("src")
