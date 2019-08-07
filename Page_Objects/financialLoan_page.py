from Common.base_page import BasePage
from time import sleep
from Page_Objects.common_business import CommBus
from Page_Locators import financialLoan_page_locators as fin_loc
from Page_Locators import commenpage_locators as com_loc
from Common.Datasource import Datasource
class FinancialLoan(BasePage):
    '''财务放款'''
    def financialLoan_fromList(self):
        # 调用接口生成一条待财务放款的数据
        Datasource().dianzongshenhe(Datasource().caiwushenhe(Datasource().qianhetong(Datasource().gujia(Datasource().pinggu(Datasource().newclue()),100000)),"approve"),"approve")
        # 在列表选择状态为“待财务放款”的线索，点击第一条
        CommBus(self.driver).follow_clue_fromList('待财务放款')
        # 进入跟进详情点击放款
        self.wait_ele_visible(com_loc.button_financialLoan)
        self.click_element(com_loc.button_financialLoan)
    def do_financialLoan(self):
        sleep(2)
        #向上滑屏
        size=self.get_size()
        self.swipe_up(size)
        sleep(2)
        #输入备注
        self.wait_ele_visible(fin_loc.input_financialLoan_remark)
        self.input_text(fin_loc.input_financialLoan_remark,'财务放款通过')
        #点击加号上传图片
        self.wait_ele_visible(fin_loc.button_open_picture)
        self.click_elements(fin_loc.button_open_picture,0)
        #选择图片
        self.wait_ele_visible(fin_loc.choice_picture)
        self.click_elements(fin_loc.choice_picture,0)
        #点击确定
        self.wait_ele_visible(fin_loc.confirm_choice_pictures)
        self.click_element(fin_loc.confirm_choice_pictures)
        sleep(5)
        #点击提交
        self.wait_ele_visible(fin_loc.button_confirm_financialLoan)
        self.click_element(fin_loc.button_confirm_financialLoan)
    def assert_financialLoan_success(self):
        if self.is_ele_visible(com_loc.text_completed):
            return True
        else:
            return False