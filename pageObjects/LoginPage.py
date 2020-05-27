from selenium.webdriver.common.by import By

from pageObjects.ProductPage import ProductPage


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    validusername = (By.XPATH, "//input[@id='user-name']")
    invalidpassword = (By.XPATH, "//input[@id='password']")
    Loginbutton = (By.XPATH, "//input[@class='btn_action']")
    passwordValidation = (By.XPATH, "//h3[1]")
    Invalidusername = (By.XPATH, "//input[@id='user-name']")
    validpassword = (By.XPATH, "//input[@id='password']")
    Loginbutton1 = (By.XPATH, "//input[@class='btn_action']")
    usernameValidation = (By.XPATH, "//h3[1]")
    usernamepasswordvalidation = (By.XPATH, "//h3[1]")

    def valid_username(self):
        return self.driver.find_element(*LoginPage.validusername)
    #self.driver.find_element_by_xpath("//input[@id='user-name']")

    def invalid_password(self):
        return self.driver.find_element(*LoginPage.invalidpassword)
    #self.driver.find_element_by_xpath("//input[@id='password']")

    def Login_Button_0(self):
        return self.driver.find_element(*LoginPage.Loginbutton)
    #self.driver.find_element_by_xpath("//input[@class='btn_action']")

    def Password_validation(self):
        return self.driver.find_element(*LoginPage.passwordValidation)
    #self.driver.find_element_by_xpath("//h3[1]")

    def Login_Button_3(self):
        self.driver.find_element(*LoginPage.Loginbutton1).click()
        Product_Page = ProductPage(self.driver)
        return Product_Page
    #self.driver.Product_Page("//input[@class='btn_action']")
