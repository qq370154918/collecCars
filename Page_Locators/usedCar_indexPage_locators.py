from appium.webdriver.common.mobileby import MobileBy
'''二手车首页'''
#提交线索
link_submit_clues=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("提交线索")')
#评估跟进
link_followUp_clues=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("评估跟进")')