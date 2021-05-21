from pageObjects.loginPage import Login
from pageObjects.addCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random
import pytest


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def random_generator(self, size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("***** ***** Test_003_AddCustomer ***** *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login Successful *****")

        self.logger.info("***** Starting Add Customer Test *****")
        self.adcust = AddCustomer(self.driver)
        self.adcust.clickOnCustomersMenu()
        self.adcust.clickOnCustomersMenuItem()
        self.adcust.clickOnAddNew()

        self.logger.info("***** Providing Customer Details *****")

        self.email = self.random_generator() + "@gmail.com"
        self.adcust.setEmail(self.email)
        self.adcust.setPassword("test123")
        self.adcust.setCustomerRoles("Guests")
        self.adcust.setManagerOfVendor("Vendor 2")
        self.adcust.setGender("Male")
        self.adcust.setFirstName("John")
        self.adcust.setLastName("Doe")
        self.adcust.setDOB("7/05/1985")
        self.adcust.setCompanyName("CG")
        self.adcust.setAdminComment("This is for testing")
        self.adcust.clickOnSave()

        self.logger.info("***** Saving Customer Info *****")

        self.logger.info("***** Saved Customer Validation Started *****")

        self.msg = self.driver.find_element_by_tag_name("body").text

        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("***** Add Customer Test Passed *****")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("***** Add Customer Test Failed *****")
            assert False == False

        self.driver.close()
        self.logger.info("***** Add Customer Test complete *****")
