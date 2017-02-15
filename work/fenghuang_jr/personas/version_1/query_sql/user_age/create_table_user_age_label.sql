use app;
drop table if exists personas_user_age_label_full;
CREATE EXTERNAL TABLE personas_user_age_label_full(
 user_id string COMMENT '用户id',
 age int  COMMENT '用户年龄',
 classified_id int COMMENT '用户年龄类别id',
 age_label string COMMENT '用户年龄标签'
 )
COMMENT '用户画像用户年龄分类'
PARTITIONED BY (dt string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n';
-- stored as parquet;