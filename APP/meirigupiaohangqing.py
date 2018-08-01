#-*- coding: utf-8 -*-

from common.base import Base
import tushare as ts

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

        # self.finacial_data.dopost('TRUNCATE TABLE stock_hangqing_date')
        # self.finacial_data.dopost('TRUNCATE TABLE stock_code_name')

        #在股市收盘后，获取股票当日行情
        hangqing = ts.get_today_all()
        today = self.base.gettoday()
        hangqing['date'] = today.replace('/','-')
        #股市收盘后，trade现价就是股票的收盘价。
        hangqing.rename(columns={'trade': 'close'}, inplace=True)
        #去重
        hangqing_qc = hangqing.drop_duplicates().sort_values(by='code').reset_index(drop=True)
        # print(hangqing_qc)
        self.base.batchwri(hangqing_qc, 'stock_hangqing_date',self.finacial_data)
        self.base.batchwri(hangqing_qc[['code','name']], 'stock_code_name', self.finacial_data)

        #股票代码-名称对照表去重
        duizhao = self.finacial_data.getdata('stock_code_name')
        print(duizhao.size)
        duizhao_qc = duizhao.drop_duplicates().sort_values(by='code').reset_index(drop=True)
        # print(df)
        self.finacial_data.dopost('TRUNCATE TABLE stock_code_name')
        self.base.batchwri(duizhao_qc, 'stock_code_name', self.finacial_data)


#测试，暂定每日股票收盘后更新一次
if __name__ == '__main__':
    base = Base()
    financial_data = base.conn('financial_data')
    conns = {'financial_data': financial_data}
    meirihangqing = GeGuHangQing()
    meirihangqing(conns)
    financial_data.close()


