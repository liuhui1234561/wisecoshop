
from selenium import webdriver
from common.element_action import *
import time

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get("http://47.95.227.133:10443/login")

time.sleep(2)

driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[3]/div[2]/span/span').click()
time.sleep(5)

a = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]').text
print(a)





driver.find_element_by_id("com.wiseco.wisecoshop:id/fragmeng_card_more").click()
print("点击热卡推荐后的更多按钮，进入信用卡列表")

try:
    isElementExist("com.wiseco.wisecoshop:id/card_backname")
    driver.find_element_by_id("com.wiseco.wisecoshop:id/card_backname").click()
    print("点击信用卡列表数据，进入信用卡详情页")
    try:
        isElementExist("com.wiseco.wisecoshop:id/appay")
        print("点击发起申请按钮，进入申请全部数据页面")
        driver.find_element_by_id("com.wiseco.wisecoshop:id/appay").click()

        isElementExist("images")
        if driver.find_element_by_id("images"):
            print("全部数据页面有数据")
        else:
            print("全部数据页面无数据")

        time.sleep(4)
        driver.keyevent(4)
        print("点击返回按钮，回到信用卡详情页面")
    except Exception as e:
        print("信用卡详情页找不到发起申请按钮")

    time.sleep(2)
    driver.keyevent(4)
    print("点击返回按钮，回到信用卡列表页面")

except Exception as e:
    print("信用卡列表未查找到数据")
    print(e)

time.sleep(2)
driver.keyevent(4)
print("点击返回按钮，回到信用卡模块初始页面")

