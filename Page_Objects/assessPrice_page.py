from Common.base_page import BasePage
from time import sleep
from Page_Objects.common_business import CommBus
from Page_Locators import commenpage_locators as com_loc
from Page_Locators import assessPrice_page_locators as assPri_loc
from Common.Datasource import Datasource
class AssessPrice(BasePage):
    def assess_price_fromList(self):
        # 调用接口生成一条待估价数据
        Datasource().pinggu(Datasource().newclue())
        #在列表选择状态为“待评估”的线索，点击第一条
        CommBus(self.driver).follow_clue_fromList('待估价')
        #进入跟进详情点击估价
        self.wait_ele_visible(com_loc.button_goTo_assessPrice)
        self.click_element(com_loc.button_goTo_assessPrice)
    def do_assessPrice(self):
        #输入评估价
        self.wait_ele_visible(assPri_loc.input_assessPrice)
        self.input_text(assPri_loc.input_assessPrice,100000)
        #点击提交
        self.wait_ele_visible(assPri_loc.button_confirm_assessPrice)
        self.click_element(assPri_loc.button_confirm_assessPrice)
    def assert_assessProice_success(self):
        if self.is_ele_visible(com_loc.button_goTo_signContract):
            return True
        else:
            return False