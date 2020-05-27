import inspect
import logging

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        log = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        log.addHandler(fileHandler)
        log.setLevel(logging.DEBUG)
        return log

    def VerifyTextPresence(self, text): #LinkText, ClassName, Xpath
        wait = WebDriverWait(self.driver, 6)
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, text)))

    def SelectOptionByText(self, locator,text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def SelectOptionByIndex(self, locator,index):
        dropdown = Select(locator)
        dropdown.select_by_index(index)


