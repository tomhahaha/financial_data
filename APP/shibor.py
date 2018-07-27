from common.base import Base
import tushare as ts

'''
银行间同业拆放利率:
    Shibor拆放利率  
    银行报价数据
    Shibor均值数据
    贷款基础利率（LPR）
    LPR均值数据
'''
class Shibor(object):
    def __init__(self):
        super(Shibor,self).__init__()


    def __call__(self,conns):
        self.base=Base()
        self.financial_data=conns['financial_data']
        year=self.base.gettoday()[:4]

        #Shibor拆放利率
        shibor_data=ts.shibor_data(year)
        print(shibor_data)
        self.base.batchwri(shibor_data, 'shibor_data', self.financial_data)

        #银行报价数据
        shibor_quote_date=ts.shibor_quote_data(year)
        self.base.batchwri(shibor_quote_date, 'shibor_quote_data', self.financial_data)

        #Shibor均值数据
        shibor_ma_data=ts.shibor_ma_data(year)
        self.base.batchwri(shibor_ma_data, 'shibor_ma_data', self.financial_data)

        #贷款基础利率(LPR)
        lpr_data=ts.lpr_data(year)
        self.base.batchwri(lpr_data, 'lpr_data', self.financial_data)

        #LPR均值数据
        lpr_ma_data=ts.lpr_ma_data(year)
        self.base.batchwri(lpr_ma_data, 'lpr_ma_data', self.financial_data)



if __name__ == "__main__":

    base = Base()
    financial_data = base.conn('financial_data')
    conns = {'financial_data': financial_data}
    shibor = Shibor()
    shibor(conns)


    financial_data.close()