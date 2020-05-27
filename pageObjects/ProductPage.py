from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class ProductPage():

    def __init__(self, driver):
        self.driver = driver

    sortlowprice = (By.XPATH, "//div[@class='inventory_list']//div[1]//div[3]//div[1]")
    sorthighprice = (By.XPATH, "//div[@class='inventory_list']//div[6]//div[3]//div[1]")
    allprice = (By.XPATH,
                "//div[@id='inventory_container']//div//div[@id='inventory_container']//div[@class='inventory_list']//div[@class='inventory_item']//div[3]//div")
    allproducts = (By.XPATH,
                   "//div[@id='inventory_container']//div//div[@id='inventory_container']//div[@class='inventory_list']//div[@class='inventory_item']")
    Addtocart = (By.XPATH,
                 "//div[@id='inventory_container']//div//div[@id='inventory_container']//div[@class='inventory_list']//div[@class='inventory_item']//div[3]//button")
    Carticon = (By.XPATH, "//div[@id='shopping_cart_container']")
    cartitems = (By.XPATH, "//div[@class='cart_list']//div[@class='cart_item']//div[@class='cart_item_label']//a//div")
    checkoutbutton = (By.XPATH, "//a[@class='btn_action checkout_button']")
    userinfofirstname = (By.XPATH, "//input[@id='first-name']")
    userinfolastname = (By.XPATH, "//input[@id='last-name']")
    userinfozipcode = (By.XPATH, "//input[@id='postal-code']")
    userinfocontiuebutton = (By.XPATH, "//input[@class='btn_primary cart_button']")
    dropdown = (By.CLASS_NAME, "product_sort_container")

    def pro_dropdwon(self):
        return self.driver.find_element(*ProductPage.dropdown)

    def sort_lowprice(self):
        return self.driver.find_element(*ProductPage.sortlowprice)
        # self.driver.find_element_by_xpath("//div[@class='inventory_list']//div[1]//div[3]//div[1]")

    def sort_highprice(self):
        return self.driver.find_element(*ProductPage.sorthighprice)
        # self.driver.find_element_by_xpath("//div[@class='inventory_list']//div[6]//div[3]//div[1]")

    def get_allprice(self):
        return self.driver.find_elements(*ProductPage.allprice)
        # self.driver.find_elements_by_xpath("//div[@id='inventory_container']//div//div[@id='inventory_container']//div[@class='inventory_list']//div[@class='inventory_item']//div[3]//div")

    def get_allproducts(self):
        return self.driver.find_elements(*ProductPage.allproducts)

    # self.driver.find_elements_by_xpath("//div[@id='inventory_container']//div//div[@id='inventory_container']//div[@class='inventory_list']//div[@class='inventory_item']")

    def Addtocart_button(self):
        return self.driver.find_elements(*ProductPage.Addtocart)

    # self.driver.find_elements_by_xpath("//div[@id='inventory_container']//div//div[@id='inventory_container']//div[@class='inventory_list']//div[@class='inventory_item']//div[3]//button")

    def cart_icon(self):
        return self.driver.find_element(*ProductPage.Carticon)

    # self.driver.find_element_by_xpath("//div[@id='shopping_cart_container']")

    def cart_items(self):
        return self.driver.find_elements(*ProductPage.allproducts)

    # self.driver.find_elements_by_xpath("//div[@class='cart_list']//div[@class='cart_item']//div[@class='cart_item_label']//a//div")

    def checkout_button(self):
        return self.driver.find_element(*ProductPage.checkoutbutton)

    # self.driver.find_element_by_xpath("//a[@class='btn_action checkout_button']")

    def userinfo_firstname(self):
        return self.driver.find_element(*ProductPage.userinfofirstname)

    # self.driver.find_element_by_xpath("//input[@id='first-name']").send_keys("Candy_Ga")

    def userinfo_lastname(self):
        return self.driver.find_element(*ProductPage.userinfolastname)

    # self.driver.find_element_by_xpath("//input[@id='last-name']").send_keys("Kannadiga")

    def userinfo_Zipcode(self):
        return self.driver.find_element(*ProductPage.userinfozipcode)

    # self.driver.find_element_by_xpath("//input[@id='postal-code']").send_keys("560068")

    def userinfo_continuebutton(self):
        self.driver.find_element(*ProductPage.userinfocontiuebutton).click()
        Checkout_Page = CheckoutPage(self.driver)
        return Checkout_Page
    # self.driver.find_element_by_xpath("//input[@class='btn_primary cart_button']").click()
