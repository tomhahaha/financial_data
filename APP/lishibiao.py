import tushare as ts
import pandas as pd
from common.base import Base
from APP.getdata_transaction import GetDataTransaction

def dapanlishi(conns):
    base = Base()
    financial_data = conns['financial_data']
    df = ts.get_index()
    for stock in df['code']:
        df1=ts.get_k_data(stock,index=True,start='2018-07-01', end='2018-07-30')
        df1 = df1.sort_values(['date'], ascending=[0]).reset_index(drop=True)  # 排序，0倒序，1正序 重置索引
        df2 = ts.get_h_data(stock, index=True, start='2018-07-01', end='2018-07-30')
        noise_df = pd.DataFrame(df2, columns=['amount']).reset_index(drop=True)
        df3 =pd.merge(df1,noise_df, left_index=True, right_index=True)
        base.batchwri(df3, 'dapanzhishulishi', financial_data)

def stocklishi(conns):
    base = Base()
    financial_data = conns['financial_data']
    df = ts.get_today_all()['code']
    # df = pd.DataFrame(df, columns=['code','name','open','high','low','volume','amount'])
    for stock in df:
        df1 = pd.DataFrame(ts.get_hist_data(stock) ,columns=['date','code','name','open','high','low','volume'])
        df2 = ts.get_h_data(stock,start='2018-07-01', end='2018-07-30')
        df3 = ts.get_h_data(stock,start='2018-07-01', end='2018-07-30',autype='hfq')
        df2 = pd.merge(df1, df2, on='date')
        df3 = pd.merge(df2, df3, on='date')
        base.batchwri(df3, 'stocklishi', financial_data)




if __name__ == "__main__":

    base = Base()
    financial_data = base.conn('financial_data')
    conns = {'financial_data': financial_data}
    # dapanlishi(conns)
    stocklishi(conns)

    financial_data.close()