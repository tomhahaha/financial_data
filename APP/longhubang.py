from common.base import Base
import tushare as ts

'''
龙虎榜数据：
    每日龙虎榜列表
    个股上榜统计
    营业部上榜统计
    龙虎榜机构席位追踪
    龙虎榜机构席位成交明细
'''
class LonghuBang(object):
    def __init__(self):
        super(LonghuBang,self).__init__()

    def __call__(self,conns):
        self.base=Base()
        self.financial_data=conns['financial_data']
        date=self.base.gettoday().replace('/','-')
        # print(date)

        # '''每日龙虎榜列表'''
        # for day in self.base.datelist('20180702','20180705'):
        #     day=day.replace('/','-')
        #     top_list=ts.top_list(day)
        #     self.base.batchwri(top_list,'top_list',self.financial_data)

        # '''
        # 名称：个股上榜统计
        # 参数说明：
        #         days：统计周期5、10、30和60日，默认为5日
        #         retry_count：当网络异常后重试次数，默认为3
        #         pause:重试时停顿秒数，默认为0'''
        # cap_tops=ts.cap_tops()
        # self.base.batchwri(cap_tops,'cap_tops',self.financial_data)

        # '''
        # 名称：营业部上榜统计
        # 参数说明：
        #         days：统计周期5、10、30和60日，默认为5日
        #         retry_count：当网络异常后重试次数，默认为3
        #         pause:重试时停顿秒数，默认为0'''
        # broker_tops=ts.broker_tops()
        # self.base.batchwri(broker_tops,'broker_tops',self.financial_data)

        # '''
        # 名称：机构席位追踪
        # 参数说明：
        #         days：统计周期5、10、30和60日，默认为5日
        #         retry_count：当网络异常后重试次数，默认为3
        #         pause:重试时停顿秒数，默认为0
        # '''
        # inst_tops=ts.inst_tops()
        # self.base.batchwri(inst_tops,'inst_tops',self.financial_data)

        '''机构成交明细'''
        inst_detail=ts.inst_detail()
        self.base.batchwri(inst_detail,'inst_detail',self.financial_data)

if __name__ == "__main__":

    base = Base()
    financial_data = base.conn('financial_data')
    conns = {'financial_data': financial_data}
    shibor = LonghuBang()
    shibor(conns)
    financial_data.close()