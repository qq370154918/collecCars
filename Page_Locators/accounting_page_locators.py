from appium.webdriver.common.mobileby import MobileBy
'''财务审核页'''
#评估价输入框
input_accounting_remark=(MobileBy.CLASS_NAME,'android.widget.EditText')
#提交按钮
button_confirm_accounting=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("提交")')

