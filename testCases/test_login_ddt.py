from pageObjects.loginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time
import pytest


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//testData/LoginData.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("**********Test_002_DDT_Login**********")
        self.logger.info("*****Verifying Login Test*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in EXcel:", self.rows)

        lst_status = []

        for row in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', row, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', row, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', row, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("**Passed**")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("**Failed**")
                    self.lp.clickLogout()
                    lst_status.append("fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.driver.save_screenshot(".\\screenshots\\" + "test_login_ddt.png")
                    self.logger.info("**Failed**")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("**Passed**")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT test Passed.......")
            self.driver.close()
            assert True
        else:
            self.logger.error("Login DDT test Failed.......")
            self.driver.close()
            assert False

        self.logger.info("***** End of Login DDT Test *****")
        self.logger.info("***** ***** Completed TC_LoginDDT_002 ***** *****")