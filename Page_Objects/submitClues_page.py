from Common.base_page import BasePage
from Common.random_str import random_mobile
from Page_Locators import usedCar_indexPage_locators as idx_loc
from Page_Locators import submitClues_page_locators as submit_loc
from Test_Data.submitClues_page_data import *
from time import sleep
import random
class SubmitCluesPage(BasePage):
    def submit_clues(self,vin_number):
        #点击二手车首页的提交线索
        self.wait_ele_visible(idx_loc.link_submit_clues)
        self.click_element(idx_loc.link_submit_clues)
        sleep(2)
        # 输入车牌号
        #点击“请输入车牌号”弹出键盘不稳定，做处理
        while True:
            if self.is_ele_visible(submit_loc.keyboard_exist, times=5):
                print("键盘可见，进行车牌号输入")
                break
                "否则，再次点击直到键盘出现"
            else:
                print("键盘未弹出，点击")
                self.wait_ele_visible(submit_loc.input_car_number)
                self.click_element(submit_loc.input_car_number)
                continue
        sleep(2)
        # 页面键盘输入7位车牌号
        arr = ["0","1","2","3","4","5","6","7","8","9","A","C","D","E","F","G","H","I","J","K","L","M"]
        list = ['B']+random.sample(arr, 6)
        print(list)
        for i in list:
            loc = submit_loc.input_num(i)
            strlist = ''.join(list)
            self.click_element(loc)
        print("输入车牌号完成:{}".format(strlist))
        #输入车架号
        self.wait_ele_visible(submit_loc.input_frame_number)
        self.input_text(submit_loc.input_frame_number,vin_number)
        #点击型号
        self.click_element(submit_loc.link_choice_carModel)
        sleep(2)
        #点击“热”
        # self.wait_ele_visible(submit_loc.button_choice_hotModel)
        # self.click_element(submit_loc.button_choice_hotModel)
        #随机选择车型
        self.wait_ele_visible(submit_loc.choice_model_random)
        self.click_element(submit_loc.choice_model_random)
        sleep(2)
        self.click_element(submit_loc.choice_model_fist)
        sleep(2)
        self.click_element(submit_loc.choice_model_year)
        sleep(2)
        # 输入行驶公里数
        self.wait_ele_visible(submit_loc.input_vehicle_mileage)
        self.input_text(submit_loc.input_vehicle_mileage, '111222')
        sleep(1)
        # 点击首次上牌日期
        self.wait_ele_visible(submit_loc.choice_fist_registeTime)
        self.click_element(submit_loc.choice_fist_registeTime)
        sleep(2)
        # #滑动屏幕选择上牌年份坐标滑动
        # self.driver.swipe(130, 900, 130, 950, 2000)
        #点击完成（坐标点击）,华为手机，分辨率为1080*1812
        size=self.get_size()
        x = int(size["width"] * 0.83)
        y = int(size["height"] * 0.556)
        self.driver.tap([(x,y)],100)
        # self.wait_ele_visible(submit_loc.complete_choice)
        # self.click_element(submit_loc.complete_choice)
        sleep(3)
        # 向上滑屏
        self.swipe_up(size)
        sleep(1)
        #输入车主姓名
        self.wait_ele_visible(submit_loc.input_owner_name)
        self.input_text(submit_loc.input_owner_name,'李教练')
        #输入车主电话号码
        mobile=random_mobile()
        self.click_element(submit_loc.input_owner_mobile)
        self.input_text(submit_loc.input_owner_mobile,mobile)
        #点击提交
        self.wait_ele_visible(submit_loc.button_submit)
        self.click_element(submit_loc.button_submit)
    def submitClue_success_isExit(self):
        if self.is_ele_visible(submit_loc.submitClue_success):
            return True
        else:
            return  False
