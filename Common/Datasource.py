# coding=utf-8
import requests
import random
import json
from Common.random_str import *
vin_num=random_vin()
class Datasource():
    #这个session是我自己手机立新立新服务商liang门店4环境的，其他账号的可以抓取
    session='16eea6c0-04a7-4575-a862-fc9dcfe4d058'
    # 定义一个函数，获取登录后的token
    def get_login_token(self):
        requests.packages.urllib3.disable_warnings()
        url = 'https://q.test.dos.cheanjia.net/auth/is_qymplogin'
        cookies = {
            "session": self.session
        }
        # headlers = {"session": self.session,
        #             "Content-Type": "application/json"
        #             }
        response = requests.get(url,cookies=cookies, verify=False)
        login_token = response.cookies["csrf-token"]
        # print(response.text)
        # print(response.cookies["csrf-token"])
        return login_token

    #定义一个函数，新建线索
    def newclue(self):
        token=Datasource.get_login_token(self)
        url = 'https://q.test.dos.cheanjia.net/api/v1/used_car/tickets'
        car_no=str(random.randint(10000,99999))
        data = {"plate_number": "粤A"+car_no,"vin": vin_num,"jzg_car_model_id": "4521","jzg_car_model_name": "奔驰 R级 2007款 5.5L 自动 R500L 4MATIC","license_issued_on": "2018-05-16","owner_name": "接口生成数据","owner_mobile":"13163750276","mileage": "111111","jzg_color_id": "1","transfer_count": "0", "province_code": "440000","province": "广东省","city_code": "440300","city": "深圳市","channel": "1","replace_detail": "1","from_employee_name": "李晓良","from_employee_id": "","note": "备注内容","district": "南山区","district_code": "440305" }
        cookies = {
            "csrf-token": token,
            "session": self.session
        }
        headlers = {"X-CSRF-Token": token,
                    "Content-Type": "application/x-www-form-urlencoded"}
        response = requests.put(url, headers=headlers, data=data, cookies=cookies, verify=False)
        #print(response.text)
        return ("粤A"+car_no)

    #定义一个函数，根据车牌号，获取车辆的id
    def get_car_id(self,car_no):
        token = Datasource.get_login_token(self)
        url = 'https://q.test.dos.cheanjia.net/api/v1/used_car/tickets/search'
        cookies = {
            "csrf-token": token,
            "session": self.session
        }
        headlers = {"session": self.session,
                    "Content-Type": "application/json"
                    }
        data = {
            "plate_number": car_no
        }
        response = requests.get(url, headers=headlers, params=data, cookies=cookies, verify=False)
        # print(response.text)
        response=json.loads(response.text)
        return response["data"]["tickets"][0]["id"]

    #定义一个函数，评估的时候用，获取车辆的info_id
    def get_info_id(self,car_no):
        token = Datasource.get_login_token(self)
        id = str(Datasource.get_car_id(self,car_no))
        url = 'https://q.test.dos.cheanjia.net/api/v1/used_car/ticket/%s/evaluation/car_info' % id
        cookies = {
            "csrf-token": token,
            "session": self.session
        }
        headers = {"X-CSRF-Token": token,
                   "Content-Type": "application/x-www-form-urlencoded"}
        response = requests.put(url, headers=headers, cookies=cookies, verify=False)
        response = json.loads(response.text)
        info_id = response["data"]["car_info_id"]
        return info_id

    #定义一个函数，上传图片的时候用，传递一个图片的本地路径，先把本地图片上传到后台，返回图片在后台的地址
    def upload_img(self,path):
        token=Datasource.get_login_token(self)
        url = 'https://q.test.dos.cheanjia.net/api/v1/upload_image'
        file = {'img': ('timg.jpg', open(path, 'rb'))}
        cookies = {
            "csrf-token": token,
            "session": self.session
        }
        headers = {"X-CSRF-Token": token,
                   # "Content-Type": "application/x-www-form-urlencoded"
                   }
        response = requests.post(url, headers=headers, cookies=cookies, files=file, verify=False)
        # print(eval(response.text)["data"])
        return (eval(response.text)["data"])


    #定义一个函数，根据车牌号，评估线索,评估的时候url带的是info_id不是car_id
    def pinggu(self,car_no):
        token = Datasource.get_login_token(self)
        info_id=Datasource.get_info_id(self,car_no)
        #第一步,评估车辆信息_基本信息
        url='https://q.test.dos.cheanjia.net/api/v1/used_car/ticket/car_info/%s'%info_id
        data={"vin":vin_num,"car_model_id":"4521","car_model_name":"奔驰 R级 2007款 5.5L 自动 R500L 4MATIC","mileage":"60000","color_id":"1","is_color_changed":"0","production_date":"2015-05-16","license_issued_on":"2019-05-16","transfer_count":"0","last_transfer_date":"","belonged_province":"广东省","belonged_province_code":"440000","belonged_city":"深圳市","belonged_city_code":"440300","located_province":"广东省","located_province_code":"440000","located_city":"深圳市","located_city_code":"440300","plate_number":car_no,"is_refitted":"false","car_character":"1", "car_character_name":"私户","usage_character":"2","usage_character_name":"非营运","emission_standard":"100","emission_standard_name":"国一", "channel":"1","channel_name":"销售端潜客","color_name":"黑","info_has_changes":"true"}
        cookies = {
            "csrf-token": token,
            "session": self.session
        }
        headers = {"X-CSRF-Token": token,
                    "Content-Type": "application/x-www-form-urlencoded"}
        response=requests.post(url,headers=headers, data=data, cookies=cookies, verify=False)
        #print(response.text)
        # 第二步,评估车辆信息_配置信息  第三步,评估车辆信息_手续信息 一个后台接口，一起发送
        url = 'https://q.test.dos.cheanjia.net/api/v1/used_car/ticket/car_info/%s/info' % info_id
        #data_info={"config": [{"group_name": "basic", "name": "\u57fa\u672c\u53c2\u6570", "params": [{"name": "\u8f66\u95e8\u6570(\u4e2a)", "external_name": "Body_Doors", "value": ""}, {"name": "\u5ea7\u4f4d\u6570(\u4e2a)", "external_name": "Perf_SeatNum", "value": ""}, {"name": "\u6392\u91cf(L)", "external_name": "Engine_ExhaustForFloat", "value": ""}, {"name": "\u71c3\u6599\u7c7b\u578b", "external_name": "Oil_FuelType", "value": ""}, {"name": "\u6321\u4f4d\u4e2a\u6570(\u4e2a)", "external_name": "UnderPan_ForwardGearNum", "value": ""}, {"name": "\u53d8\u901f\u7bb1\u7c7b\u578b", "external_name": "UnderPan_TransmissionType", "value": ""}, {"name": "\u9a71\u52a8\u65b9\u5f0f", "external_name": "Perf_DriveType", "value": ""}]}, {"group_name": "security", "name": "\u4e3b/\u88ab\u52a8\u5b89\u5168\u8bbe\u5907", "params": [{"name": "\u9a7e\u9a76\u4f4d\u5b89\u5168\u6c14\u56ca", "external_name": "Safe_DriverGasBag", "value": ""}, {"name": "\u526f\u9a7e\u9a76\u4f4d\u5b89\u5168\u6c14\u56ca", "external_name": "Safe_SubDriverGasBag", "value": ""}, {"name": "\u524d\u6392\u4fa7\u5b89\u5168\u6c14\u56ca", "external_name": "Safe_FsadGasbag", "value": ""}, {"name": "\u540e\u6392\u4fa7\u5b89\u5168\u6c14\u56ca", "external_name": "Safe_BsadGasbag", "value": ""}, {"name": "\u524d\u6392\u5934\u90e8\u6c14\u56ca(\u6c14\u5e18)", "external_name": "Safe_FheadGasbag", "value": ""}, {"name": "\u819d\u90e8\u6c14\u56ca", "external_name": "Safe_KneeGasBag", "value": ""}, {"name": "\u5b89\u5168\u5e26\u6c14\u56ca", "external_name": "InStat_BeltBag", "value": ""}, {"name": "\u80ce\u538b\u76d1\u6d4b\u88c5\u7f6e", "external_name": "UnderPan_TyrePressureWatcher", "value": ""}, {"name": "\u5239\u8f66\u9632\u62b1\u6b7b(ABS)", "external_name": "Safe_ABS", "value": ""}, {"name": "\u76f2\u70b9\u68c0\u6d4b/\u5e76\u7ebf\u8f85\u52a9", "external_name": "InStat_blindspotdetection", "value": ""}, {"name": "\u591c\u89c6\u7cfb\u7edf", "external_name": "InStat_NightVisionSystem", "value": ""}]}, {"group_name": "accessory", "name": "\u8f85\u52a9/\u64cd\u63a7\u914d\u7f6e", "params": [{"name": "\u6cca\u8f66\u96f7\u8fbe(\u8f66\u524d)", "external_name": "UnderPan_PRadar", "value": ""}, {"name": "\u5012\u8f66\u96f7\u8fbe(\u8f66\u540e)", "external_name": "UnderPan_RRadar", "value": ""}, {"name": "\u5012\u8f66\u5f71\u50cf", "external_name": "UnderPan_RImage", "value": ""}, {"name": "\u5168\u666f\u6444\u50cf\u5934", "external_name": "InStat_PanoramicCamera", "value": ""}, {"name": "\u5b9a\u901f\u5de1\u822a", "external_name": "InStat_SpeedCruise", "value": ""}, {"name": "\u81ea\u9002\u5e94\u5de1\u822a", "external_name": "InStat_Automaticcruise", "value": ""}, {"name": "\u81ea\u52a8\u6cca\u8f66\u5165\u4f4d", "external_name": "InStat_AutoParking", "value": ""}, {"name": "\u4e0a\u5761\u8f85\u52a9", "external_name": "InStat_UphillAuxiliary", "value": ""}, {"name": "\u81ea\u52a8\u9a7b\u8f66", "external_name": "InStat_AutoPark", "value": ""}, {"name": "\u9661\u5761\u7f13\u964d", "external_name": "InStat_HDC", "value": ""}, {"name": "\u9065\u63a7\u9a7e\u9a76", "external_name": "Safe_Remotedriving", "value": ""}]}, {"group_name": "external", "name": "\u5916\u90e8/\u9632\u76d7\u914d\u7f6e", "params": [{"name": "\u5929\u7a97\u578b\u5f0f", "external_name": "Body_Louver", "value": ""}, {"name": "\u8fd0\u52a8\u5916\u89c2\u5957\u4ef6", "external_name": "OutStat_SportsAppearanceKit", "value": ""}, {"name": "\u94dd\u5408\u91d1\u8f6e\u5708", "external_name": "Aluminum_alloy_wheels # \u6ca1\u6709\u6807\u660e", "value": ""}, {"name": "\u611f\u5e94\u884c\u674e\u53a2", "external_name": "Induction_trunk", "value": ""}, {"name": "\u8f66\u9876\u884c\u674e\u7bb1\u67b6", "external_name": "OutStat_TopSnelf", "value": ""}, {"name": "\u65e0\u94a5\u5319\u542f\u52a8\u7cfb\u7edf", "external_name": "InStat_AIgnitionSys", "value": ""}, {"name": "\u65e0\u94a5\u5319\u8fdb\u5165\u7cfb\u7edf", "external_name": "nokey_into", "value": ""}, {"name": "\u9065\u63a7\u542f\u52a8", "external_name": "InStat_RemoteStart", "value": ""}, {"name": "\u540e\u5bfc\u6d41\u5c3e\u7ffc", "external_name": "OutStat_InductEmpennage", "value": ""}]}, {"group_name": "internal", "name": "\u5185\u90e8\u914d\u7f6e", "params": [{"name": "\u591a\u529f\u80fd\u65b9\u5411\u76d8", "external_name": "InStat_MultiFuncSteer", "value": ""}, {"name": "\u6362\u6321\u62e8\u7247", "external_name": "InStat_SteerEtc", "value": ""}, {"name": "\u65b9\u5411\u76d8\u52a0\u70ed", "external_name": "Steering_Wheel_hot", "value": ""}, {"name": "\u65b9\u5411\u76d8\u8bb0\u5fc6\u8bbe\u7f6e", "external_name": "InStat_SteerMomery", "value": ""}, {"name": "\u65b9\u5411\u76d8\u8868\u9762\u6750\u6599", "external_name": "InStat_SteerMaterial", "value": ""}, {"name": "HUD\u62ac\u5934\u6570\u5b57\u663e\u793a", "external_name": "InStat_Hud", "value": ""}]}, {"group_name": "seat", "name": "\u5ea7\u6905\u914d\u7f6e", "params": [{"name": "\u5ea7\u6905\u6750\u6599", "external_name": "InStat_SeatMaterial", "value": ""}, {"name": "\u8fd0\u52a8\u5ea7\u6905", "external_name": "InStat_SportSeat", "value": ""}, {"name": "\u9a7e\u9a76\u5ea7\u8170\u90e8\u652f\u6491\u8c03\u8282", "external_name": "InStat_DSeatProp", "value": ""}, {"name": "\u9a7e\u9a76\u5ea7\u80a9\u90e8\u652f\u6491\u8c03\u8282", "external_name": "InStat_AdjustableShoulderSupport", "value": ""}, {"name": "\u9a7e\u9a76\u5ea7\u5ea7\u6905\u8c03\u8282\u65b9\u5f0f", "external_name": "InStat_DSeatTuneType", "value": ""}, {"name": "\u526f\u9a7e\u9a76\u5ea7\u6905\u8c03\u8282\u65b9\u5f0f", "external_name": "InStat_DASeatTuneType", "value": ""}, {"name": "\u7535\u52a8\u5ea7\u6905\u8bb0\u5fc6", "external_name": "InStat_ElectricSeatMemory", "value": ""}, {"name": "\u524d\u6392\u5ea7\u6905\u52a0\u70ed", "external_name": "Heated_front_seats", "value": ""}, {"name": "\u540e\u6392\u5ea7\u6905\u52a0\u70ed", "external_name": "Heated_rear_seats", "value": ""}, {"name": "\u524d\u6392\u5ea7\u6905\u901a\u98ce", "external_name": "The_front_seat_ventilation", "value": ""}, {"name": "\u540e\u6392\u5ea7\u6905\u901a\u98ce", "external_name": "Rear_seat_ventilation", "value": ""}, {"name": "\u5ea7\u6905\u6309\u6469\u529f\u80fd", "external_name": "InStat_SeatKnead", "value": ""}, {"name": "\u7b2c\u4e09\u6392\u5ea7\u6905", "external_name": "InStat_3rdRowSeats", "value": ""}]}, {"group_name": "multimedia", "name": "\u591a\u5a92\u4f53\u914d\u7f6e", "params": [{"name": "GPS\u5bfc\u822a\u7cfb\u7edf", "external_name": "InStat_GPS", "value": ""}, {"name": "\u4e2d\u63a7\u53f0\u6db2\u6676\u5c4f", "external_name": "InStat_CCEscreen", "value": ""}, {"name": "\u540e\u6392\u6db2\u6676\u5c4f", "external_name": "InStat_BEscreen", "value": ""}, {"name": "\u84dd\u7259\u7cfb\u7edf", "external_name": "InStat_Bluetooth", "value": ""}, {"name": "\u65e0\u7ebf\u4e0a\u7f51\u529f\u80fd", "external_name": "InStat_WireLink", "value": ""}, {"name": "\u8f66\u8f7d\u7535\u89c6", "external_name": "InStat_Video", "value": ""}, {"name": "CD", "external_name": "InStat_CDPlayer", "value": ""}, {"name": "DVD", "external_name": "InStat_DVDPlayer", "value": ""}]}, {"group_name": "light", "name": "\u706f\u5149\u914d\u7f6e", "params": [{"name": "\u65e5\u95f4\u884c\u8f66\u706f", "external_name": "OutStat_DaytimeRunningLights", "value": ""}, {"name": "\u524d\u5927\u706f\u81ea\u52a8\u5f00\u95ed", "external_name": "OutStat_FLightClose", "value": ""}, {"name": "\u524d\u96fe\u706f", "external_name": "OutStat_FfogLamp", "value": ""}, {"name": "\u524d\u5927\u706f\u81ea\u52a8\u6e05\u6d17\u529f\u80fd", "external_name": "OutStat_FLightAutoClean", "value": ""}, {"name": "\u524d\u5927\u706f\u968f\u52a8\u8f6c\u5411", "external_name": "OutStat_FLightSteer", "value": ""}, {"name": "\u524d\u5927\u706f\u7c7b\u578b", "external_name": "OutStat_FrontLightType", "value": ""}]}, {"group_name": "glass", "name": "\u73bb\u7483/\u540e\u89c6\u955c", "params": [{"name": "\u524d\u7535\u52a8\u8f66\u7a97", "external_name": "The_front_power_window", "value": ""}, {"name": "\u540e\u7535\u52a8\u8f66\u7a97", "external_name": "After_the_electric_window", "value": ""}, {"name": "\u5916\u540e\u89c6\u955c\u7535\u52a8\u8c03\u8282", "external_name": "OutStat_ReMirrorElecTune", "value": ""}, {"name": "\u5916\u540e\u89c6\u955c\u52a0\u70ed\u529f\u80fd", "external_name": "OutStat_ReMirrorHot", "value": ""}, {"name": "\u5185\u540e\u89c6\u955c\u9632\u7729\u76ee\u529f\u80fd", "external_name": "OutStat_ReMirrorDazzle", "value": ""}, {"name": "\u5916\u540e\u89c6\u955c\u7535\u52a8\u6298\u53e0\u529f\u80fd", "external_name": "OutStat_ReMirrorFold", "value": ""}, {"name": "\u5916\u540e\u89c6\u955c\u8bb0\u5fc6\u529f\u80fd", "external_name": "OutStat_ReMirrormemory", "value": ""}, {"name": "\u540e\u7a97\u906e\u9633\u5e18", "external_name": "OutStat_BackCurtain", "value": ""}, {"name": "\u540e\u6392\u4fa7\u906e\u9633\u5e18", "external_name": "OutStat_SecondRowCurtain", "value": ""}, {"name": "\u906e\u9633\u677f\u5316\u5986\u955c", "external_name": "InStat_FaceMirror", "value": ""}, {"name": "\u540e\u96e8\u5237\u5668", "external_name": "OutStat_BBrushSensor", "value": ""}]}, {"group_name": "refrigeration", "name": "\u7a7a\u8c03/\u51b0\u7bb1", "params": [{"name": "\u7a7a\u8c03\u63a7\u5236\u65b9\u5f0f", "external_name": "InStat_AirCType", "value": ""}, {"name": "\u540e\u6392\u72ec\u7acb\u7a7a\u8c03", "external_name": "InStat_BAirCSystem", "value": ""}, {"name": "\u6e29\u5ea6\u5206\u533a\u63a7\u5236", "external_name": "InStat_TemperSubCount", "value": ""}, {"name": "\u8f66\u8f7d\u51b0\u7bb1", "external_name": "InStat_carFridge", "value": ""}]}], "config_is_ready": "true", "procedure": {"transferRequest": "", "purchaseTax": "1", "drivingLicense": "\u6709", "registration": "\u6709", "annualDue": "", "strongInsurance": "", "commercialInsurance": "", "carInvoice": "\u6709", "carWarranty": "\u8fc7\u4fdd", "key": "2", "maintenanceManual": "\u6709", "instructions": "\u6709", "unHandleIllegal": "\u65e0", "transferTickets": "\u6709", "newPlace": "1", "transferFee": "1", "freight": "1", "mentionFee": "1", "proceduresSpend": "1"}, "procedure_is_ready": "false"}
        data_info={"config":[{"group_name":"basic","name":"基本参数","params":[{"external_name":"Body_Doors","name":"车门数(个)","value":""},{"external_name":"Perf_SeatNum","name":"座位数(个)","value":""},{"external_name":"Engine_ExhaustForFloat","name":"排量(L)","value":""},{"external_name":"Oil_FuelType","name":"燃料类型","value":""},{"external_name":"UnderPan_ForwardGearNum","name":"挡位个数(个)","value":""},{"external_name":"UnderPan_TransmissionType","name":"变速箱类型","value":""},{"external_name":"Perf_DriveType","name":"驱动方式","value":""}]},{"group_name":"security","name":"主/被动安全设备","params":[{"external_name":"Safe_DriverGasBag","name":"驾驶位安全气囊","value":""},{"external_name":"Safe_SubDriverGasBag","name":"副驾驶位安全气囊","value":""},{"external_name":"Safe_FsadGasbag","name":"前排侧安全气囊","value":""},{"external_name":"Safe_BsadGasbag","name":"后排侧安全气囊","value":""},{"external_name":"Safe_FheadGasbag","name":"前排头部气囊(气帘)","value":""},{"external_name":"Safe_KneeGasBag","name":"膝部气囊","value":""},{"external_name":"InStat_BeltBag","name":"安全带气囊","value":""},{"external_name":"UnderPan_TyrePressureWatcher","name":"胎压监测装置","value":""},{"external_name":"Safe_ABS","name":"刹车防抱死(ABS)","value":""},{"external_name":"InStat_blindspotdetection","name":"盲点检测/并线辅助","value":""},{"external_name":"InStat_NightVisionSystem","name":"夜视系统","value":""}]},{"group_name":"accessory","name":"辅助/操控配置","params":[{"external_name":"UnderPan_PRadar","name":"泊车雷达(车前)","value":""},{"external_name":"UnderPan_RRadar","name":"倒车雷达(车后)","value":""},{"external_name":"UnderPan_RImage","name":"倒车影像","value":""},{"external_name":"InStat_PanoramicCamera","name":"全景摄像头","value":""},{"external_name":"InStat_SpeedCruise","name":"定速巡航","value":""},{"external_name":"InStat_Automaticcruise","name":"自适应巡航","value":""},{"external_name":"InStat_AutoParking","name":"自动泊车入位","value":""},{"external_name":"InStat_UphillAuxiliary","name":"上坡辅助","value":""},{"external_name":"InStat_AutoPark","name":"自动驻车","value":""},{"external_name":"InStat_HDC","name":"陡坡缓降","value":""},{"external_name":"Safe_Remotedriving","name":"遥控驾驶","value":""}]},{"group_name":"external","name":"外部/防盗配置","params":[{"external_name":"Body_Louver","name":"天窗型式","value":""},{"external_name":"OutStat_SportsAppearanceKit","name":"运动外观套件","value":""},{"external_name":"Aluminum_alloy_wheels # 没有标明","name":"铝合金轮圈","value":""},{"external_name":"Induction_trunk","name":"感应行李厢","value":""},{"external_name":"OutStat_TopSnelf","name":"车顶行李箱架","value":""},{"external_name":"InStat_AIgnitionSys","name":"无钥匙启动系统","value":""},{"external_name":"nokey_into","name":"无钥匙进入系统","value":""},{"external_name":"InStat_RemoteStart","name":"遥控启动","value":""},{"external_name":"OutStat_InductEmpennage","name":"后导流尾翼","value":""}]},{"group_name":"internal","name":"内部配置","params":[{"external_name":"InStat_MultiFuncSteer","name":"多功能方向盘","value":""},{"external_name":"InStat_SteerEtc","name":"换挡拨片","value":""},{"external_name":"Steering_Wheel_hot","name":"方向盘加热","value":""},{"external_name":"InStat_SteerMomery","name":"方向盘记忆设置","value":""},{"external_name":"InStat_SteerMaterial","name":"方向盘表面材料","value":""},{"external_name":"InStat_Hud","name":"HUD抬头数字显示","value":""}]},{"group_name":"seat","name":"座椅配置","params":[{"external_name":"InStat_SeatMaterial","name":"座椅材料","value":""},{"external_name":"InStat_SportSeat","name":"运动座椅","value":""},{"external_name":"InStat_DSeatProp","name":"驾驶座腰部支撑调节","value":""},{"external_name":"InStat_AdjustableShoulderSupport","name":"驾驶座肩部支撑调节","value":""},{"external_name":"InStat_DSeatTuneType","name":"驾驶座座椅调节方式","value":""},{"external_name":"InStat_DASeatTuneType","name":"副驾驶座椅调节方式","value":""},{"external_name":"InStat_ElectricSeatMemory","name":"电动座椅记忆","value":""},{"external_name":"Heated_front_seats","name":"前排座椅加热","value":""},{"external_name":"Heated_rear_seats","name":"后排座椅加热","value":""},{"external_name":"The_front_seat_ventilation","name":"前排座椅通风","value":""},{"external_name":"Rear_seat_ventilation","name":"后排座椅通风","value":""},{"external_name":"InStat_SeatKnead","name":"座椅按摩功能","value":""},{"external_name":"InStat_3rdRowSeats","name":"第三排座椅","value":""}]},{"group_name":"multimedia","name":"多媒体配置","params":[{"external_name":"InStat_GPS","name":"GPS导航系统","value":""},{"external_name":"InStat_CCEscreen","name":"中控台液晶屏","value":""},{"external_name":"InStat_BEscreen","name":"后排液晶屏","value":""},{"external_name":"InStat_Bluetooth","name":"蓝牙系统","value":""},{"external_name":"InStat_WireLink","name":"无线上网功能","value":""},{"external_name":"InStat_Video","name":"车载电视","value":""},{"external_name":"InStat_CDPlayer","name":"CD","value":""},{"external_name":"InStat_DVDPlayer","name":"DVD","value":""}]},{"group_name":"light","name":"灯光配置","params":[{"external_name":"OutStat_DaytimeRunningLights","name":"日间行车灯","value":""},{"external_name":"OutStat_FLightClose","name":"前大灯自动开闭","value":""},{"external_name":"OutStat_FfogLamp","name":"前雾灯","value":""},{"external_name":"OutStat_FLightAutoClean","name":"前大灯自动清洗功能","value":""},{"external_name":"OutStat_FLightSteer","name":"前大灯随动转向","value":""},{"external_name":"OutStat_FrontLightType","name":"前大灯类型","value":""}]},{"group_name":"glass","name":"玻璃/后视镜","params":[{"external_name":"The_front_power_window","name":"前电动车窗","value":""},{"external_name":"After_the_electric_window","name":"后电动车窗","value":""},{"external_name":"OutStat_ReMirrorElecTune","name":"外后视镜电动调节","value":""},{"external_name":"OutStat_ReMirrorHot","name":"外后视镜加热功能","value":""},{"external_name":"OutStat_ReMirrorDazzle","name":"内后视镜防眩目功能","value":""},{"external_name":"OutStat_ReMirrorFold","name":"外后视镜电动折叠功能","value":""},{"external_name":"OutStat_ReMirrormemory","name":"外后视镜记忆功能","value":""},{"external_name":"OutStat_BackCurtain","name":"后窗遮阳帘","value":""},{"external_name":"OutStat_SecondRowCurtain","name":"后排侧遮阳帘","value":""},{"external_name":"InStat_FaceMirror","name":"遮阳板化妆镜","value":""},{"external_name":"OutStat_BBrushSensor","name":"后雨刷器","value":""}]},{"group_name":"refrigeration","name":"空调/冰箱","params":[{"external_name":"InStat_AirCType","name":"空调控制方式","value":""},{"external_name":"InStat_BAirCSystem","name":"后排独立空调","value":""},{"external_name":"InStat_TemperSubCount","name":"温度分区控制","value":""},{"external_name":"InStat_carFridge","name":"车载冰箱","value":""}]}],"config_is_ready":"true","procedure":{"annualDue":"2019-05-17","carInvoice":"有","carWarranty":"过保","commercialInsurance":"2019-05-17","drivingLicense":"有","freight":"","instructions":"有","key":"2","maintenanceManual":"有","mentionFee":"","newPlace":"1","proceduresSpend":"1","purchaseTax":"1","registration":"有","strongInsurance":"2019-05-17","transferFee":"1","transferRequest":"52","transferTickets":"有","unHandleIllegal":"无"},"procedure_is_ready":"true"}
        data_info=json.dumps(data_info)
        data={"info":data_info,
              "info_has_changes":"false"}
        cookies = {
            "csrf-token": token,
            "session": self.session
        }
        headers = {"X-CSRF-Token": token,
                   "Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(url, headers=headers, data=data, cookies=cookies, verify=False)
        #print(response.text)
        #第四步，上传车辆照片
        img_path=Datasource.upload_img(self,r'C:\Users\93439\Desktop\timg.jpg')
        url='https://q.test.dos.cheanjia.net/api/v1/used_car/ticket/car_info/%s/images'%info_id
        cookies = {
            "csrf-token": token,
            "session": self.session
        }
        headers = {"X-CSRF-Token": token,
                   "Content-Type": "application/x-www-form-urlencoded"}
        data={"info_has_changes": "1", "mask_left_front_image_url": img_path, "left_front_image_url": img_path, "mask_left_image_url": img_path, "left_image_url": img_path, "mask_front_chair_image_url": img_path, "front_chair_image_url": img_path, "mask_dashboard_image_url": img_path, "dashboard_image_url": img_path, "mask_back_chair_image_url": img_path, "back_chair_image_url": img_path, "mask_central_control_board_image_url": img_path, "central_control_board_image_url": img_path, "mask_end_image_url": img_path, "end_image_url": img_path, "mask_trunk_bottom_image_url": img_path, "trunk_bottom_image_url": img_path, "mask_right_end_image_url": img_path, "right_end_image_url": img_path, "mask_engine_compartment_image_url": img_path, "engine_compartment_image_url": img_path, "mask_factory_nameplate_image_url": img_path, "factory_nameplate_image_url": img_path, "mask_other_1_image_url": img_path, "other_1_image_url": img_path, "mask_other_2_image_url": img_path, "other_2_image_url": img_path, "mask_other_3_image_url": img_path, "other_3_image_url": img_path, "mask_other_4_image_url": img_path, "other_4_image_url": img_path, "mask_other_5_image_url": img_path, "other_5_image_url": img_path}
        response = requests.post(url, headers=headers, data=data, cookies=cookies, verify=False)
        #print(response.text)
        #第五步，评估检测信息,分别为车头，左侧，车尾，右侧，机械内饰，电器
        url='https://q.test.dos.cheanjia.net/api/v1/used_car/ticket/car_info/%s/inspection'%info_id
        cookies = {
            "csrf-token": token,
            "session": self.session
        }
        headers = {"X-CSRF-Token": token,
                   "Content-Type": "application/x-www-form-urlencoded"}
        # 先评估车头
        data_info={"head":[{"id":"1","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"前保险杠"},{"id":"2","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"左前大灯"},{"id":"3","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"右前大灯"},{"id":"4","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"前横梁"},{"id":"5","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"水箱支架"},{"id":"6","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"左前纵梁"},{"id":"7","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"右前纵梁"},{"id":"8","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"左前避震器座"},{"id":"9","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"右前避震器座"},{"id":"10","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"防火墙"},{"id":"11","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"前挡风玻璃"},{"id":"12","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"车顶"},{"id":"13","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"引擎盖"},{"id":"14","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"车底板"}]}
        #data_info="{\"head\":[{\"id\":1,\"title\":[\"正常\"],\"damageList\":[{\"key\":\"1\",\"value\":\"正常\",\"selected\":true,\"__keyPath\":{\"selected\":true}}],\"note\":\"前保险杠\",\"images\":[],\"message\":\"\"},{\"id\":2,\"title\":[\"正常\"],\"damageList\":[{\"key\":\"1\",\"value\":\"正常\",\"selected\":true,\"__keyPath\":{\"selected\":true}}],\"note\":\"左前大灯\",\"images\":[],\"message\":\"\"},{\"id\":3,\"title\":[\"正常\"],\"damageList\":[{\"key\":\"1\",\"value\":\"正常\",\"selected\":true,\"__keyPath\":{\"selected\":true}}],\"note\":\"右前大灯\",\"images\":[],\"message\":\"\"},{\"id\":4,\"title\":[\"正常\"],\"damageList\":[{\"key\":\"1\",\"value\":\"正常\",\"selected\":true,\"__keyPath\":{\"selected\":true}}],\"note\":\"前横梁\",\"images\":[],\"message\":\"\"},{\"id\":5,\"title\":[\"正常\"],\"damageList\":[{\"key\":\"1\",\"value\":\"正常\",\"selected\":true,\"__keyPath\":{\"selected\":true}}],\"note\":\"水箱支架\",\"images\":[],\"message\":\"\"},{\"id\":6,\"title\":[\"正常\"],\"damageList\":[{\"key\":\"1\",\"value\":\"正常\",\"selected\":true,\"__keyPath\":{\"selected\":true}}],\"note\":\"左前纵梁\",\"images\":[],\"message\":\"\"},{\"id\":7,\"title\":[\"正常\"],\"damageList\":[{\"key\":\"1\",\"value\":\"正常\",\"selected\":true,\"__keyPath\":{\"selected\":true}}],\"note\":\"右前纵梁\",\"images\":[],\"message\":\"\"},{\"id\":8,\"title\":[\"正常\"],\"damageList\":[{\"key\":\"1\",\"value\":\"正常\",\"selected\":true,\"__keyPath\":{\"selected\":true}}],\"note\":\"左前避震器座\",\"images\":[],\"message\":\"\"},{\"id\":9,\"title\":[\"正常\"],\"damageList\":[{\"key\":\"1\",\"value\":\"正常\",\"selected\":true,\"__keyPath\":{\"selected\":true}}],\"note\":\"右前避震器座\",\"images\":[],\"message\":\"\"},{\"id\":10,\"title\":[\"正常\"],\"damageList\":[{\"key\":\"1\",\"value\":\"正常\",\"selected\":true,\"__keyPath\":{\"selected\":true}}],\"note\":\"防火墙\",\"images\":[],\"message\":\"\"},{\"id\":11,\"title\":[\"正常\"],\"damageList\":[{\"key\":\"1\",\"value\":\"正常\",\"selected\":true,\"__keyPath\":{\"selected\":true}}],\"note\":\"前挡风玻璃\",\"images\":[],\"message\":\"\"},{\"id\":12,\"title\":[\"正常\"],\"damageList\":[{\"key\":\"1\",\"value\":\"正常\",\"selected\":true,\"__keyPath\":{\"selected\":true}}],\"note\":\"车顶\",\"images\":[],\"message\":\"\"},{\"id\":13,\"title\":[\"正常\"],\"damageList\":[{\"key\":\"1\",\"value\":\"正常\",\"selected\":true,\"__keyPath\":{\"selected\":true}}],\"note\":\"引擎盖\",\"images\":[],\"message\":\"\"},{\"id\":14,\"title\":[\"正常\"],\"damageList\":[{\"key\":\"1\",\"value\":\"正常\",\"selected\":true,\"__keyPath\":{\"selected\":true}}],\"note\":\"车底板\",\"images\":[],\"message\":\"\"}]}"
        data_info = json.dumps(data_info)
        data = {"inspection": data_info,
                "info_has_changes": "false"}
        response = requests.post(url, headers=headers, data=data, cookies=cookies, verify=False)
        #print(response.text)
        #评估左侧
        data_info={"left":[{"id":"15","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"左前叶子板"},{"id":"16","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"左前轮毂"},{"id":"17","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"左前轮胎"},{"id":"18","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"左后视镜"},{"id":"19","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"左前门"},{"id":"20","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"左A柱"},{"id":"21","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"左后门"},{"id":"22","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"左B柱"},{"id":"23","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"左C柱"},{"id":"24","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"左后叶子板"},{"id":"25","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"左后轮毂"},{"id":"26","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"左后轮胎"},{"id":"27","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"左裙边"}]}
        data_info = json.dumps(data_info)
        data = {"inspection": data_info,
                "info_has_changes": "true"}
        response = requests.post(url, headers=headers, data=data, cookies=cookies, verify=False)
        #评估车尾
        data_info={"tail":[{"id":"28","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"左后大灯"},{"id":"29","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"右后大灯"},{"id":"30","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"后行李箱盖"},{"id":"31","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"后保险杠"},{"id":"32","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"后挡风玻璃"},{"id":"33","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"备胎"},{"id":"34","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"随车工具"},{"id":"35","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"备胎室"}]}
        data_info = json.dumps(data_info)
        data = {"inspection": data_info,
                "info_has_changes": "true"}
        response = requests.post(url, headers=headers, data=data, cookies=cookies, verify=False)
        #评估右侧
        data_info={"right":[{"id":"36","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"右后叶子板"},{"id":"37","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"右后轮毂"},{"id":"38","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"右后轮胎"},{"id":"39","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"右后门"},{"id":"40","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"右C柱"},{"id":"41","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"右B柱"},{"id":"42","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"右前门"},{"id":"43","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"右A柱"},{"id":"44","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"右后视镜"},{"id":"45","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"右前叶子板"},{"id":"46","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"右前轮毂"},{"id":"47","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"右前轮胎"},{"id":"48","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"右裙边"}]}
        data_info = json.dumps(data_info)
        data = {"inspection": data_info,
                "info_has_changes": "true"}
        response = requests.post(url, headers=headers, data=data, cookies=cookies, verify=False)
        #评估机械内饰
        data_info={"machine_interior":[{"id":"49","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"发动机"},{"id":"50","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"变速箱"},{"id":"51","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"转向机"},{"id":"52","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"减震器"},{"id":"53","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"消音器"},{"id":"54","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"座椅"},{"id":"55","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"安全带"},{"id":"56","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"顶蓬"},{"id":"57","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"门饰板"},{"id":"58","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"地毯"},{"id":"59","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"换挡杆"},{"id":"60","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"中央控制台"},{"id":"61","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"方向盘"},{"id":"62","title":["无泥沙/无更换过/无清理痕迹"],"damageList":[{"key":"1","value":"无泥沙/无更换过/无清理痕迹","selected":"true","__keyPath":{"selected":"true"}}],"note":"保险盒"},{"id":"63","title":["无水渍或泥沙"],"damageList":[{"key":"1","value":"无水渍或泥沙","selected":"true","__keyPath":{"selected":"true"}}],"note":"EUC接口处"},{"id":"64","title":["无锈迹"],"damageList":[{"key":"1","value":"无锈迹","selected":"true","__keyPath":{"selected":"true"}}],"note":"点烟器底座"},{"id":"65","title":["无水渍或泥沙"],"damageList":[{"key":"1","value":"无水渍或泥沙","selected":"true","__keyPath":{"selected":"true"}}],"note":"烟灰缸底座"},{"id":"66","title":["无霉味/无水渍或泥沙"],"damageList":[{"key":"1","value":"无霉味/无水渍或泥沙","selected":"true","__keyPath":{"selected":"true"}}],"note":"驾驶舱和后备箱内"},{"id":"67","title":["无水渍或泥沙"],"damageList":[{"key":"1","value":"无水渍或泥沙","selected":"true","__keyPath":{"selected":"true"}}],"note":"后排座椅坐垫底部"},{"id":"68","title":["无火烧或烟熏"],"damageList":[{"key":"1","value":"无火烧或烟熏","selected":"true","__keyPath":{"selected":"true"}}],"note":"发动机线束及橡胶制品"},{"id":"69","title":["无火烧或烟熏"],"damageList":[{"key":"1","value":"无火烧或烟熏","selected":"true","__keyPath":{"selected":"true"}}],"note":"车辆覆盖件及驾驶舱"}]}
        data_info = json.dumps(data_info)
        data = {"inspection": data_info,
                "info_has_changes": "true"}
        response = requests.post(url, headers=headers, data=data, cookies=cookies, verify=False)
        #评估电器
        data_info={"appliance":[{"id":"70","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"音响"},{"id":"71","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"导航"},{"id":"72","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"电动后视镜"},{"id":"73","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"电动车窗"},{"id":"74","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"天窗"},{"id":"75","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"空调"},{"id":"76","title":["正常"],"damageList":[{"key":"1","value":"正常","selected":"true","__keyPath":{"selected":"true"}}],"note":"仪表灯"}]}
        data_info = json.dumps(data_info)
        data = {"inspection": data_info,
                "info_has_changes": "true"}
        response = requests.post(url, headers=headers, data=data, cookies=cookies, verify=False)
        #print(response.text)
        #第六步，评估简述
        url = 'https://q.test.dos.cheanjia.net/api/v1/used_car/ticket/car_info/%s/qymp_remark' % info_id
        data = {"note": "zuixin", "info_has_changes": "true"}
        cookies = {
            "csrf-token": token,
            "session": self.session
        }
        headers = {"X-CSRF-Token": token,
                   "Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(url, headers=headers, data=data, cookies=cookies, verify=False)
        #print(response.text)
        #最后一步，生成评估报告，完成整个评估过程
        url='https://q.test.dos.cheanjia.net/api/v1/used_car/ticket/car_info/%s/status'%info_id
        headers = {"X-CSRF-Token": token,
                   "Content-Type": "application/json"}
        data={}
        response = requests.put(url, headers=headers, data=data, cookies=cookies, verify=False)
        #print(response.text)
        return car_no


    #定义一个函数，待估价状态的进行估价,返回该车牌号,数据传递时候，价格是除以100的
    def gujia(self,car_no,price):
        token=Datasource.get_login_token(self)
        id = str(Datasource.get_car_id(self,car_no))
        url='https://q.test.dos.cheanjia.net/api/v1/used_car/ticket/%s/appraise'%id
        data = {"note": "估价", "price": price}
        cookies = {
            "csrf-token": token,
            "session": self.session
        }
        headers = {"X-CSRF-Token": token,
                   "Content-Type": "application/x-www-form-urlencoded"}
        response = requests.put(url, headers=headers, data=data, cookies=cookies, verify=False)
        #print(response.text)
        return car_no

    #定义一个函数,待签合同状态的进行签合同操作，返回该车牌号
    def qianhetong(self,car_no):
        token=Datasource.get_login_token(self)
        img_path = Datasource.upload_img(self, r'C:\Users\93439\Desktop\timg.jpg')
        id=str(Datasource.get_car_id(self, car_no))
        url='https://q.test.dos.cheanjia.net/api/v1/used_car/ticket/%s/contract'%id
        # files = {
        #     "contract_image_url": ("timg.jpg", open(r"C:\Users\93439\Desktop\timg.jpg", "rb")),
        #     "vehicle_front_45_degree_image_url": ("timg.jpg", open(r"C:\Users\93439\Desktop\timg.jpg", "rb")),
        #     "vehicle_key_image_url": ("timg.jpg", open(r"C:\Users\93439\Desktop\timg.jpg", "rb")),
        #     "vehicle_license_image_url": ("timg.jpg", open(r"C:\Users\93439\Desktop\timg.jpg", "rb")),
        #     "vehicle_registration_image_url": ("timg.jpg", open(r"C:\Users\93439\Desktop\timg.jpg", "rb")),
        #     "personal_identification_front_image_url": ("timg.jpg", open(r"C:\Users\93439\Desktop\timg.jpg", "rb")),
        #     "personal_identification_back_image_url": ("timg.jpg", open(r"C:\Users\93439\Desktop\timg.jpg", "rb")),
        # }

        data={
            "channel": "1",
            "replace_detail": "1",
            "appraiser": "李晓良",
            "appraiser_id": "1835",
            "price": "9900000",
            "recepit_name": "接口数据",
            "bank_name": "招行",
            "bank_card_number": "621455555555555",
            "note": "备注内容",
            "appraised_price": "100000",
            "channel_name": "销售端潜客",
            "latest_operator[id]": "1835",
            "latest_operator[name]": "李晓良",
            "owner_name": "接口数据",
            "replace_detail_name": "以旧换新",
            #"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTgwNjE4MTcsImlzX2xvZ2luIjp0cnVlLCJ1aWQiOjE4MTN9.NWiq-oX4WFDuE9nL-5L-AA1CfgsXgE4pASxqjH3csKU",
            "images": "",
            "contract_image_url": img_path,
            "vehicle_front_45_degree_image_url": img_path,
            "vehicle_key_image_url": img_path,
            "vehicle_license_image_url": img_path,
            "vehicle_registration_image_url": img_path,
            "personal_identification_front_image_url": img_path,
            "personal_identification_back_image_url":img_path
        }
        cookies = {
            "csrf-token": token,
            "session": self.session
        }
        headers = {"X-CSRF-Token": token,
                   "Content-Type": "application/x-www-form-urlencoded"}
        response = requests.put(url, headers=headers, data=data,cookies=cookies,verify=False)
        # print(response.json())
        return car_no

    #定义一个方法，待财务审核进行财务审核操作,result为审核的结果，approve为通过，reject为驳回
    def caiwushenhe(self,car_no,result):
        token=Datasource.get_login_token(self)
        id = str(Datasource.get_car_id(self, car_no))
        url = 'https://q.test.dos.cheanjia.net/api/v1/used_car/ticket/%s/finance/review' % id
        cookies = {
            "csrf-token": token,
            "session": self.session
        }
        headers = {"X-CSRF-Token": token,
                   "Content-Type": "application/x-www-form-urlencoded"}
        data={
            "note":"自动化审核备注内容",
            "action":result
        }
        response = requests.post(url, headers=headers, data=data, cookies=cookies, verify=False)
        #print(response.text)
        return car_no

    #定义一个方法，待店总审核进行店总审核操作,result为审核的结果，approve为通过，reject为驳回
    def dianzongshenhe(self,car_no,result):
        token=Datasource.get_login_token(self)
        id = str(Datasource.get_car_id(self,car_no))
        url = 'https://q.test.dos.cheanjia.net/api/v1/used_car/ticket/%s/manager/review' % id
        cookies = {
            "csrf-token": token,
            "session": self.session
        }
        headers = {"X-CSRF-Token": token,
                   "Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "note": "自动化审核备注内容",
            "action": result
        }
        response = requests.post(url, headers=headers, data=data, cookies=cookies, verify=False)
        #print(response.text)
        return car_no

    #定义一个方法，待财务放款的进行财务放款操作
    def caiwufangkuang(self,car_no):
        token=Datasource.get_login_token(self)
        id = str(Datasource.get_car_id(self, car_no))
        url = 'https://q.test.dos.cheanjia.net/api/v1/used_car/ticket/%s/finish' % id
        cookies = {
            "csrf-token": token,
            "session": self.session
        }
        headers = {"X-CSRF-Token": token,
                   "Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "price": "880000",
            "recepit_name":"",
            "bank_name": "招商银行",
            "bank_card_number": "888888888888888",
            "note": "自动化测试数据",
            "appraised_price": "",
            "appraiser": "",
            "appraiser_id": "",
            "appraiser_role": "",
            "channel": "",
            "channel_name":"",
            "id": "",
            "images": "",
            "latest_operator[id]": "",
            "latest_operator[name]": "",
            "owner_name": "",
            "replace_detail": "",
            "replace_detail_name": "",
            "token": "",
            "image_url_payment":r"C:\Users\93439\Desktop\timg.jpg",
        }
        response = requests.put(url, headers=headers, data=data, cookies=cookies, verify=False)
        #print(response.text)
        return car_no

if __name__ == '__main__':
    # car_no=Datasource().newclue()
    # print(car_no)
    # print(Datasource().pinggu(car_no))
    # print(Datasource().gujia(car_no,100000))
    # Datasource().qianhetong(car_no)
    # print(Datasource().caiwushenhe(car_no,"approve"))
    # print(Datasource().dianzongshenhe(car_no,"approve"))
    # print(Datasource().caiwufangkuang(car_no))
    print(Datasource().caiwushenhe(Datasource().qianhetong(Datasource().gujia(Datasource().pinggu(Datasource().newclue()),100000)),"approve"))