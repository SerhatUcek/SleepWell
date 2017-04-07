from sys import platform
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Browser:
    def __enter__(self):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
            "(KHTML, like Gecko) Chrome/15.0.87"
        )
        sarg = ["--load-images=false"]
        self.browser = webdriver.PhantomJS(executable_path=self.browser_platform(),
                                           desired_capabilities=dcap,
                                           service_args=sarg)
        self.browser.implicitly_wait(15)
        self.browser.set_window_size(1920, 1080)
        return self.browser

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.browser.quit()

    @staticmethod
    def browser_platform():
        if platform.startswith('win32'):
            return 'browsers\windows\phantomjs.exe'
        elif platform.startswith('linux'):
            return 'phantomjs'
        elif platform.startswith('darwin'):
            return 'browsers/osx/phantomjs'
