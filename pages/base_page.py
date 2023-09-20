class BasePage:
    def __init__(self, browser, url=''):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)
