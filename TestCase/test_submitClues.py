from Page_Objects.submitClues_page import SubmitCluesPage
from Page_Objects.usedCar_index_page import UsedCarIndexPage
from Page_Objects.common_business import CommBus
from Page_Objects.assessClues_page import AssessClues
from Page_Objects.assessPrice_page import AssessPrice
from Page_Objects.signContract_page import SignContract
from Page_Objects.accounting_page import Accounting
from Page_Objects.managerAudit_page import ManagerAudit
from Page_Objects.financialLoan_page import FinancialLoan
from Test_Data.submitClues_page_data import *
from Common.my_log import MyLog
from time import sleep
import pytest

@pytest.mark.usefixture('startApp')
class TestSubmintClues():
    '''新建线索'''
    def test_submintClues_sucess(self,startApp):
        #切换到二手车
        SubmitCluesPage(startApp).submit_clues(vin_number)
        sleep(3)
        try:
            assert SubmitCluesPage(startApp).submitClue_success_isExit()
        except Exception as e:
            MyLog().info(e)
            raise
# class TestAssessClues():
#     '''评估线索'''
#     def test_assessClue_success(self,startApp):
#         #切换到二手车首页
#         CommBus(startApp).confirm_and_swichTo_usedCar()
#         # #评估线索（从提交线索成功页面直接评估）
#         # AssessClues(startApp).assess_clue_fromSubmitSuccess_page()
#         #评估线索（从跟进列表进入）
#         AssessClues(startApp).assess_clue_fromList()
#         sleep(5)
#         #车辆信息编辑--车辆信息
#         AssessClues(startApp).provide_car_info()
#         sleep(3)
#         # 车辆信息编辑--车辆图片
#         AssessClues(startApp).upload_pictures()
#         # 车辆信息编辑--检测信息
#         sleep(5)
#         AssessClues(startApp).provide_test_info()
#         sleep(5)
#         AssessClues(startApp).submit_assess()
#         #断言
#         try:
#              assert AssessClues(startApp).submit_assess_success_isExit()
#         except Exception as e:
#              MyLog().info(e)
#              raise
# class TestAssessPrice():
#     '''估价'''
#     def test_assessPrice_success(self,startApp):
#         # 切换到二手车首页
#         CommBus(startApp).confirm_and_swichTo_usedCar()
#         #由跟进列表选择待估价状态线索
#         AssessPrice(startApp).assess_price_fromList()
#         sleep(3)
#         AssessPrice(startApp).do_assessPrice()
#         try:
#             assert AssessPrice(startApp).assert_assessProice_success()
#         except Exception as e:
#             MyLog().info(e)
#             raise
# class TestSignContract():
#     '''签合同'''
#     def test_singContract_success(self, startApp):
#         # 切换到二手车首页
#         CommBus(startApp).confirm_and_swichTo_usedCar()
#         # 由跟进列表选择待估价状态线索
#         SignContract(startApp).sign_contract_fromList()
#         sleep(3)
#         SignContract(startApp).do_signContract()
#         try:
#             assert SignContract(startApp).assert_signContract_success()
#         except Exception as e:
#             MyLog().info(e)
#             raise
# class TestAccounting():
#     '''财务审核'''
#     def test_accountingPass_success(self, startApp):
#         # 切换到二手车首页
#         CommBus(startApp).confirm_and_swichTo_usedCar()
#         # 由跟进列表选择待财务审核状态线索
#         Accounting(startApp).accounting_pass_fromList()
#         sleep(3)
#         Accounting(startApp).do_accounting()
#         try:
#             assert Accounting(startApp).assert_accounting_pass_success()
#         except Exception as e:
#             MyLog().info(e)
#             raise
# class TestManagerAudit():
#     '''店总审核'''
#     def test_managerAuditPass_success(self, startApp):
#         # 切换到二手车首页
#         CommBus(startApp).confirm_and_swichTo_usedCar()
#         # 由跟进列表选择待财务审核状态线索
#         ManagerAudit(startApp).managerAudit_pass_fromList()
#         sleep(3)
#         ManagerAudit(startApp).do_audit()
#         try:
#             assert ManagerAudit(startApp).assert_managerAudit_pass_success()
#         except Exception as e:
#             MyLog().info(e)
#             raise
# class TestFinancialLoan():
#     '''财务放款'''
#     def test_financialLoan_success(self, startApp):
#         # 切换到二手车首页
#         CommBus(startApp).confirm_and_swichTo_usedCar()
#         # 由跟进列表选择待财务审核状态线索
#         FinancialLoan(startApp).financialLoan_fromList()
#         sleep(3)
#         FinancialLoan(startApp).do_financialLoan()
#         try:
#             assert FinancialLoan(startApp).assert_financialLoan_success()
#         except Exception as e:
#             MyLog().info(e)
#             raise

