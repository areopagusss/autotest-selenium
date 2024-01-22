import os
import random
import requests
import logging
from pages.sbis_page import SbisPage

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)


def test_button_download_vlsi(browser):
    sbis_page = SbisPage(browser)
    sbis_page.open_sbis()
    assert sbis_page.button_download_vlsi().is_displayed

    logger.info("Кнопка для скачивания VLSI отображается.")

    element = sbis_page.button_download_vlsi()
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    sbis_page.button_download_vlsi().click()


def test_button_download_plugin(browser):
    sbis_page = SbisPage(browser)
    sbis_page.open_sbis_download()
    assert sbis_page.button_download_plugin().is_displayed

    logger.info("Кнопка для скачивания плагина отображается.")

    sbis_page.button_download_plugin().click()
    assert sbis_page.button_windows().is_displayed

    knopka_sbis = sbis_page.button_download_web_installer()
    link = knopka_sbis.get_attribute('href')
    path_name_file = rf'C:\\Users\\днс\\PycharmProjects\\Autotest-for-tensor\\PLAGIN2{random.randint(0, 999)}.exe'

    response = requests.get(link)
    response.raise_for_status()

    with open(path_name_file, 'wb') as file:
        file.write(response.content)
        check_file = os.path.exists(path_name_file)
        file_size_bytes = os.path.getsize(path_name_file)
        file_size_mb = file_size_bytes / (1024 * 1024)
        file_size_mb = (round(file_size_mb, 2))

        logger.info(f"Размер файла: {file_size_mb} МБ")

        expected_size_mb = 7.02
        if file_size_mb == expected_size_mb:
            logger.info("Размер файла соответствует ожидаемому размеру.")
        else:
            logger.warning("Размер файла не соответствует ожидаемому размеру.")

        file.close()
        return check_file








