from Common.base_page import BasePage
from time import sleep
from Page_Objects.common_business import CommBus
from Page_Locators import followClues_page_locators as fol_loc
from Page_Locators import usedCar_indexPage_locators as idx_loc
from Page_Locators import submitClues_page_locators as sub_loc
from Page_Locators import commenpage_locators as com_loc
from Page_Locators import assessClues_page_locators as ass_loc
from Common.Datasource import Datasource
class AssessClues(BasePage):
    #从提交线索成功页面点击去评估
    def assess_clue_fromSubmitSuccess_page(self):
        #点击跟进线索
        self.wait_ele_visible(sub_loc.link_goTo_assessCar)
        self.click_element(sub_loc.link_goTo_assessCar)
    def assess_clue_fromList(self):
        #调用接口生成一条待评估数据
        Datasource().newclue()
        #在列表选择状态为“待评估”的线索，点击第一条
        CommBus(self.driver).follow_clue_fromList('待评估')
        self.wait_ele_visible(com_loc.button_goTo_assess)
        self.click_element(com_loc.button_goTo_assess)
    def upload_pictures(self):
        '''车辆照片'''
        #点击车辆照片
        self.wait_ele_visible(ass_loc.link_upload_picture)
        self.click_element(ass_loc.link_upload_picture)
        for i in range(2):
            #点击加号上传照片
            # eles=ass_loc.button_open_picture
            self.wait_ele_visible(ass_loc.button_open_picture)
            self.click_elements(ass_loc.button_open_picture,12)
            #打开本地相册选择照片，每次选择8张,要选两次
            # eles1=ass_loc.choice_picture
            self.wait_ele_visible(ass_loc.choice_picture)
            for j in range(1,9):
                #第一个是“拍摄图片”，从第二个开始选
                self.click_elements(ass_loc.choice_picture,j)
            self.wait_ele_visible(ass_loc.confirm_choice_pictures)
            self.click_element(ass_loc.confirm_choice_pictures)
            sleep(23)
        #上传完成后点击保存
        self.wait_ele_visible(ass_loc.button_save_pictures)
        self.click_element(ass_loc.button_save_pictures)
    def provide_car_info(self):
        '''车辆信息'''
        #点击车辆信息
        self.wait_ele_visible(ass_loc.link_car_info)
        self.click_element(ass_loc.link_car_info)
        sleep(5)
        #点击排放标准
        self.wait_ele_visible(ass_loc.paiFangBiaoZhun)
        self.click_element(ass_loc.paiFangBiaoZhun)
        for i in range(2):
            if self.is_ele_visible(ass_loc.choice_paiFangBiaoZhun):
                #选择排放标注
                self.click_element(ass_loc.choice_paiFangBiaoZhun)
                break
            else:
                self.click_element(ass_loc.paiFangBiaoZhun)
                continue
        #点击出厂日期
        self.wait_ele_visible(ass_loc.leave_factory_time)
        self.click_element(ass_loc.leave_factory_time)
        sleep(3)
        #确定出厂日期(坐标点击“完成”)
        size = self.get_size()
        x = int(size["width"] * 0.833)
        y = int(size["height"] * 0.552)
        self.driver.tap([(x, y)], 100)
        #向上滑屏
        sleep(1)
        self.swipe_up(size,n=2)
        #选择车辆性质
        self.wait_ele_visible(ass_loc.cheLiangXingZhi)
        self.click_element(ass_loc.cheLiangXingZhi)
        sleep(2)
        self.wait_ele_visible(ass_loc.choice_cheLiangXingZhi)
        self.click_element(ass_loc.choice_cheLiangXingZhi)
        #选择使用性质
        self.wait_ele_visible(ass_loc.shiYongXingZhi)
        self.click_element(ass_loc.shiYongXingZhi)
        sleep(2)
        self.wait_ele_visible(ass_loc.choice_shiYongXingZhi)
        self.click_element(ass_loc.choice_shiYongXingZhi)
        #点击保存基本信息
        self.wait_ele_visible(ass_loc.button_save_carInfo)
        self.click_element(ass_loc.button_save_carInfo)
        sleep(2)
        #点击保存配置信息
        print('开始滑屏')
        self.swipe_up(size,time=100)
        sleep(2)
        print('滑屏结束')
        x = int(size["width"] * 0.5)
        y = int(size["height"] * 0.95)
        self.driver.tap([(x, y)], 100)
        print("已点击“保存配置信息”")
        sleep(5)
        self.swipe_down(size,time=200,n=3)
        self.wait_ele_visible(ass_loc.input_guoHuTime)
        self.input_text(ass_loc.input_guoHuTime, 10)
        sleep(2)
        #选择年检到期日,坐标点击完成
        self.wait_ele_visible(ass_loc.nianJianDaoQi)
        self.click_element(ass_loc.nianJianDaoQi)
        sleep(2)
        size = self.get_size()
        x = int(size["width"] * 0.833)
        y = int(size["height"] * 0.552)
        self.driver.tap([(x, y)], 100)
        sleep(2)
        #选择强险到期日
        self.wait_ele_visible(ass_loc.qiangXianDaoQi)

        self.click_element(ass_loc.qiangXianDaoQi)
        sleep(2)
        x = int(size["width"] * 0.833)
        y = int(size["height"] * 0.552)
        self.driver.tap([(x, y)], 100)
        sleep(2)
        #选择商险到期日
        self.wait_ele_visible(ass_loc.shangXianDaoQi)
        self.click_element(ass_loc.shangXianDaoQi)
        sleep(2)
        x = int(size["width"] * 0.833)
        y = int(size["height"] * 0.552)
        self.driver.tap([(x, y)], 100)
        # #向上滑屏
        # self.swipe_up(size, time=100)
        sleep(2)
        # 点击保存手续信息
        self.wait_ele_visible(ass_loc.button_save_shouXu)
        self.click_element(ass_loc.button_save_shouXu)
        sleep(4)
        for i in range(3):
            if self.is_ele_visible(ass_loc.button_save_remark):
                #点击保存备注信息
                self.wait_ele_visible(ass_loc.button_save_remark)
                self.click_element(ass_loc.button_save_remark)
                break
            else:
                self.click_element(ass_loc.button_save_shouXu)
                continue
    def provide_test_info(self):
        '''检测信息'''
        #点击检测信息
        for i in range(3):
            sleep(5)
            if self.is_ele_visible(ass_loc.link_test_info):
                '''有时候点击了但是页面未跳转，做处理'''
                print('进入“if self.is_ele_visible(ass_loc.link_test_info)')
                # 如果元素“检测信息存在”，点击，继续循环
                self.wait_ele_visible(ass_loc.link_test_info)
                self.click_element(ass_loc.link_test_info)
                print('元素“检测信息”存在，已点击')
                continue
            elif self.is_ele_visible(ass_loc.button_save_cheTou):
                print('进入“elif self.is_ele_visible(ass_loc.button_save_cheTou)”')
                #如果已经进入下个页面，跳出循环
                break
            else:
                print('当前页面错误')
        sleep(2)
        #点击保存车头检测
        self.wait_ele_visible(ass_loc.button_save_cheTou)
        self.click_element(ass_loc.button_save_cheTou)
        sleep(2)
        #点击保存左侧检测
        self.wait_ele_visible(ass_loc.button_save_zuoCe)
        self.click_element(ass_loc.button_save_zuoCe)
        sleep(2)
        # 点击保存车尾检测
        self.wait_ele_visible(ass_loc.button_save_cheWei)
        self.click_element(ass_loc.button_save_cheWei)
        sleep(2)
        # 点击保存右侧检测
        self.wait_ele_visible(ass_loc.button_save_youCe)
        self.click_element(ass_loc.button_save_youCe)
        sleep(2)
        # 点击保存机械内饰检测
        self.wait_ele_visible(ass_loc.button_save_jiXieNeiShi)
        self.click_element(ass_loc.button_save_jiXieNeiShi)
        sleep(2)
        # 点击保存电器检测
        self.wait_ele_visible(ass_loc.button_save_dianQi)
        self.click_element(ass_loc.button_save_dianQi)
    def submit_assess(self):
        '''提交评估'''
        self.wait_ele_visible(ass_loc.button_submit_assess)
        self.click_element(ass_loc.button_submit_assess)
    def submit_assess_success_isExit(self):
        if self.is_ele_visible(ass_loc.button_follow_clue):
            return True
        else:
            return False

