from appium.webdriver.common.mobileby import MobileBy
'''签合同页'''
#置换情况
show_zhiHuanQingKuang=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("请选择置换情况")')
#选择依旧换新
choice_zhiHuanQingKuang=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("以旧换新")')
#评估师
show_pingGuShi=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("请选择评估师")')
#选择评估师
choice_pingGuShi=(MobileBy.XPATH,'//android.view.View[contains(@text,"李晓良")]')
#评估师页面提交按钮
button_confirm_pingGuShi=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("提交")')
#合同价输入框
input_contract_price=(MobileBy.XPATH,'//android.view.View[@text="合同价*"]/following-sibling::android.view.View/android.widget.EditText')
#收款人输入框
input_people_reciveMoney=(MobileBy.XPATH,'//android.view.View[@text="收款人*"]/following-sibling::android.view.View/android.widget.EditText')
#加号上传照片
button_open_picture=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("javascript:void(0);")')
#点击选中图片,多个元素，依次点击
# choice_picture=(MobileBy.ID,'com.tencent.wework:id/do5')
# choice_picture=(MobileBy.ID,'com.tencent.wework:id/do6')
choice_picture=(MobileBy.ID,'com.tencent.wework:id/dqm')
#选中图片后点击确定
# confirm_choice_pictures=(MobileBy.ID,'com.tencent.wework:id/ecl')
# confirm_choice_pictures=(MobileBy.ID,'com.tencent.wework:id/ecm')
confirm_choice_pictures=(MobileBy.ID,'com.tencent.wework:id/efk')

#提交按钮
button_confirm_signContract=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("提交")')
#提交后跳转跟进详情页，驳回按钮,存在即可断言签合同成功
button_reject_contract=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("驳回")')
