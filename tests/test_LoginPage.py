import pytest

from TestData.LoginPageData import LoginPageData
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestLoginPage(BaseClass):

    def test_LoginTest(self, getData):
        log = self.getlogger()
        Login_Page = LoginPage(self.driver)
        log.info("UserName is :"+ getData["UserName"])
        Login_Page.valid_username().send_keys(getData["UserName"])
        log.info("PassWord is :" + getData["PassWord"])
        Login_Page.invalid_password().send_keys(getData["PassWord"])
        Login_Page.Login_Button_0().click()
        Validation = Login_Page.Password_validation().text
        print("Error Validation is: ", Validation)
        assert "password " in Validation
        self.driver.refresh()

    @pytest.fixture(params=LoginPageData.test_Homepage_data)
    def getData(self, request):
        return request.param