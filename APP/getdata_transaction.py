import tushare as ts
import pandas as pd
from common.base import Base

class GetDataTransaction(object):
    def __init__(self):
        self.code = '002337'
        self.start = '2018-06-01'
        self.end = '2018-07-25'
        self.df=pd.DataFrame()
    def __call__(self, conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_stock_basics()
        self.base.batchwri(self.df, 'stock_basics1', self.financial_data)
    #历史行情:获取个股历史交易数据（包括均线数据），可以通过参数设置获取日k线、周k线、月k线，以及5分钟、15分钟、30分钟和60分钟k线数据。
    #本接口只能获取近3年的日线数据，适合搭配均线数据进行选股和分析，如果需要全部历史数据，请调用下一个接口get_h_data()
    def get_hist_data(self, conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_hist_data(self.code)
        self.base.batchwri(self.df, 'history_data', self.financial_data)
    #复权数据:获取历史复权数据，分为前复权和后复权数据，接口提供股票上市以来所有历史数据，默认为前复权。如果不设定开始和结束日期，
    #则返回近一年的复权数据，从性能上考虑，推荐设定开始日期和结束日期，而且最好不要超过三年以上，获取全部历史数据，请分年段分步获取。
    def get_stock_basics(self, conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        #self.df = ts.get_stock_basics(self.code)
        # ts.get_h_data('002337')  # 前复权
        # ts.get_h_data('002337', autype='hfq')  # 后复权
        # ts.get_h_data('002337', autype=None)  # 不复权
        self.df = ts.get_h_data(self.code,self.start,self.end)  # 两个日期之间的前复权数据
        #
        # ts.get_h_data('399106', index=True)  # 深圳综合指数
        self.base.batchwri(self.df, 'fuquan_data', self.financial_data)
    #实时行情::一次性获取当前交易所有股票的行情数据（如果是节假日，即为上一交易日，结果显示速度取决于网速）
    def get_today_all(self, conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        #self.df=ts.get_hist_data(self.code,self.start,self.end)
        #self.df=ts.get_stock_basics(self.code,self.start,self.end)
        self.df=ts.get_today_all()
        #self.df=ts.get_tick_data(self.code,date='2017-01-09')
        #self.df=ts.get_realtime_quotes(self.code)
        #self.df=ts.get_today_ticks(self.code)
        #self.df=ts.get_index()
        #self.df=ts.get_sina_dd(self.code,date='2014-01-09')
        self.base.batchwri(self.df, 'shishihangqing', self.financial_data)
    #历史分笔:获取个股以往交易历史的分笔数据明细，通过分析分笔数据，可以大致判断资金的进出情况。
    def get_tick_data(self, conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_tick_data(self.code, date='2018-06-01')
        self.base.batchwri(self.df, 'lishifenbi', self.financial_data)
    #实时分笔:获取实时分笔数据，可以实时取得股票当前报价和成交信息
    def get_realtime_quotes(self, conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_realtime_quotes(self.code)
        #ts.get_realtime_quotes(['600848','000980','000981']) 请求多个股票
        self.base.batchwri(self.df, 'shishifenbi', self.financial_data)
    #当日历史分笔:获取当前交易日（交易进行中使用）已经产生的分笔明细数据。
    def get_today_ticks(self, conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_today_ticks(self.code)
        self.base.batchwri(self.df, 'dangrilishifenbi', self.financial_data)
    #大盘指数行情列表:获取大盘指数实时行情列表，以表格的形式展示大盘指数实时行情。
    def get_index(self, conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_index()
        self.base.batchwri(self.df, 'dapanzhishu', self.financial_data)
    #大单交易数据:获取大单交易数据，默认为大于等于400手，数据来源于新浪财经。
    def get_sina_dd(self, conns):
        self.base = Base()
        self.financial_data = conns['financial_data']
        self.df = ts.get_sina_dd(self.code, date='2018-07-25')#默认400手
        # self.df = ts.get_sina_dd('600848', date='2015-12-24', vol=500)  #指定大于等于500手的数据
        self.base.batchwri(self.df, 'dadanjiaoyi', self.financial_data)

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
    # G = GetDataTransaction()
    # G.get_hist_data(conns)
    # G.get_stock_basics(conns)
    # G.get_today_all(conns)
    # #G.get_tick_data(conns) #无数据
    # G.get_realtime_quotes(conns)
    # G.get_today_ticks(conns)
    # G.get_index(conns)
    # #G.get_sina_dd(conns) 不一定有数据


    # G=GerDataTouzicankao()
    # #G.profit_data(conns,top=50) 报错
    # G.forecast_data(conns,year=2018,quarter=1)
    # G.xsg_data(conns)
    # G.fund_holdings(conns,year=2018,quarter=1)
    # G.new_stocks(conns)
    # G.sh_margins(conns,start='2018-06-01',end='2018-07-01')
    # G.sz_margins(conns,start='2018-06-01',end='2018-07-01')

    # G = GetDataGupiaofenlei()
    #G.get_industry_classified(conns)
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

    G = GetDataJibenmian()
    y=2018
    q=1
    G.get_stock_basics(conns)
    G.get_report_data(conns,y,q)
    G.get_profit_data(conns,y,q)
    G.get_operation_data(conns,y,q)
    G.get_growth_data(conns,y,q)
    G.get_debtpaying_data(conns,y,q)
    G.get_cashflow_data(conns,y,q)

    financial_data.close()