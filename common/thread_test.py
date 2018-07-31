#-*- coding: utf-8 -*-

import threading
from time import ctime
import logging.config
import configparser

from common.base_test import Base
import threading
from time import ctime
import pandas as pd
import tushare as ts



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

#多线程处理
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

#测试
def main(func, clsj, *args, mul_t=4):
    '''
    测试多线程处理
    :param func: 多线程运行函数
    :param mul_t: 线程数量
    :param clsj: 多线程处理的数据，列表类型
    :param args: 函数其余条件
    :return: 返回dataframe格式
    '''

    # 将处理数据按线程数量均分
    try:
        k = int(len(clsj) / mul_t)
    except Exception as e:
        logger.info(u"均分失败！\n" + u"失败原因：")
        logger.info(e)
        raise e
    sj_list = []
    for i in range(mul_t):
        if i != (mul_t - 1):
            sj = clsj[i * k:(i + 1) * k].reset_index(drop=True)
        else:
            sj = clsj[i * k:].reset_index(drop=True)
        sj_list.append(sj)

    start = ctime()
    print('starting at: ', start)
    # 多线程
    threads = []
    try:
        for i in range(mul_t):
            t = ThreadFunc(func, (clsj, *args), func.__name__)
            threads.append(t)
        for i in range(mul_t):
            threads[i].start()
        for i in range(mul_t):
            threads[i].join()
    except Exception as e:
        logger.info(u"多线程失败！\n" + u"失败原因：")
        logger.info(e)
        raise e
    print('all DONE at: ', ctime(), '  start at: ', start)

    for t in threads:
        print(t.getResult())


def get_today_close(date, code_list):

    fin = []
    #print(code_list)
    # start = ctime()
    # print('strat: '+start)

    for i in range(len(code_list)):
    # for i in range(0,10):
        code_tj = code_list['code'][i]
        #print(code_tj)
        df = ts.get_k_data(code_tj, start=date, end=date, autype=None).reset_index(drop=True)
        print(df)
        if df.empty:
            continue
        code = df['code'][0]
        #print(code)
        close = df['close'][0]
        #print(close)
        fin.append([code, close])

    res = pd.DataFrame(fin, columns=['code','close'])
    # print('End: '+ ctime() + ', start at' + start)
    return res

if __name__ == "__main__":
    base = Base()
    financial_data = base.conn('financial_data')
    conns = {'financial_data': financial_data}
    cnx = conns['financial_data']
    code_list = cnx.getdata('stock_code_name', ['code'])[0:1000]
    main(get_today_close, code_list, '2018-07-27')