# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import MySQLdb


class CreateTable:
    def __init__(self):
        self.db_name = 'test'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码
        self.file_name = 'baidu_licai'
        self.conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name, port=self.db_port)
        self.cur = self.conn.cursor()

    def create_table(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute(
                    "CREATE TABLE IF NOT EXISTS %s "
                    "("
                    "id varchar(20) comment '产品id',"
                    "title varchar(100) comment '产品名称',"
                    "titleAll varchar(100) comment '产品全称',"
                    "productTypeLabel varchar(8) comment '产品类型',"
                    "expectedProfitRate decimal(10,2) comment '到期利率',"
                    "investCycle varchar(20) comment '投资周期',"
                    "investField varchar(20) comment '投资领域',"
                    "riskScore int comment '百度风险分数',"
                    "risk  varchar(100) comment '风险说明',"
                    "idea  varchar(100) comment '产品细化说明',"
                    "lowestAmount varchar(20) comment '最低投资金额',"
                    "profitType int comment '收益类型:1-固定收益 0-浮动收益',"
                    "profitDesc_value varchar(200) comment '收益说明',"
                    "inShop varchar(20) comment '',"
                    "earlyBack int comment '提前还款月数',"
                    "earlyTransfer int comment '提前转让月数',"
                    # "extraFields_tips varchar(1000) comment '投资转让说明',"
                    "investFieldDesc varchar(1000) comment '投资风险说明',"
                    "channelNameShort varchar(100) comment '被投资方简称',"
                    "channelName varchar(100) comment '被投资方全称',"
                    "channelUrl varchar(5000) comment '产品渠道网址',"
                    "url varchar(5000) comment '百度抓取产品所属公司主页',"
                    "rawUrl varchar(5000) comment '百度抓取产品所属公司主页',"
                    "tag varchar(20) comment '第三方评级',"
                    "haomai varchar(20) comment '',"
                    "breakEven varchar(20) comment '是否盈亏平衡',"
                    "timeStamp varchar(50) comment '时间戳',"
                    "PRIMARY KEY (`id`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                    % self.file_name)
        except Exception, e:
            print Exception, e

if __name__ == '__main__':
    test = CreateTable()
    test.create_table()
