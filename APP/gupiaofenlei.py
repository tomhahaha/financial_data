import tushare as ts
import pandas as pd
from common.base import Base

class GetDataGupiaofenlei(object):
    def __init__(self):
        self.code = '002337'
        self.df = pd.DataFrame()
    def get_industry_classified(self,conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_industry_classified()
        self.base.batchwri(self.df, 'industry_classified', self.financial_data)
    def get_concept_classified(self,conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_concept_classified()
        self.base.batchwri(self.df, 'concept_classified', self.financial_data)
    def get_area_classified(self,conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_area_classified()
        self.base.batchwri(self.df, 'area_classified', self.financial_data)
    def get_sme_classified(self,conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_sme_classified()
        self.base.batchwri(self.df, 'sme_classified', self.financial_data)
    def get_gem_classified(self,conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_gem_classified()
        self.base.batchwri(self.df, 'gem_classified', self.financial_data)
    def get_st_classified(self,conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_st_classified()
        self.base.batchwri(self.df, 'st_classified', self.financial_data)
    def get_hs300s(self,conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_hs300s()
        self.base.batchwri(self.df, 'hs300s', self.financial_data)
    def get_sz50s(self,conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_sz50s()
        self.base.batchwri(self.df, 'sz50s', self.financial_data)
    def get_zz500s(self,conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_zz500s()
        self.base.batchwri(self.df, 'zz500s', self.financial_data)
    def get_terminated(self,conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_terminated()
        self.base.batchwri(self.df, 'terminated', self.financial_data)
    def get_suspended(self,conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_suspended()
        self.base.batchwri(self.df, 'suspended', self.financial_data)

if __name__ == "__main__":

    base = Base()
    financial_data = base.conn('financial_data')
    conns = {'financial_data': financial_data}
    # G = GetDataGupiaofenlei()
    # G.get_industry_classified(conns)
    ##G.get_concept_classified(conns)
    # G.get_area_classified(conns)
    # G.get_sme_classified(conns)
    # G.get_gem_classified(conns)
    # G.get_st_classified(conns)
    ##G.get_hs300s(conns)  #表空
    ##G.get_sz50s(conns)   #表空
    ##G.get_zz500s(conns)  #表空
    # G.get_terminated(conns)
    # G.get_suspended(conns)

    financial_data.close()