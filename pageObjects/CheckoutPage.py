from selenium.webdriver.common.by import By


class CheckoutPage():

    def __init__(self, driver):
        self.driver = driver

    checkoutproductprice = (By.XPATH,
                            "//div[@class='cart_list']//div[@class='cart_item']//div[@class='cart_item_label']//div[@class='inventory_item_price']")
    totalamount = (By.XPATH, "//div[@class='summary_subtotal_label']")
    tax = (By.XPATH, "//div[@class='summary_tax_label']")
    finishbutton = (By.XPATH, "//a[@class='btn_action cart_button']")
    ordersuccesstext = (By.XPATH, "//h2[@class='complete-header']")
    def checkout_product_price(self):
        return self.driver.find_elements(*CheckoutPage.checkoutproductprice)
        # self.driver.find_elements_by_xpath("//div[@class='cart_list']//div[@class='cart_item']//div[@class='cart_item_label']//div[@class='inventory_item_price']")

    def checkout_totalamount(self):
        return self.driver.find_element(*CheckoutPage.totalamount)

    # self.driver.find_element_by_xpath("//div[@class='summary_subtotal_label']")

    def checkout_tax(self):
        return self.driver.find_element(*CheckoutPage.tax)

    # self.driver.find_element_by_xpath("//div[@class='summary_tax_label']")

    def checkout_finishbutton(self):
        return self.driver.find_element(*CheckoutPage.finishbutton)
    # self.driver.find_element_by_xpath("//a[@class='btn_action cart_button']").click()

    def checkout_ordersuccesstext(self):
        return self.driver.find_element(*CheckoutPage.ordersuccesstext)
    #self.driver.find_element_by_xpath("//h2[@class='complete-header']")
