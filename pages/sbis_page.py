from pages.base_page import BasePage
from selenium.webdriver.common.by import By


button_contacts_selector = (By.CSS_SELECTOR,
                            'a[href="/contacts"][class*="sbisru-Header__menu-link"]')

button_banner_tensor_selector = (By.CSS_SELECTOR,
                            '[class*="sbisru-Contacts__logo-tensor mb-12 "] [alt="Разработчик системы СБИС — компания «Тензор»"]')

button_area_selector = (By.CSS_SELECTOR,
                     '[class="sbis_ru-Region-Chooser__text sbis_ru-link"]')

button_area_kamchatka_selector = (By.CSS_SELECTOR,
                     '[title="Камчатский край"]')

button_download_vlsi_selector = (By.CSS_SELECTOR,
                     '[href="/download?tab=ereport&innerTab=ereport25"]')

button_download_plagin_selector = (By.CSS_SELECTOR,
                                   '[class*="controls-TabButton__right-align controls-ListView__item undefined"]  ')

button_windows_selector = (By.CSS_SELECTOR,
                     '[class*="controls-TabButton__right-align controls-Checked__checked controls-ListView__item undefined ws-enabled ws-control-inactive "]')

button_download_web_installer_selector = (By.CSS_SELECTOR,
                                          '[href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')

list_of_partners_selector = (By.ID,
                    "contacts_list")

button_download_save_selector = (By.XPATH,
                                          '//*[@id="dangerous"]/span[2]/cr-button')


class SbisPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_sbis(self):
        self.browser.get("https://sbis.ru/")

    def open_sbis_contacts(self):
        self.browser.get("https://sbis.ru/contacts/41-kamchatskij-kraj?tab=partners")

    def open_sbis_download(self):
        self.browser.get("https://sbis.ru/download?tab=ereport&innerTab=ereport25")

    def open_chrome_download(self):
        self.browser.get("chrome://downloads/")

    def button_area(self):
        return self.find(button_area_selector)

    def button_area_kamchatka(self):
        return self.find(button_area_kamchatka_selector)

    def button_contacts_is_displayed(self):
        return self.button_contacts().is_displayed

    def button_contacts(self):
        return self.find(button_contacts_selector)

    def button_banner_tensor(self):
        return self.find(button_banner_tensor_selector)

    def button_download_vlsi(self):
        return self.find(button_download_vlsi_selector)

    def button_download_plugin(self):
        return self.find(button_download_plagin_selector)

    def button_windows(self):
        return self.find(button_windows_selector)

    def button_download_web_installer(self):
        return self.find(button_download_web_installer_selector)

    def button_download_save(self):
        return self.find(button_download_save_selector)

    def list_of_partners(self):
        return self.find(list_of_partners_selector)


