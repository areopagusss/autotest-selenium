from pages.sbis_page import SbisPage


def test_correct_area(browser):
    """
    Проверяет, что на странице Sbis Contacts корректно определен регион и отображается список партнеров.

    Args:
        browser (webdriver): Объект WebDriver для взаимодействия с браузером.
    """
    sbis_page = SbisPage(browser)
    sbis_page.open_sbis_contacts()

    if "Калининградская обл." == sbis_page.button_area().text:
        print("Ошибки нет")
    else:
        print("Регион определился неверно")

    if sbis_page.list_of_partners().is_displayed:
        print("Партнёры определены")
    else:
        print("Партнёры не определены")


def test_changing_area(browser):
    """
    Проверяет, что на странице Sbis Contacts корректно меняется регион и отображаются партнёры Камчатского края.

    Args:
        browser (webdriver): Объект WebDriver для взаимодействия с браузером.
    """
    sbis_page = SbisPage(browser)
    sbis_page.open_sbis_contacts()
    sbis_page.button_area().click()
    sbis_page.button_area_kamchatka().click()

    if sbis_page.list_of_partners().is_displayed:
        print("Партнёры Камчатского края определены")
    else:
        print("Партнёры Камчатского края не определены")

    if 'Камчатский край' == sbis_page.button_area().text:
        print("В строке 'Выбор региона' указан верный регион")
    else:
        print("В строке 'Выбор региона' указан неверный регион")

    if 'kamchatskij' in browser.current_url.lower():
        print("Url определён верно")
    else:
        print("Url определён неверно")

    if 'Камчатский край' in browser.title:
        print("title определён верно")
    else:
        print("title определён неверно")









