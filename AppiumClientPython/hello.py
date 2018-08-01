# coding=utf-8

from appium import webdriver
import time


desired_caps = {}

desired_caps['platformName'] = 'Android'

desired_caps['deviceName'] = 'MI 4LTE'

desired_caps['appPackage'] = 'com.jijindou.android.fund'

desired_caps['appActivity'] = 'com.talicai.fund.activity.SplashActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(15)

driver.swipe(910,1200,100,1200)

time.sleep(2)

driver.swipe(910,1200,100,1200)

driver.find_element_by_id('com.jijindou.android.fund:id/item_splash_bt_experience').click()

time.sleep(10)

driver.quit()