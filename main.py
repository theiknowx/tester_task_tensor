import unittest
from yandex_pages import TensorOnYandexSearch
from yandex_images import SearchImages


class TestOnYa(unittest.TestCase):
    def setUp(self):
        pass

    def test_search_results(self):
        print("_____________TEST CHECK RESULT OF SEARCHING______________")
        page = TensorOnYandexSearch("https:/yandex.ru/")
        page.go_to_site()
        page.enter_word("Тензор")
        page.check_first_five_result()
        page.close_browser()
        print("_______________________________________")

    def test_image_tab(self):
        print("____________TEST IMAGE TAB_______________")
        image_page = SearchImages("https:/yandex.ru/")
        image_page.go_to_site()
        image_page.check_search_bar()
        image_page.check_menu_images()
        image_page.open_new_tab()
        image_page.open_first_category_of_images()
        image_page.open_image()
        image_page.close_browser()
        print("______________________________________-")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main
