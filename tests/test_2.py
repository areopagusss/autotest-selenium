import logging
import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.sbis_page import SbisPage

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)


@pytest.fixture
def sbis_page(browser):
    sbis_page = SbisPage(browser)
    sbis_page.open_sbis_contacts()
    return sbis_page


def test_correct_area(sbis_page):
    try:
        logger.info("Проверка правильности определения области на странице Sbis Contacts.")
        assert "Калининградская обл." == sbis_page.button_area().text
        logger.info("Ошибок нет.")

        assert sbis_page.list_of_partners().is_displayed
        logger.info("Партнеры определены.")
    except AssertionError as e:
        logger.error(f"Проверка не удалась: {e}")
        pytest.fail("Тест неудачен из-за ошибки проверки.")


def test_changing_area(sbis_page):
    sbis_page.button_area().click()
    sbis_page.button_area_kamchatka().click()
    time.sleep(5)

    try:
        logger.info("Проверка правильности изменения региона на странице Sbis Contacts.")
        assert sbis_page.list_of_partners().is_displayed
        logger.info("Партнеры Камчатского края определены.")

        assert 'Камчатский край' == sbis_page.button_area().text
        logger.info("Правильный регион указан в строке 'Выбор региона'.")

        assert 'kamchatskij' in sbis_page.get_current_url().lower()
        logger.info("URL определен правильно.")

        assert 'СБИС Контакты — Камчатский край' in sbis_page.get_title_sbis().get_attribute('innerText')
        logger.info("Заголовок определен правильно.")
    except AssertionError as e:
        logger.error(f"Проверка не удалась: {e}")
        pytest.fail("Тест неудачен из-за ошибки проверки.")









