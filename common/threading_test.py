#-*- coding: utf-8 -*-

import threading

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

class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self, jstj, mul_t=4):
        '''
        多线程执行检索任务
        :param jstj: 检索条件，列表
        :param mul_t: 线程数量
        :return:
        '''

        # self.func(*self.args)

        # 将检索条件按线程数量均分
        try:
            k = int(len(jstj) / mul_t)
        except Exception as e:
            raise e
        code_t = []
        for i in range(mul_t):
            if i != (mul_t - 1):
                code = code_list[i * k:(i + 1) * k].reset_index(drop=True)
            else:
                code = code_list[i * k:].reset_index(drop=True)
            code_t.append(code)

        start = ctime()
        print('starting at: ', start)
        # 多线程
        threads = []
        for i in range(mul_t):
            t = threading.Thread(target=ThreadFunc(self.get_today_close,
                                                   ('2018-07-27', code_t[i]),
                                                   self.get_today_close.__name__))
            threads.append(t)
        for i in range(mul_t):
            threads[i].start()
        for i in range(mul_t):
            threads[i].join()
        print('all DONE at: ', ctime(), '  start at: ', start)

        result = pd.concat(self.close_res).reset_index(drop=True)
        print(result)
