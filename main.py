import pytest
from Common.get_time import GetTime
time=GetTime().get_time_by_day()
report_name="test_submintClues_"+time+".html"

if __name__ == '__main__':
    pytest.main(['-v','-s','--reruns=2','TestCase/test_submitClues.py','--html=Out_Puts/html_report/report_name','--alluredir=allure-results'])
