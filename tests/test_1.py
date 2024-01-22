import logging
import pytest
from selenium.common.exceptions import NoSuchElementException
from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)


@pytest.fixture
def sbis_page(browser):
    return SbisPage(browser)


@pytest.fixture
def tensor_page(browser):
    return TensorPage(browser)


def test_button_contacts(sbis_page):
    try:
        sbis_page.open_sbis()
        logger.info("Проверка отображения кнопки 'Контакты'.")
        assert sbis_page.button_contacts().is_displayed
        sbis_page.button_contacts().click()
    except NoSuchElementException as e:
        pytest.fail(f"Не удалось нажать на кнопку 'Контакты'. Исключение: {e}")


def test_button_banner_tensor(sbis_page):
    try:
        sbis_page.open_sbis_contacts()
        logger.info("Проверка отображения кнопки 'Баннер Тензор'.")
        assert sbis_page.button_banner_tensor().is_displayed
        sbis_page.button_banner_tensor().click()
    except NoSuchElementException as e:
        pytest.fail(f"Не удалось нажать на кнопку 'Баннер Тензор'. Исключение: {e}")


def test_text_sila_v_ludyah(tensor_page):
    try:
        tensor_page.open_tensor()
        logger.info("Проверка правильного отображения блока 'Сила в людях'.")
        assert "Сила в людях" == tensor_page.text_block_sila_v_ludyah().text
        logger.info("Блок определен корректно.")
    except NoSuchElementException as e:
        pytest.fail(f"Не удалось проверить блок 'Сила в людях'. Исключение: {e}")
    except AssertionError as e:
        pytest.fail(f"Блок определен некорректно. Исключение: {e}")


def test_button_more_detailed(tensor_page):
    try:
        tensor_page.open_tensor()
        tensor_page.cookie_closing()
        logger.info("Проверка отображения кнопки 'Подробнее'.")
        assert tensor_page.button_more_detailed().is_displayed
        tensor_page.button_more_detailed().click()
    except NoSuchElementException as e:
        pytest.fail(f"Не удалось нажать на кнопку 'Подробнее'. Исключение: {e}")


def test_checking_photos(tensor_page):
    try:
        tensor_page.open_tensor_about()
        logger.info("Проверка того, что все изображения на странице 'Тензор О компании' имеют одинаковый размер.")
        assert all(img.size == tensor_page.picture_1().size for img in [tensor_page.picture_2(), tensor_page.picture_3(), tensor_page.picture_4()])
        logger.info("Все изображения имеют одинаковый размер.")
    except NoSuchElementException as e:
        pytest.fail(f"Не удалось проверить изображения на странице 'Тензор О компании'. Исключение: {e}")
    except AssertionError as e:
        pytest.fail(f"Изображения имеют разный размер. Исключение: {e}")

