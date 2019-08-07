import time

'''时间处理'''
class GetTime():

    def get_time_by_second(self):
        '''精确到秒'''
        # print(time.time())  # time.time()获取的是从1970年到现在的间隔，单位是秒
        # print(time.localtime())
        # 格式化时间，按照 2017-04-15 13:46:32的格式打印出来
        # new_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        # 格式化时间，按照 20170415_134632的格式打印出
        new_time = time.strftime('%Y%m%d_%H%M%S', time.localtime())
        return new_time

    def get_time_by_day(self):
        '''精确到天'''
        new_time = time.strftime('%Y-%m-%d', time.localtime())
        return new_time
