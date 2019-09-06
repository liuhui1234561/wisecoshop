#encoding = utf-8

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.driverUtil import driver
from selenium.common.exceptions import NoSuchElementException
import time



# 显性等待，判断指定时间内元素是否存在，存在返回true，不存在返回false
def isElementExist(element,ele_by=By.ID,timeout=30):
    try:
        WebDriverWait(driver,timeout).until(EC.presence_of_element_located((ele_by,element)))
        return True
    except:
        return False



# 数据校验，先校验列表是否为空，再校验是否出现网络异常错误,最后校验是否一直显示加载中
def dataCheck():
    if isElementExist("com.wiseco.wisecoshop:id/no_data_image", By.ID, 3):
        return False
    elif isElementExist("com.wiseco.wisecoshop:id/net_erroy_image",By.ID,3):
        raise "网络异常，刷新重试了"
        return False
    elif isElementExist("com.wiseco.wisecoshop:id/progressBar",By.ID,3):
        time.sleep(30)
        if isElementExist("com.wiseco.wisecoshop:id/progressBar",By.ID,3):
            raise "页面显示加载中的时长超过35秒"
            return False
    else:
        return True



# 元素存在则执行点击操作，未找到抛出异常
def clickAction(element, ele_by=By.ID):
    try:
        if isElementExist(element):
            findElement(element, ele_by).click()
            time.sleep(2)
            # print("点击元素", element, "成功，进入下一页面")
        else:
            raise "未定位到元素"
    except Exception as e:
        raise "未定位到元素或元素点击操作执行失败"
        raise e



# 列表进详情，详情点击立即申请，并校验下个页面
def listAction(listid, infoid, inid=''):
    time.sleep(2)
    print("点击列表数据，进入详情页")
    clickAction(listid)

    time.sleep(2)
    print("点击发起申请按钮，进入下个页面")
    clickAction(infoid)

    time.sleep(2)
    if inid != '':
        if isElementExist(inid):
            print("跳转页面数据正确")
        else:
            driver.get_screenshot_as_file("../error_pic/info.png")
            raise "未跳转或跳转后页面数据不正确"
    else:
        print("该页面暂未校验")
    time.sleep(2)



# 整个页面使用的是一个table view，而table view里面的空间无法被识别到，无法操作空间，需要使用tap方法模拟用户的点击操作
def target_click(x1,y1):
    x_1 = x1/1080
    y_1 = y1/2280
    x = driver.get_window_size()["width"]
    y = driver.get_window_size()["height"]
    print(x_1*x,y_1*y)
    print("模拟点击操作")
    driver.tap([(x_1*x,y_1*y)],500)     # 模拟单手点击操作


# 页面元素校验，存在则返回True表示页面正常，不存在则返回False表示页面不正常
def pageCheck(element,ele_type=By.ID):
    try:
        if isElementExist(element):
            return True
        else:
            return False
    except Exception as e:
        raise "页面元素" + element + "校验失败" + e


# 元素对应的text校验，一致则返回True，不一致则返回False
def titleCheck(title,element="com.wiseco.wisecoshop:id/bar_tittle",ele_type=By.ID):
    try:
        if findElement(element,ele_type).text == title:
            print("进入的页面title为",title)
            time.sleep(1)
            return True
        else:
            raise "元素未找到"
    except Exception as e:
        raise "元素对应的text与给定的text不一致"



# 获取元素对应的文本并返回
def getText(element):
    return driver.find_element_by_id(element).text


# 页面回退操作
def returnInit(count=1):
    i = 1
    while(count > 0):
        time.sleep(1)
        try:
            print("执行返回操作,第",i,'次操作')
            driver.keyevent(4)
        except Exception as e:
            print("未成功返回到上级页面")
            print(e)

        else:
            time.sleep(2)
            i= i + 1
            count = count - 1


# 查找元素操作，返回元素对象
def findElement(element,ele_by=By.ID):
    """
           查询页面元素，增加显性时间等待机制
           :param ele_type:元素定位方式
           :param value 元素定位属性值
           :return ele(WebElement):返回查找到的元素对象
    """

    ele = None
    try:
        if ele_by == "id":
            ele = driver.find_element_by_id(element)
            return ele
        elif ele_by == "name":
            ele = driver.find_element_by_name(element)
            return ele
        elif ele_by == "link_text":
            ele = driver.find_element_by_link_text(element)
            return ele
        elif ele_by == "partial_link_text":
            ele = driver.find_element_by_partial_link_text(element)
            return ele
        elif ele_by == "tag_name":
            ele = driver.find_element_by_tag_name(element)
            return ele
        elif ele_by == "xpath":
            ele = driver.find_element_by_tag_name(element)
            return ele
        elif ele_by == "class_name":
            ele = driver.find_element_by_class_name(element)
            return ele
        else:
            print("没有这种元素定位方式{}".format(ele_by))
            return ele

    except Exception as e:
        print("未找到响应的元素",e)



# 判断是否存在更新弹窗
def isUpdate(element):
    while(isElementExist(element,By.ID,5)):
        print("存在更新弹窗，关闭")
        driver.find_element_by_id(element).click()
    else:
        print("不存在更新弹窗")



# 封装toast方法实例
def toastCheck(submessage,message):
    target = WebDriverWait(driver, 5, 0.1).until(
        EC.presence_of_element_located(("xpath", "//*[contains(@text,'" + submessage + "')]")))
    print(target.text)
    if target.text == message:
        print("toast提示正确")
    else:
        raise "未捕获到toast提示或者toast提示不正确"





