from selenium.webdriver.common.by import By


class YaNavLoc:
    class ByCss:
        POPUP_MENU = (By.CSS_SELECTOR, ".input__clear.mini-suggest__input-clear"
                                               ".input__clear_visibility_visible")
        IMAGE_SEARCH_BAR = (By.CSS_SELECTOR, ".input__control")
        IMAGE_CATEGORY = (By.CSS_SELECTOR, ".PopularRequestList-Item")

    class ById:
        SEARCH_BAR = (By.ID, "text")

    class ByClass:
        FULL_SIZE_IMAGE = (By.CLASS_NAME, "MMImageWrapper")
        IMAGE_CATEGORY_TEXT = (By.CLASS_NAME, "PopularRequestList-SearchText")
        IMAGE = (By.CLASS_NAME, "serp-item__preview")
        IMAGE_SRC = (By.CLASS_NAME, "MMImage-Origin")

    class ByXpath:
        SEARCH_MENU_IMAGE = (By.XPATH, "//div[contains(@class,'services-new__list')]"
                                               "/a[contains(@data-id, 'images')]")
        RESULT_LINKS = (By.XPATH, "//h2[contains(@class,'organic__title-wrapper typo "
                                          "typo_text_l typo_line_m')]/a[contains(@href,"
                                          "'http')] ")
        MODAL_NEXT = (By.XPATH, "//div[contains(@class,'MediaViewer-ButtonNext "
                                        "MediaViewer_theme_fiji-ButtonNext')]")
        MODAL_PREV = (By.XPATH, "//div[contains(@class,'MediaViewer-ButtonPrev "
                                        "MediaViewer_theme_fiji-ButtonPrev')]")
