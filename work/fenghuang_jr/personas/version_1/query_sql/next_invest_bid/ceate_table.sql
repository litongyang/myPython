use app;
drop table if exists personas_next_invest_bid_label_full;
drop table if exists personas_next_invest_bid_deadline_label_full;

CREATE EXTERNAL TABLE personas_next_invest_bid_label_full(
 user_id string COMMENT '用户id',
 next_rate string  COMMENT '下一次投资利率'
 )
COMMENT '用户画像预测用户下一次投资标的利率'
PARTITIONED BY (dt string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n';


CREATE EXTERNAL TABLE personas_next_invest_bid_deadline_label_full(
 user_id string COMMENT '用户id',
 next_deadline string  COMMENT '下一次投资期限'
 )
COMMENT '用户画像预测用户下一次投资标的期限'
PARTITIONED BY (dt string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n';