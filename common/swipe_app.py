#cogding = utf-8


import time
from common.driverUtil import driver
from common.element_action import *



# 向上滑动
def swipeToUp(t=500):
    s = driver.get_window_size()
    x = s['width'] * 0.5
    starty = s['height'] * 0.8
    endy = s['height'] * 0.2
    try:
        driver.swipe(x,starty,x,endy,t)
    except Exception as e:
        print(e)

# 向下滑动
def swipeToDown(t=500):
    s = driver.get_window_size()
    x = s['width'] * 0.5
    starty = s['height'] * 0.2
    endy = s['height'] * 0.8
    try:
        driver.swipe(x, starty, x, endy, t)
    except Exception as e:
        print(e)


# 向左滑动
def swipeToLeft(t=500):
    s = driver.get_window_size()
    startx = s['width'] * 0.8
    endx = s['width'] * 0.2
    y = s['height'] * 0.5
    try:
        driver.swipe(startx, y, endx, y, t)
    except Exception as e:
        print(e)



# 向右滑动
def swipeToRight(t=500):
    s = driver.get_window_size()
    startx = s['width'] * 0.2
    endx = s['width'] * 0.8
    y = s['height'] * 0.5
    try:
        driver.swipe(startx, y, endx, y, t)
    except Exception as e:
        print(e)



# 滑动方法，通过参数实现各方向滑动
def swipe(direction,t=500):
    try:
        if direction == 'up':
            swipeToUp()
        elif direction == 'down':
            swipeToDown()
        elif direction == 'left':
            swipeToLeft()
        elif direction == 'ritht':
            swipeToRight()
        else:
            print("没有这种元素定位方式{}".format(direction))

    except Exception as e:
        print(e)



# 在某方向上滑动直至期望的元素出现
def swipeUtilElementAppear(element,direction="up",ele_by=By.ID,t=500):
    flag = True
    i = 1
    while(flag):
        try:
            if ele_by == "id":
                driver.find_element_by_id(element)
                return False
            elif ele_by == "name":
                driver.find_element_by_name(element)
                return False
            elif ele_by == "link_text":
                driver.find_element_by_link_text(element)
                return False
            elif ele_by == "partial_link_text":
                driver.find_element_by_partial_link_text(element)
                return False
            elif ele_by == "tag_name":
                driver.find_element_by_tag_name(element)
                return False
            elif ele_by == "xpath":
                driver.find_element_by_tag_name(element)
                return False
            elif ele_by == "class_name":
                driver.find_element_by_class_name(element)
                return False
            else:
                print("没有这种元素定位方式{}".format(ele_by))
                return False
        except:
            swipe(direction,t)



# 滑动至某元素出现
def swipeEnd(element,direction="up",t=500):
    flag = True
    i = 1
    while(flag and i<=5):
        try:
            # if driver.getPageSource().contains(element):
            if driver.find_element_by_id(element):
                return False

        except:
            swipe(direction, t)
            print("第",i,"次滑动")
            i = i + 1

def swipeTest():
    print(driver.getPageSource())


# 获取应用占屏幕大小
def app_screen():
    return driver.get_window_size()






if __name__ == '__main__':
    print(app_screen())  # 打印一下屏幕尺寸，是一个dict
    time.sleep(5)
    # print("向上滑动操作")
    # swipe('up')
    # time.sleep(3)
    # print("向下滑动操作")
    # swipe('down')
    # time.sleep(5)
    #swipeUtilElementAppear("com.wiseco.wisecoshop:id/textView4",'up')

    swipeEnd("买春节车票必看")

