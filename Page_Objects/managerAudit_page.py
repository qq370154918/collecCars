from Common.base_page import BasePage
from time import sleep
from Page_Objects.common_business import CommBus
from Page_Locators import managerAudit_page_locators as man_loc
from Page_Locators import commenpage_locators as com_loc
from Common.Datasource import Datasource
class ManagerAudit(BasePage):
    '''店总审核审核'''
    def managerAudit_pass_fromList(self):
        # 调用接口生成一条待店总审核的数据
        Datasource().caiwushenhe(Datasource().qianhetong(Datasource().gujia(Datasource().pinggu(Datasource().newclue()),100000)),"approve")
        # 在列表选择状态为“待店总审核”的线索，点击第一条
        CommBus(self.driver).follow_clue_fromList('待店总审核')
        # 进入跟进详情点击估价
        self.wait_ele_visible(com_loc.button_accounting_pass)
        self.click_element(com_loc.button_accounting_pass)
    def do_audit(self):
        #输入备注内容
        self.wait_ele_visible(man_loc.input_audit_remark)
        self.input_text(man_loc.input_audit_remark,'店总审核通过')
        #点击提交
        self.wait_ele_visible(man_loc.button_confirm_audit)
        self.click_element(man_loc.button_confirm_audit)
    def assert_managerAudit_pass_success(self):
        if self.is_ele_visible(com_loc.text_managerPass):
            return True
        else:
            return False