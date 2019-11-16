from selenium.webdriver import Chrome
import pytest

def test_DoBrowserTest():
    driver=Chrome(executable_path="chromedriver.exe")

    driver.get("https://www.nopcommerce.com/")

    driver.maximize_window()

    driver.find_element_by_xpath("(//a[normalize-space(text())='Log in'])[1]").click()

def test_Tc_02():
    print("Test Case 2")
    a=10
    exp=20
    assert a==exp,"A is not equal to 20"

def test_Tc_03():
    print("Test Case 03")
