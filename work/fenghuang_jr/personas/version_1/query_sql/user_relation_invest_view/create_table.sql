use app;

drop table if exists personas_user_relation_invest_view_bid_label_full;
drop table if exists personas_user_relation_invest_view_user_label_full;

CREATE EXTERNAL TABLE personas_user_relation_invest_view_bid_label_full(
 user_id string COMMENT '用户id',
 user_type string COMMENT '用户类型',
 recommend_bid string  COMMENT '推荐标的类型',
 recommend_bid_score string  COMMENT '推荐相关系数'
 )
COMMENT '用户画像基于投资行为的用户产品类型推荐'
PARTITIONED BY (dt string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n';


CREATE EXTERNAL TABLE personas_user_relation_invest_view_user_label_full(
 user_id string COMMENT '用户id',
 user_type string COMMENT '用户类型',
 recommend_user string  COMMENT '推荐相关用户',
 recommend_user_score string  COMMENT '推荐相关系数'
 )
COMMENT '用户画像基于投资行为的用户相关推荐'
PARTITIONED BY (dt string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n';