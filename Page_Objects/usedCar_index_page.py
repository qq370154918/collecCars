from Common.base_page import BasePage
from Page_Locators import commenpage_locators as com_loc
from time import sleep
class UsedCarIndexPage(BasePage):
    def switchTo_workSpace(self):
        #等待工作台
        self.wait_ele_visible(com_loc.tab_workSpace)
        #点击工作台
        self.click_element(com_loc.tab_workSpace)
        sleep(2)
    def swichTo_usedCar(self):
        "如果“二手车”元素可见"
        while True:
            if  self.is_ele_visible(com_loc.link_used_car,times=5):
                print("‘【立新出行】二手车’元素可见，点击")
                # self.wait_ele_visible(com_loc.link_used_car)
                # 点击二手车
                self.click_element(com_loc.link_used_car)
                break
                "否则，滚动屏幕"
            else:
                print("二手车“服务商”元素不可见，开始滑屏操作")
                size=self.get_size()
                self.swipe_up(size,time=2000)
                print("继续查找二手车（服务商）")
                sleep(3)
                continue
        sleep(5)
        #点击演示店1
        # self.wait_ele_visible(com_loc.choice_store)
        # self.click_element(com_loc.choice_store)