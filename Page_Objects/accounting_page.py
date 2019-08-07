from Common.base_page import BasePage
from time import sleep
from Page_Objects.common_business import CommBus
from Page_Locators import accounting_page_locators as acc_loc
from Page_Locators import commenpage_locators as com_loc
from Common.Datasource import Datasource
class Accounting(BasePage):
    '''财务审核'''
    def accounting_pass_fromList(self):
        # 调用接口生成一条待财务审核的数据
        Datasource().qianhetong(Datasource().gujia(Datasource().pinggu(Datasource().newclue()),100000))
        # 在列表选择状态为“待财务审核”的线索，点击第一条
        CommBus(self.driver).follow_clue_fromList('待财务审核')
        # 进入跟进详情点击估价
        self.wait_ele_visible(com_loc.button_accounting_pass)
        self.click_element(com_loc.button_accounting_pass)
    def do_accounting(self):
        #输入备注内容
        self.wait_ele_visible(acc_loc.input_accounting_remark)
        self.input_text(acc_loc.input_accounting_remark,'财务审核通过')
        #点击提交
        self.wait_ele_visible(acc_loc.button_confirm_accounting)
        self.click_element(acc_loc.button_confirm_accounting)
    def assert_accounting_pass_success(self):
        if self.is_ele_visible(com_loc.text_accountingPass):
            return True
        else:
            return False