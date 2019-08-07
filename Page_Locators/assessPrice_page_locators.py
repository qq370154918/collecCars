from appium.webdriver.common.mobileby import MobileBy
'''估价页'''
#评估价输入框
input_assessPrice=(MobileBy.XPATH,'//android.view.View[@text="评估价"]/following-sibling::android.view.View/android.widget.EditText')
#提交按钮
button_confirm_assessPrice=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("提交")')

