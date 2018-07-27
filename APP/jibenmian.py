import tushare as ts
import pandas as pd
from common.base import Base

class GetDataJibenmian(object):
    def __init__(self):
        self.code = '002337'
        self.df = pd.DataFrame()
    def get_stock_basics(self,conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_stock_basics()
        self.base.batchwri(self.df, 'stock_basics', self.financial_data)
    def get_report_data(self,conns,year,quarter):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_report_data(year,quarter)
        self.base.batchwri(self.df, 'report_data', self.financial_data)
    def get_profit_data(self,conns,year,quarter):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_profit_data(year,quarter)
        self.base.batchwri(self.df, 'profit_data', self.financial_data)
    def get_operation_data(self,conns,year,quarter):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_operation_data(year,quarter)
        self.base.batchwri(self.df, 'operation_data', self.financial_data)
    def get_growth_data(self,conns,year,quarter):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_growth_data(year,quarter)
        self.base.batchwri(self.df, 'growth_data', self.financial_data)
    def get_debtpaying_data(self,conns,year,quarter):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_debtpaying_data(year,quarter)
        self.base.batchwri(self.df, 'debtpaying_data', self.financial_data)
    def get_cashflow_data(self,conns,year,quarter):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_cashflow_data(year,quarter)
        self.base.batchwri(self.df, 'cashflow_data', self.financial_data)

if __name__ == "__main__":
    base = Base()
    financial_data = base.conn('financial_data')
    conns = {'financial_data': financial_data}
    G = GetDataJibenmian()
    y=2018
    q=1
    # G.get_stock_basics(conns)
    # G.get_report_data(conns,y,q)
    # G.get_profit_data(conns,y,q)
    # G.get_operation_data(conns,y,q)
    # G.get_growth_data(conns,y,q)
    # G.get_debtpaying_data(conns,y,q)
    # G.get_cashflow_data(conns,y,q)

    financial_data.close()