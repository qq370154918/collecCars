from appium.webdriver.common.mobileby import MobileBy
'''评估页'''
#评估车辆-车辆信息编辑

#@@@@@------------车辆照片
#车辆照片按钮
link_upload_picture=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("车辆照片")')
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
#上传图片完成后点击保存
button_save_pictures=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("保存")')

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#@@@@@@@@@@@@------车辆信息
#车辆信息按钮
# link_car_info=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("车辆信息")')
link_car_info=(MobileBy.XPATH,'//*[@resource-id="app"]/android.view.View[1] /android.view.View[2]')
#排放标准--点击弹出排放标准选择
paiFangBiaoZhun=(MobileBy.XPATH,'//android.view.View[@text="排放标准"]/parent::android.view.View/parent::android.view.View/android.view.View[3]')
#选择排放标准
choice_paiFangBiaoZhun=(MobileBy.XPATH,'//android.widget.TextView[@text="国三"]')
#出厂日期-点击弹出时间选择
leave_factory_time=(MobileBy.XPATH,'//android.view.View[contains(@text,"出厂日期")]')
#选择出厂日期确定--“完成”用坐标点
#分辨率 1080*1812   坐标点900,1000 比例分别是0.833，0.552
confirm_leaveFactoryTime=()

#点击弹出车辆性质
cheLiangXingZhi=(MobileBy.XPATH,'//android.view.View[@text="车辆性质"]/parent::android.view.View/parent::android.view.View/android.view.View[3]')
#选择车辆性质
choice_cheLiangXingZhi=(MobileBy.XPATH,'//android.widget.TextView[@text="私户"]')

#点击弹出使用性质
shiYongXingZhi=(MobileBy.XPATH,'//android.view.View[@text="使用性质"]/parent::android.view.View/parent::android.view.View/android.view.View[3]')
#选择使用性质
choice_shiYongXingZhi=(MobileBy.XPATH,'//android.widget.TextView[@text="非营运"]')

#点击保存基本信息
button_save_carInfo=(MobileBy.XPATH,'//*[@resource-id="app"]/android.view.View/android.view.View/android.view.View[2]')

#点击保存配置信息
button_save_peiZhi=(MobileBy.XPATH,'//android.widget.TextView[@text="保存配置信息"]')


#手续信息-----------------页面
#过户要求输入框
input_guoHuTime=(MobileBy.XPATH,'//android.widget.EditText[@text="请输入"]')
#年检到期日-点击弹出时间选择框
nianJianDaoQi=(MobileBy.XPATH,'//android.view.View[contains(@text,"年检到期日")]')
#强险到期日-点击弹出时间选择框
qiangXianDaoQi=(MobileBy.XPATH,'//android.view.View[contains(@text,"强险到期日")]')
#商险到期日-点击弹出时间选择
shangXianDaoQi=(MobileBy.XPATH,'//android.view.View[contains(@text,"商险到期日")]')
#保存手续信息按钮
# button_save_shouXu=(MobileBy.XPATH,'//*[@resource-id="app"]/android.view.View/android.view.View[2]/android.view.View[2]')
button_save_shouXu=(MobileBy.XPATH,'//android.view.View[@text="保存手续信息"]')

#保存备注信息按钮
button_save_remark=(MobileBy.XPATH,'//android.view.View[@text="保存备注信息"]')





#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#@@@@@@@@@@@@------检测信息
#检测信息按钮
link_test_info=(MobileBy.XPATH,'//*[@resource-id="app"]/android.view.View[1]/android.view.View[3]')
# link_test_info=(MobileBy.XPATH,'//android.view.View[@text="检测信息"]')
#保存车头检测
button_save_cheTou=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("保存车头检测")')
#保存左侧检测
button_save_zuoCe=(MobileBy.XPATH,'//android.view.View[contains(@text,"保存")]')
#保存车尾检测
button_save_cheWei=(MobileBy.XPATH,'//android.view.View[contains(@text,"保存")]')
#保存右侧检测
button_save_youCe=(MobileBy.XPATH,'//android.view.View[contains(@text,"保存")]')
#保存机械内饰检测
button_save_jiXieNeiShi=(MobileBy.XPATH,'//android.view.View[contains(@text,"保存")]')
#保存电器检测
button_save_dianQi=(MobileBy.XPATH,'//android.view.View[contains(@text,"保存")]')

#提交评估按钮
button_submit_assess=(MobileBy.XPATH,'//android.view.View[contains(@text,"提交")]')

#提交成功页面--跟进线索
button_follow_clue=(MobileBy.XPATH,'//android.view.View[@text="已保存"]')