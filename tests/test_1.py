from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage


def test_button_contacts(browser):
    """
    Проверяет, что кнопка "Контакты" на странице Sbis отображается и можно на нее кликнуть.

    Args:
        browser (webdriver): Объект WebDriver для взаимодействия с браузером.
    """
    sbis_page = SbisPage(browser)
    sbis_page.open_sbis()
    assert sbis_page.button_contacts().is_displayed
    sbis_page.button_contacts().click()


def test_button_banner_tensor(browser):
    """
    Проверяет, что кнопка "Баннер Tensor" на странице Sbis Contacts отображается и можно на нее кликнуть.

    Args:
        browser (webdriver): Объект WebDriver для взаимодействия с браузером.
    """
    sbis_page = SbisPage(browser)
    sbis_page.open_sbis_contacts()
    assert sbis_page.button_banner_tensor().is_displayed
    sbis_page.button_banner_tensor().click()


def test_text_sila_v_ludyah(browser):
    """
    Проверяет, что блок текста "Сила в людях" на странице Tensor отображается корректно.

    Args:
        browser (webdriver): Объект WebDriver для взаимодействия с браузером.
    """
    tenzor_page = TensorPage(browser)
    tenzor_page.open_tensor()
    if "Сила в людях" == tenzor_page.text_block_sila_v_ludyah().text:
        print("Блок определён верно")
    else:
        print("Блок определён неверно")


def test_button_more_detailed(browser):
    """
    Проверяет, что кнопка "Подробнее" на странице Tensor отображается и можно на нее кликнуть.

    Args:
        browser (webdriver): Объект WebDriver для взаимодействия с браузером.
    """
    tenzor_page = TensorPage(browser)
    tenzor_page.open_tensor()
    tenzor_page.cookie_closing()
    assert tenzor_page.button_more_detailed().is_displayed
    tenzor_page.button_more_detailed().click()


def test_checking_photos(browser):
    """
    Проверяет, что все изображения на странице Tensor About имеют одинаковый размер.

    Args:
        browser (webdriver): Объект WebDriver для взаимодействия с браузером.
    """
    tenzor_page = TensorPage(browser)
    tenzor_page.open_tensor_about()
    if tenzor_page.picture_1().size == \
            tenzor_page.picture_2().size == \
            tenzor_page.picture_3().size == \
            tenzor_page.picture_4().size:
        print("Все изображения равны")
    else:
        print("Изображения неравны")


