from common.base import Base
import tushare as ts

'''
宏观经济数据：
    存款利率
    贷款利率
    存款准备金率
    货币供应量
    货币供应量（年底余额）
    国内生产总值（年度，季度）
    三大需求对GDP贡献、拉动
    三大产业贡献率
    居民消费价格指数
    工业品出厂价格指数
'''
class FinanceMacro(object):
    def __init__(self):
        super(FinanceMacro,self).__init__()

    def __call__(self,conns):
        self.base=Base()
        self.financial_data=conns['financial_data']

        '''存款利率'''
        deposit_rate=ts.get_deposit_rate()
        self.base.batchwri(deposit_rate, 'deposit_rate', self.financial_data)

        '''贷款利率'''
        loan_rate=ts.get_loan_rate()
        self.base.batchwri(loan_rate, 'loan_rate', self.financial_data)

        '''存款准备金率'''
        rrr=ts.get_rrr()
        self.base.batchwri(rrr,'RatioOfDeposit',self.financial_data)

        '''货币供应量'''
        money_supply=ts.get_money_supply()
        self.base.batchwri(money_supply,'money_supply',self.financial_data)

        '''货币供应量（年底余额)'''
        money_supply_bal=ts.get_money_supply_bal()
        self.base.batchwri(money_supply_bal,'money_supply_bal',self.financial_data)

        '''国内生产总值(年度）'''
        gdp_year=ts.get_gdp_year()
        self.base.batchwri(gdp_year,'gdp_year',self.financial_data)

        '''国内生产总值（季度）'''
        gdp_quarter=ts.get_gdp_quarter()
        self.base.batchwri(gdp_quarter, 'gdp_quarter', self.financial_data)

        '''三大需求对GDP贡献'''
        gdp_for=ts.get_gdp_for()
        self.base.batchwri(gdp_for, 'gdp_for', self.financial_data)

        '''三大产业对GDP拉动'''
        gdp_pull=ts.get_gdp_pull()
        self.base.batchwri(gdp_pull, 'gdp_pull', self.financial_data)

        '''三大产业贡献率'''
        gdp_contrib=ts.get_gdp_contrib()
        self.base.batchwri(gdp_contrib, 'gdp_contrib', self.financial_data)

        '''居民消费价格指数'''
        cpi=ts.get_cpi()
        self.base.batchwri(cpi, 'cpi', self.financial_data)

        '''工业品出场价格指数'''
        ppi=ts.get_ppi()
        self.base.batchwri(ppi, 'ppi', self.financial_data)



if __name__ == "__main__":

    base = Base()
    financial_data = base.conn('financial_data')
    conns = {'financial_data': financial_data}
    shibor = FinanceMacro()
    shibor(conns)
    financial_data.close()