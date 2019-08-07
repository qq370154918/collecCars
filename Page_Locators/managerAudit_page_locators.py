from appium.webdriver.common.mobileby import MobileBy
'''店总审核页'''
#备注输入框
input_audit_remark=(MobileBy.CLASS_NAME,'android.widget.EditText')
#提交按钮
button_confirm_audit=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("提交")')

