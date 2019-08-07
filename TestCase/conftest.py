import pytest
from appium import webdriver
from Common.get_path import caps_dir
import yaml
from Page_Objects.common_business import CommBus
from time import sleep

def baseDriver(server_port=4723,noReset=None,automationName=None,**kwargs):
    #将默认的配置数据读取出来
    fs = open(caps_dir + "/caps.yaml")
    desired_caps = yaml.load(fs)
    #调整参数
    if noReset is not None:
        desired_caps["noReset"] = noReset
    if automationName is not None:
        desired_caps["automationName"] = automationName
    #返回一个启动对象 - driver
    return webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(server_port), desired_caps)

# @pytest.fixture
@pytest.fixture(scope="module")
def startApp():
    "单纯启动APP，返回driver"
    driver = baseDriver()
    sleep(5)
    #切换到工作台首页
    CommBus(driver).switchTo_usedCar()
    yield (driver)
    pass

@pytest.fixture(scope="class")
def swich_to_usedCar():
    #切换到二手车首页
    driver = baseDriver()
    sleep(3)
    CommBus(driver).confirm_and_swichTo_usedCar()
    yield
    pass





