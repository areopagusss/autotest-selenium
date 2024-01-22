from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

button_contacts_selector = (By.CSS_SELECTOR,
                            '[class*="sbisru-Header__menu-item-1 mh-8"]')

button_banner_tensor_selector = (By.CSS_SELECTOR,
                                 '[class="sbisru-Contacts__logo-tensor mb-12"]')

button_area_selector = (By.CSS_SELECTOR,
                        '[class="sbis_ru-Region-Chooser ml-16 ml-xm-0"] [class="sbis_ru-Region-Chooser__text sbis_ru-link"]')

button_area_kamchatka_selector = (By.XPATH,
                                  "//span[@title='Камчатский край' and @class='sbis_ru-link'][contains(text(), '41 Камчатский край')]")

button_download_vlsi_selector = (By.LINK_TEXT,
                                 'Скачать СБИС')

button_download_plagin_selector = (By.CSS_SELECTOR,
                                   '[class*="controls-TabButton__right-align controls-ListView__item undefined"]  ')

button_windows_selector = (By.CSS_SELECTOR,
                           '[class*="controls-TabButton__right-align controls-Checked__checked controls-ListView__item undefined ws-enabled ws-control-inactive "]')

button_download_web_installer_selector = (By.LINK_TEXT,
                                          'Скачать (Exe 7.02 МБ)')

list_of_partners_selector = (By.ID,
                             "contacts_list")

button_download_save_selector = (By.XPATH,
                                 '//*[@id="dangerous"]/span[2]/cr-button')
link_button_selector = (By.CLASS_NAME,
               'state-1')


class SbisPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_url(self, url):
        self.browser.get(url)

    def open_sbis(self):
        self.open_url("https://sbis.ru/")

    def open_sbis_contacts(self):
        self.open_url("https://sbis.ru/contacts/28-amurskaya-oblast?tab=clients")

    def open_sbis_download(self):
        self.open_url("https://sbis.ru/download?tab=ereport&innerTab=ereport25")

    def open_chrome_download(self):
        self.open_url("chrome://downloads/")

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Element with locator {locator} not found on the page."
        )

    def button_area(self):
        return self.find_element(button_area_selector)

    def button_area_kamchatka(self):
        return self.find_element(button_area_kamchatka_selector)

    def button_contacts(self):
        return self.find_element(button_contacts_selector)

    def button_banner_tensor(self):
        return self.find_element(button_banner_tensor_selector)

    def button_download_vlsi(self):
        return self.find_element(button_download_vlsi_selector)

    def button_download_plugin(self):
        return self.find_element(button_download_plagin_selector)

    def button_windows(self):
        return self.find_element(button_windows_selector)

    def button_download_web_installer(self):
        return self.find_element(button_download_web_installer_selector)

    def button_download_save(self):
        return self.find_element(button_download_save_selector)

    def list_of_partners(self):
        return self.find_element(list_of_partners_selector)

    def get_current_url(self):
        return self.browser.current_url

    def get_title_sbis(self):
        return self.find_element(link_button_selector)


