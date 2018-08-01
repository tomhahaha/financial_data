# -*- coding: utf-8 -*-

from common.base import Base
import tushare as ts
import pandas as pd

'''
   大盘指数每日行情数据:
        code	    指数代码
        date	    日期
        change	    涨跌幅
        open	    开盘点位
        preclose	昨日收盘点位
        close	    收盘点位
        high	    最高点
        low	        最低点位
        volume	    成交量
        amount	    成交金额

   大盘代码-名字对照表
        code    指数代码
        name    指数名字
        date    出现的日期
'''


class DaPanHangQing(object):
    def __init__(self):
        super(DaPanHangQing, self).__init__()

    def __call__(self, conns):
        self.base = Base()
        self.finacial_data = conns['financial_data']

        #self.finacial_data.dopost('TRUNCATE TABLE dapan_hangqing_date')
        #self.finacial_data.dopost('TRUNCATE TABLE dapan_code_name')

        # 实时行情
        hangqing = ts.get_index()
        today = self.base.gettoday()
        hangqing['date'] = today.replace('/','-')
        #大盘指数每日行情数据
        self.base.batchwri(hangqing, 'dapan_hangqing_date', self.finacial_data)
        #大盘代码-名字对照表
        self.base.batchwri(hangqing[['code','name']], 'dapan_code_name', self.finacial_data)

        #大盘代码-名字对照表去重
        duizhao = self.finacial_data.getdata('dapan_code_name')
        duizhao.duplicated()
        duizhao.sort_index(by='code')
        self.finacial_data.dopost('TRUNCATE TABLE dapan_code_name')
        self.base.batchwri(hangqing[['code','name']], 'dapan_code_name', self.finacial_data)



if __name__ == '__main__':
    base = Base()
    financial_data = base.conn('financial_data')
    conns = {'financial_data': financial_data}
    meirihangqing = DaPanHangQing()
    meirihangqing(conns)
    financial_data.close()