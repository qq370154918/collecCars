from appium.webdriver.common.mobileby import MobileBy
'''线索跟进页'''

#待评估下拉框
show_status=(MobileBy.XPATH,'//*[@resource-id="app"]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[2]')

#选择状态
def choice_statu_locator(statu):
    #statu=['待评估','待估价','待签合同','待财务审核','待店总审核','待财务放款','已完成','已关闭']
    choice_status=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("{}")'.format(statu))
    return choice_status

#列表第一个
fist_of_list=(MobileBy.XPATH,'//*[@resource-id="app"]/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View[1]/android.view.View[1]')
