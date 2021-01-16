from base_page import BasePage
from locators import YaNavLoc
from selenium.webdriver.common.keys import Keys


class TensorOnYandexSearch(BasePage):

    def enter_word(self, text="Тензор"):
        # find element by locator
        search_bar = self.find_element(YaNavLoc.ById.SEARCH_BAR, 3)
        print("search bar was found")
        # send "Тензор"
        search_bar.send_keys(text)
        # check popup menu
        self._check_popup_menu()
        # when send enter
        search_bar.send_keys(Keys.RETURN)

    def _check_popup_menu(self):
        self.find_element(YaNavLoc.ByCss.POPUP_MENU, 3)
        print("popup menu was open")

    def check_first_five_result(self):
        count = 0
        short_list = []
        links_list = self.find_elements(YaNavLoc.ByXpath.RESULT_LINKS)
        if len(links_list) > 5:
            short_list = links_list[:5]

        for link in short_list:
            if str(link.get_attribute('href')).find("tensor.ru") != -1:
                count = + count + 1

        print(f"find {count} matches with tensor.ru")
