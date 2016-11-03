use crm_v2_test;

create table if not exists  user_relation_invest_view_label(user_id string,recommend_bid string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
