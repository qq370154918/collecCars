from Common.base_page import BasePage
from time import sleep
from Common.my_log import MyLog
from Page_Locators import usedCar_indexPage_locators as idx_loc
from Page_Locators import commenpage_locators as com_loc
from Page_Locators import followClues_page_locators as fol_loc
from Page_Objects import usedCar_index_page

class CommBus(BasePage):
    def switchTo_usedCar(self):
        #等待工作台
        self.wait_ele_visible(com_loc.tab_workSpace)
        #点击工作台
        self.click_element(com_loc.tab_workSpace)
        sleep(2)
    #点击【立新出行】二手车，切换到二手车首页
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
                print("【立新出行】二手车元素不可见，开始滑屏操作")
                size=self.get_size()
                self.swipe_up(size,time=2000)
                print("继续查找【立新出行】二手车")
                sleep(3)
                continue
        sleep(5)
        #点击演示店1
        # self.wait_ele_visible(com_loc.choice_store)
        # self.click_element(com_loc.choice_store)
    #判断是否在二手车首页并切换至二手车首页
    def confirm_and_swichTo_usedCar(self):
        for i in range(3):
			#点击一下屏幕上方，以防有页面弹窗导致无法找到以下元素，点击屏幕上方可以关闭弹窗。
            size=self.get_size()
            x = int(size["width"] * 0.5)
            y = int(size["height"] * 0.1)
            self.driver.tap([(x, y)], 100)
            #1，如果找到元素“提交线索”，说明在二手车页面
            if self.is_ele_visible(idx_loc.link_submit_clues):
                print("当前在二手车首页，无需切换")
                break
            #2，如果未找到元素“提交线索”，找是否有关闭页面的“X”号，关闭页面回到工作台，再切换至二手车首页
            elif self.is_ele_visible(com_loc.close_window):
                self.click_element(com_loc.close_window)
                self.switchTo_usedCar()
                print("当前在页面有“X”号")
                continue
            #3，查找是否有“工作台”元素，有的话可以切换到二手车首页
            elif self.is_ele_visible(com_loc.tab_workSpace):
                self.switchTo_usedCar()
                continue
            #4，以上都没找到
            else:
                MyLog().info("当前页面无法切换至二手车首页！")
                print("当前页面无法切换至工作台")

                break

    #从跟进列表筛选对应状态的线索，选择第一条进入跟进详情
    def follow_clue_fromList(self,cluesStatu):
        #点击评估跟进
        self.wait_ele_visible(idx_loc.link_followUp_clues)
        self.click_element(idx_loc.link_followUp_clues)
        #点击状态下拉框
        self.wait_ele_visible(fol_loc.show_status)
        self.click_element(fol_loc.show_status)
        #点击状态（待评估）
        self.wait_ele_visible(fol_loc.choice_statu_locator(cluesStatu))
        self.click_element(fol_loc.choice_statu_locator(cluesStatu))
        sleep(2)
        #点击列表第一个
        self.wait_ele_visible(fol_loc.fist_of_list)
        self.click_element(fol_loc.fist_of_list)
