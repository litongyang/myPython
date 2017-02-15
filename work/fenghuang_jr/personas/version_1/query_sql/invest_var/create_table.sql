use app;
drop table if exists personas_user_invest_var_label_full;
CREATE EXTERNAL TABLE personas_user_invest_var_label_full(
 user_id string COMMENT '用户id',
 invest_var double  COMMENT '用户历史投资利率方差',
 classified_id int COMMENT '用户投资利率稳定性分类id',
 invest_var_label string COMMENT '用户投资利率稳定性分类标签'
 )
COMMENT '用户画像用户投资稳定性预测'
PARTITIONED BY (dt string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n';