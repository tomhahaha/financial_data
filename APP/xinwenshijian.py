from common.base import Base
import tushare as ts

'''
新闻事件数据：
    即时财经新闻
    个股信息地雷
    新浪股吧新闻

'''
class XinwenShijian(object):
    def __init__(self):
        super(XinwenShijian,self).__init__()

    def __call__(self,conns):
        self.base=Base()
        self.financial_data=conns['financial_data']

        '''即时财经新闻'''
        latest_news=ts.get_latest_news()
        self.base.batchwri(latest_news,'latest_news',self.financial_data)

        '''
        名称：个股信息地雷
        功能：获得个股信息地雷数据
        参数
            code：股票代码
            date：信息公布日期
        '''
        notices=ts.get_notices()
        self.base.batchwri(notices,'notices',self.financial_data)

        '''新浪股吧新闻'''
        guba_sina=ts.guba_sina()
        self.base.batchwri(guba_sina,'guba_sina',self.financial_data)



if __name__ == "__main__":

    base = Base()
    financial_data = base.conn('financial_data')
    conns = {'financial_data': financial_data}
    shibor = XinwenShijian()
    shibor(conns)
    financial_data.close()