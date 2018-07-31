#-*- coding: utf-8 -*-

from common.base_test import Base
import threading
import tushare as ts
from time import ctime
import pandas as pd


class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)


def get_today_close(date, code_list):

    fin = []
    #print(code_list)
    # start = ctime()
    # print('strat: '+start)

    for i in range(len(code_list)):
    # for i in range(0,10):
        code_tj = code_list['code'][i]
        #print(code_tj)
        df = ts.get_k_data(code_tj, start=date, end=date, autype=None).reset_index(drop=True)
        print(df)
        if df.empty:
            continue
        code = df['code'][0]
        #print(code)
        close = df['close'][0]
        #print(close)
        fin.append([code, close])

    res = pd.DataFrame(fin, columns=['code','close'])
    # print('End: '+ ctime() + ', start at' + start)
    return res

def main():
    base = Base()
    financial_data = base.conn('financial_data')
    conns = {'financial_data': financial_data}
    cnx = conns['financial_data']
    code_list = cnx.getdata('stock_code_name',['code'])[0:1000]
    k = int(len(code_list)/4)
    code_t = [code_list[0:k].reset_index(drop=True),
              code_list[k:2*k].reset_index(drop=True),
              code_list[2*k:3*k].reset_index(drop=True),
              code_list[3*k:].reset_index(drop=True)]

    start = ctime()
    print('starting at: ',start)
    threads = []

    for i in range(4):
        t = threading.Thread(target=ThreadFunc(get_today_close,
                                               ('2018-07-27', code_t[i]),
                                               get_today_close.__name__))
        threads.append(t)

    for i in range(4):
        threads[i].start()

    for i in range(4):
        threads[i].join()

    print('all DONE at: ',ctime(),'  start at: ',start)

if __name__ == "__main__":
    main()



