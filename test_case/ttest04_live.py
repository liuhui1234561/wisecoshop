#coding = utf-8

from appium import webdriver
from common.desired_caps import *
from common.element_action import *
from common.driverUtil import driver
import unittest

class Live(unittest.TestCase):

    def testLive(self):

        wait_element(By.ID,"com.wiseco.wisecoshop:id/navigation_home_live")
        driver.find_element_by_id("com.wiseco.wisecoshop:id/navigation_home_live").click()


