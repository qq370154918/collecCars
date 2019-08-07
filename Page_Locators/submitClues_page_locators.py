from appium.webdriver.common.mobileby import MobileBy
from random import randint
'''提交线索页'''
#首页“提交线索”
link_submit_clues=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("提交线索")')
#车架号输入框
input_frame_number=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("输入17位车架号，识别车型")')

#车型（点击进入车型选择）
link_choice_carModel=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("车型")')
#hot
button_choice_hotModel=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("HOT")')
#型号
list=["奔驰","宝马","标致","雪铁龙","丰田","大众","奥迪","现代","比亚迪","福特","马自达","本田","日产","别克","雪佛兰"]

choice_model_random=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("{}")'.format(list[randint(0,len(list)-1)]))
#车型
choice_model_fist=(MobileBy.XPATH,'//*[@resource-id="app"]/android.view.View/android.widget.ListView/android.view.View[1]/android.view.View')
#排量及年款
choice_model_year=(MobileBy.XPATH,'//*[@resource-id="app"]/android.view.View/android.widget.ListView/android.view.View[1]')
#车牌号输入框
input_car_number=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("请输入车牌号")')
#键盘已弹出
keyboard_exist=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("B")')

def input_num(num):
    input_numuber = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")'.format(num))
    return input_numuber
#首次上牌日期选择
choice_fist_registeTime=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text(" 首次上牌 请选择首次上牌日期 ")')
#选择上牌日期后完成
complete_choice=(MobileBy.XPATH,'//com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View[2]')
#complete_choice=(MobileBy.XPATH,'//*[@resource-id="app"]/following-sibling::android.view.View[2]/android.view.View[text()="完成"]')
# complete_choice=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("完成")')
#行驶里程输入框
input_vehicle_mileage=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("请输入公里数")')
#车主姓名输入框
input_owner_name=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("注意，需要填写车主的姓名")')
#车主电话输入框
input_owner_mobile=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("车主手机号码")')
#提交
#button_submit=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("提交")')
button_submit=(MobileBy.XPATH,'//*[@resource-id="app"]/android.view.View/android.view.View/android.view.View[7]/android.view.View')
#跳转已提交页面（已提交）
submitClue_success=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("已提交")')

#跟进线索
link_goTo_assessCar=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("去评估")')