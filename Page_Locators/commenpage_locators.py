from appium.webdriver.common.mobileby import MobileBy
#企业微信首页的tab切换
#我的
tab_myselef=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("我")')
#工作台
tab_workSpace=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("工作台")')
# tab_workSpace=(MobileBy.XPATH,'//com.tencent.wework:id/kz[@text="工作台"]')
# '//android.widget.ListView[1]/android.view.View[{}]'
#工作台-二手车（服务商）
link_used_car=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("【立新出行】二手车")')

#选择门店-演示店1
choice_store=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("演示店1")')
#页面关闭按钮（‘X’）
# close_window=(MobileBy.ID,'com.tencent.wework:id/ec7')
# close_window=(MobileBy.ID,'com.tencent.wework:id/ec8')
close_window=(MobileBy.ID,'com.tencent.wework:id/ef6')


'''二手车跟进详情页'''
#文本"已签合同"
text_signedContract=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("已签合同")')
#文本"财务审核通过"
text_accountingPass=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("财务审核通过")')
#文本"店总审核通过"
text_managerPass=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("店总审核通过")')
#文本“已完成”
text_completed=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("已完成")')

#评估按钮
button_goTo_assess=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("评估")')
#估价按钮
button_goTo_assessPrice=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("估价")')
#签合同按钮
button_goTo_signContract=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("签合同")')
#财务审核通过按钮
button_accounting_pass=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("通过")')
#店总审核通过按钮
button_managerAudit_pass=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("通过")')
#财务“放款”按钮
button_financialLoan=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("放款")')

