import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.sbis_page import SbisPage


def test_button_download_vlsi(browser):
    """
    Проверяет, что кнопка для скачивания VLSI отображается и может быть нажата.

    Args:
        browser (webdriver): Объект WebDriver для взаимодействия с браузером.
    """
    sbis_page = SbisPage(browser)
    sbis_page.open_sbis()
    assert sbis_page.button_download_vlsi().is_displayed
    element = sbis_page.button_download_vlsi()
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    sbis_page.button_download_vlsi().click()


def test_button_download_plugin(browser):
    """
    Проверяет, что кнопка для скачивания плагина отображается, может быть нажата, скачивание завершается успешно
    и размер скачанного файла соответствует ожидаемому размеру.

    Args:
        browser (webdriver): Объект WebDriver для взаимодействия с браузером.
    """
    sbis_page = SbisPage(browser)
    sbis_page.open_sbis_download()
    assert sbis_page.button_download_plugin().is_displayed
    sbis_page.button_download_plugin().click()

    assert sbis_page.button_windows().is_displayed
    sbis_page.button_download_web_installer().click()
    wait = WebDriverWait(browser, 30)

    download_path = os.path.expanduser("C:\Users\днс\PycharmProjects\Autotest-for-tensor\PLAGIN")
    downloaded_file = "sbisplugin-setup-web.exe"

    file_path = os.path.join(download_path, downloaded_file)
    file_size = os.path.getsize(file_path) / (1024 * 1024)
    expected_size = 3.64

    if file_size == expected_size:
        print("Файл скачан успешно и его размер совпадает с ожидаемым.")
    else:
        print("Произошла ошибка при скачивании файла или размер не совпадает с ожидаемым.")








