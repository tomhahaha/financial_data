#-*- coding: utf-8 -*-

from test.threading_test import ThreadFunc
from common.base_test import Base
import tushare as ts
import pandas as pd
from time import ctime
import threading

'''
   股票每日行情数据:
        code	        股票代码
        date	        日期
        open	        开盘价
        high	        最高价
        settlement	    昨日收盘价
        low	            最低价
        volume	        成交量
        trade	        现价
        changepercent	涨跌幅
        turnoverratio	换手率
        amount	        成交金额
        per	            市盈率
        pb	            市净率
        mktcap	        总市值
        nmc	            流通市值
        
    股票代码-名字对照表
        code    股票代码
        name    股票名字
'''

#每日行情数据
class GeGuHangQing(object):
    def __init__(self):
        super(GeGuHangQing,self).__init__()
        self.close_res = []

    def __call__(self, conns, mul_t=4):
        '''
        抓取股票每日行情数据
        :param conns: 数据库连接
        :param mul_t: 线程数量
        :return: 数据存储在数据库
        '''
        self.base = Base()
        self.finacial_data = conns['financial_data']

        self.finacial_data.dopost('TRUNCATE TABLE stock_hangqing_date')
        self.finacial_data.dopost('TRUNCATE TABLE stock_code_name')

        #获取股票当日实时行情
        hangqing = ts.get_today_all()
        today = self.base.gettoday()
        hangqing['date'] = today.replace('/','-')
        hangqing.rename(columns={'trade': 'close'}, inplace=True)

        self.base.batchwri(hangqing, 'stock_hangqing_date',self.finacial_data)
        self.base.batchwri(hangqing.iloc[:,0:2], 'stock_code_name', self.finacial_data)

        # #多线程获取当日股票收盘价close
        # code_list = hangqing['code']
        # k = int(len(code_list) / mul_t)
        # code_t = []
        # for i in range(mul_t):
        #     if i != (mul_t-1):
        #         code = code_list[i*k:(i+1)*k].reset_index(drop=True)
        #     else:
        #         code = code_list[i*k:].reset_index(drop=True)
        #     code_t.append(code)
        #
        # start = ctime()
        # print('starting at: ', start)
        # #多线程
        # threads = []
        # for i in range(mul_t):
        #     t = threading.Thread(target=ThreadFunc(self.get_today_close,
        #                                            ('2018-07-27', code_t[i]),
        #                                            self.get_today_close.__name__))
        #     threads.append(t)
        # for i in range(mul_t):
        #     threads[i].start()
        # for i in range(mul_t):
        #     threads[i].join()
        # print('all DONE at: ', ctime(), '  start at: ', start)
        #
        # result = pd.concat(self.close_res).reset_index(drop=True)
        # print(result)

        # #合并每日行情与收盘价
        # hangqing_test = self.finacial_data.getdata('stock_hangqing_date')
        # new_hangqing = pd.merge(hangqing_test, result, on='code', how='left')
        # print(new_hangqing)

    # # 获取每日收盘价
    # def get_today_close(self, date, code_list):
    #     fin = []
    #     start = ctime()
    #     print('strat: ' + start)
    #
    #     for i in range(len(code_list)):
    #         code_tj = code_list['code'][i]
    #         # print(code_tj)
    #         df = ts.get_k_data(code_tj, start=date, end=date, autype=None).reset_index(drop=True)
    #         print(df)
    #         if df.empty:
    #             continue
    #         code = df['code'][0]
    #         # print(code)
    #         close = df['close'][0]
    #         # print(close)
    #         fin.append([code, close])
    #
    #     res = pd.DataFrame(fin, columns=['code', 'close'])
    #     print('End: ' + ctime() + ', start at' + start)
    #     # print(res)
    #     # self.base.batchwri(res, 'stock_close_20180727',self.finacial_data)
    #     self.close_res.append(res)


if __name__ == '__main__':
    base = Base()
    financial_data = base.conn('financial_data')
    conns = {'financial_data': financial_data}
    meirihangqing = GeGuHangQing()
    meirihangqing(conns)
    # meirihangqing.get_today_close(conns,'2018-07-27')
    financial_data.close()


