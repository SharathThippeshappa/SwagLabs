import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getlogger()
        Login_Page = LoginPage(self.driver)
        Login_Page.valid_username().send_keys("standard_user")
        Login_Page.invalid_password().send_keys("secret_sauce")
        Product_Page = Login_Page.Login_Button_3()
        element = WebDriverWait(self.driver,10)
        self.VerifyTextPresence("app_logo")
        self.SelectOptionByText(Product_Page.pro_dropdwon(), "Price (low to high)")
        lowpriceproduct = Product_Page.sort_lowprice().text.lstrip("$")
        highpriceproduct = Product_Page.sort_highprice().text.lstrip("$")
        log.info("Lowest Price Product is: "+ lowpriceproduct)
        log.info("Highest Price Product is: "+ highpriceproduct)
        assert float(lowpriceproduct) < float(highpriceproduct)
        self.SelectOptionByIndex(Product_Page.pro_dropdwon(), 3)
        assert float(highpriceproduct) > float(lowpriceproduct)

        allprice = Product_Page.get_allprice()
        for prices in allprice:
            log.info(prices.text.lstrip("$"))

        products = Product_Page.get_allproducts()
        for product in products:
            producName = product.find_element_by_xpath("div[2]//a//div").text
            log.info(producName)
            if producName == "Sauce Labs Backpack":
                product.find_element_by_xpath("div[3]//button").click()

        Addtocart = Product_Page.Addtocart_button()
        Addtocart[3].click()
        time.sleep(1)
        Addtocart[4].click()
        time.sleep(1)
        Addtocart[5].click()
        Product_Page.cart_icon().click()
        self.VerifyTextPresence("cart_desc_label")
        cart_items = Product_Page.cart_items()
        for cart in cart_items:
            log.info(cart.text)
        Product_Page.checkout_button().click()
        element.until(expected_conditions.presence_of_element_located((By.ID, "first-name")))
        Product_Page.userinfo_firstname().send_keys("Candy_Ga")
        Product_Page.userinfo_lastname().send_keys("Kannadiga")
        Product_Page.userinfo_Zipcode().send_keys("560068")
        Checkout_Page = Product_Page.userinfo_continuebutton()
        self.VerifyTextPresence("summary_subtotal_label")
        product_price = Checkout_Page.checkout_product_price()
        sumi = 0
        for amount in product_price:
            amt = amount.text.lstrip("$")
            sumi = sumi + float(amt)
        log.info("Sum of products is: "+ '{0:.2f}'.format(sumi).rstrip('0').rstrip('.'))
        total_Amount = Checkout_Page.checkout_totalamount()
        amt1 = total_Amount.text.lstrip("Item total: $")
        log.info("Item Total is: "+ amt1)
        assert str(sumi) in str(amt1)

        tax = Checkout_Page.checkout_tax()
        tax1 = tax.text.lstrip("Tax: $")
        log.info("Tax applied is: "+ tax1)
        Total = float(sumi) + float(tax1)
        log.info("Total amount is: "+ '{0:.2f}'.format(Total).rstrip('0').rstrip('.'))
        assert float(Total) > float(sumi)

        Checkout_Page.checkout_finishbutton().click()
        self.VerifyTextPresence("complete-header")
        Ordersuccessfull = Checkout_Page.checkout_ordersuccesstext().text
        log.info(Ordersuccessfull)
        assert "THANK" in Ordersuccessfull
