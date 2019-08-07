from Common.base_page import BasePage
from time import sleep
from Page_Objects.common_business import CommBus
from Page_Locators import commenpage_locators as com_loc
from Page_Locators import signContract_page_locators as sign_loc
from Common.Datasource import Datasource
class SignContract(BasePage):
    def sign_contract_fromList(self):
        # 调用接口生成一条待签合同数据
        Datasource().gujia(Datasource().pinggu(Datasource().newclue()),100000)
        #在列表选择状态为“待签合同”的线索，点击第一条
        CommBus(self.driver).follow_clue_fromList('待签合同')
        #进入跟进详情点击估价
        self.wait_ele_visible(com_loc.button_goTo_signContract)
        self.click_element(com_loc.button_goTo_signContract)
    def do_signContract(self):
        #选择置换情况
        # self.wait_ele_visible(sign_loc.show_zhiHuanQingKuang)
        # self.click_element(sign_loc.show_zhiHuanQingKuang)
        # self.wait_ele_visible(sign_loc.choice_zhiHuanQingKuang)
        # self.click_element(sign_loc.choice_zhiHuanQingKuang)
        #选择评估师并提交
        self.wait_ele_visible(sign_loc.show_pingGuShi)
        self.click_element(sign_loc.show_pingGuShi)
        self.wait_ele_visible(sign_loc.choice_pingGuShi)
        self.click_element(sign_loc.choice_pingGuShi)
        self.click_element(sign_loc.button_confirm_pingGuShi)
        #输入合同价
        self.wait_ele_visible(sign_loc.input_contract_price)
        self.input_text(sign_loc.input_contract_price,100000)
        #输入收款人姓名
        self.wait_ele_visible(sign_loc.input_people_reciveMoney)
        self.input_text(sign_loc.input_people_reciveMoney,'李教练')
        #上滑屏幕
        size=self.get_size()
        self.swipe_up(size,n=3)
        #--上传图片--
        self.wait_ele_visible(sign_loc.button_open_picture)
        self.click_elements(sign_loc.button_open_picture,3)
        # 打开本地相册选择照片，每次选择7张
        self.wait_ele_visible(sign_loc.choice_picture)
        for j in range(1, 8):
            # 第一个是“拍摄图片”，从第二个开始选
            self.click_elements(sign_loc.choice_picture, j)
        self.wait_ele_visible(sign_loc.confirm_choice_pictures)
        self.click_element(sign_loc.confirm_choice_pictures)
        sleep(20)
        #点击提交
        self.click_element(sign_loc.button_confirm_signContract)
    def assert_signContract_success(self):
        if self.is_ele_visible(com_loc.text_signedContract):
            return True
        else:
            return False