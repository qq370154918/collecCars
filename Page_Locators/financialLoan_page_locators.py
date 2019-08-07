from appium.webdriver.common.mobileby import MobileBy
#备注输入框
# input_financialLoan_remark=(MobileBy.XPATH,'//android.widget.EditText[@text="请输入备注内容"]')
input_financialLoan_remark=(MobileBy.XPATH,'//android.widget.EditText[@text="备注内容"]')
#加号上传照片(有多个元素，需要取第一个)
button_open_picture=(MobileBy.XPATH,'//android.view.View[@text="javascript:void(0);"]')
#选择照片（有多个元素，可以取第一个）
# choice_picture=(MobileBy.ID,'com.tencent.wework:id/fc')
choice_picture=(MobileBy.ID,'com.tencent.wework:id/fe')
#跳转预览页面后的确定按钮
# confirm_choice_pictures=(MobileBy.ID,'com.tencent.wework:id/ecl')
# confirm_choice_pictures=(MobileBy.ID,'com.tencent.wework:id/ecm')
confirm_choice_pictures=(MobileBy.ID,'com.tencent.wework:id/efk')

#提交按钮
button_confirm_financialLoan=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("提交")')