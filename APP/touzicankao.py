import tushare as ts
import pandas as pd
from common.base import Base

class GerDataTouzicankao(object):
    def __init__(self):
        #self.code = '002337'
        self.df = pd.DataFrame()
    def profit_data(self,conns,top):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.profit_data(top)
        self.base.batchwri(self.df, 'fenpeiyuan', self.financial_data)
    def forecast_data(self,conns,year,quarter):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.forecast_data(year, quarter)
        self.base.batchwri(self.df, 'yejibaobiao', self.financial_data)
    def xsg_data(self,conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.xsg_data()
        self.base.batchwri(self.df, 'xianshougujiejin', self.financial_data)
    def fund_holdings(self,conns,year,quarter):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.fund_holdings(year, quarter)
        self.base.batchwri(self.df, 'jijinchigu', self.financial_data)
    def new_stocks(self,conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.new_stocks()
        self.base.batchwri(self.df, 'xingushuju', self.financial_data)
    def sh_margins(self,conns,start,end):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.sh_margins(start, end)
        self.base.batchwri(self.df, 'rongzirongquan_sh', self.financial_data)
    def sz_margins(self,conns,start,end):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.sz_margins(start,end)
        self.base.batchwri(self.df, 'rongzirongquan_sz', self.financial_data)

if __name__ == "__main__":

    base = Base()
    financial_data = base.conn('financial_data')
    conns = {'financial_data': financial_data}
    # G=GerDataTouzicankao()
    # #G.profit_data(conns,top=50) 报错
    # G.forecast_data(conns,year=2018,quarter=1)
    # G.xsg_data(conns)
    # G.fund_holdings(conns,year=2018,quarter=1)
    # G.new_stocks(conns)
    # G.sh_margins(conns,start='2018-06-01',end='2018-07-01')
    # G.sz_margins(conns,start='2018-06-01',end='2018-07-01')

    financial_data.close()