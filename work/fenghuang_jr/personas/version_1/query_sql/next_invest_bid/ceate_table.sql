use crm_v2_test;

create table if not exists  next_invest_bid_label(user_id string,next_rate string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
