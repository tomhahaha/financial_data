#-*- coding: utf-8 -*-

import threading
from time import ctime
import logging.config
import configparser

conf = configparser.ConfigParser()
conf.read("../common/test.conf")
logger = logging.getLogger()
logger.setLevel(logging.INFO)
fh = logging.FileHandler(conf.get('path','log_path'), mode='a')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)
print('这里是测试内容：{}'.format(conf.get('path','log_path')))

#执行多线程处理，处理列表数据
class ThreadFunc(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        self.res = self.func(*self.args)



#     def __call__(self, jstj, mul_t=4):
#         '''
#         多线程执行检索任务
#         :param jstj: 检索条件，或待处理的数据，列表
#         :param mul_t: 线程数量
#         :return:
#         '''
#
#         # 将检索条件按线程数量均分
#         try:
#             k = int(len(jstj) / mul_t)
#         except Exception as e:
#             logger.info(u"均分失败！\n" + u"失败原因：")
#             logger.info(e)
#             raise e
#         tj_list = []
#         for i in range(mul_t):
#             if i != (mul_t - 1):
#                 tj = jstj[i * k:(i + 1) * k].reset_index(drop=True)
#             else:
#                 tj = jstj[i * k:].reset_index(drop=True)
#             tj_list.append(tj)
#
#         start = ctime()
#         print('starting at: ', start)
#         # 多线程
#         threads = []
#         try:
#             for i in range(mul_t):
#                 t = threading.Thread(target=self.getfun())
#                 threads.append(t)
#             for i in range(mul_t):
#                 threads[i].start()
#             for i in range(mul_t):
#                 threads[i].join()
#         except Exception as e:
#             logger.info(u"多线程失败！\n" + u"失败原因：")
#             logger.info(e)
#             raise e
#         print('all DONE at: ', ctime(), '  start at: ', start)
#
# if __name__ == "__main__":
#
