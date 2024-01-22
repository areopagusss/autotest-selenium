import logging
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


block_text_sila_v_ludyah_selector = (By.CSS_SELECTOR,
                                    '[class*="tensor_ru-Index__block4-content"] [class*="tensor_ru-Index__card-title"]')

button_cookie_closing_selector = (By.CSS_SELECTOR,
                         '[class="tensor_ru-CookieAgreement__close icon-Close ws-flex-shrink-0 ws-flexbox ws-align-items-center"]')

button_more_detailed_selector = (By.CSS_SELECTOR,
                                 '[href="/about"][class="tensor_ru-link tensor_ru-Index__link"]')

picture_1_selector = (By.CSS_SELECTOR, '[alt="Разрабатываем систему СБИС"]')
picture_2_selector = (By.CSS_SELECTOR, '[alt="Продвигаем сервисы"]')
picture_3_selector = (By.CSS_SELECTOR, '[alt="Создаем инфраструктуру"]')
picture_4_selector = (By.CSS_SELECTOR, '[alt="Сопровождаем клиентов"]')


class TensorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_tensor(self):
        self.browser.get("https://tensor.ru/")

    def open_tensor_about(self):
        self.browser.get("https://tensor.ru/about")

    def text_block_sila_v_ludyah(self):
        return self.find(block_text_sila_v_ludyah_selector)

    def cookie_closing(self):
        cookie_close_button = self.find(button_cookie_closing_selector)
        if cookie_close_button.is_displayed():
            cookie_close_button.click()
            logger.info("Clicked on cookie closing button.")
        else:
            logger.warning("Cookie closing button is not displayed.")

    def button_more_detailed(self):
        return self.find(button_more_detailed_selector)

    def picture_1(self):
        return self.find(picture_1_selector)

    def picture_2(self):
        return self.find(picture_2_selector)

    def picture_3(self):
        return self.find(picture_3_selector)

    def picture_4(self):
        return self.find(picture_4_selector)







