import os
from Common.get_time import GetTime

'''路径管理'''
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
print(project_path)

test_report_path=os.path.join(project_path,'out_puts','html_report')
#日志按天分开
logfile_name=GetTime().get_time_by_day()+"_log.txt"
logs_path=os.path.join(project_path,'out_puts','test_logs',logfile_name)

test_case_path=os.path.join(project_path,'TestCase')
screenshot_path=os.path.join(project_path,'out_puts','screenshots')

caps_dir=os.path.join(project_path,'Desired_Caps')
