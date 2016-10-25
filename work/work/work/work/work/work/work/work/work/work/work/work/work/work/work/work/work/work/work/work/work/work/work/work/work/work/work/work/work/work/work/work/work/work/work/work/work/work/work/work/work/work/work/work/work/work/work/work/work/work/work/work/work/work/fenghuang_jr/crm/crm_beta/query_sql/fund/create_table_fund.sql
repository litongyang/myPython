use crm_v2;
create table if not exists  crm_fund_statistics(user_id string,balance_amount double,total_amount double, available_amount double) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
create table if not exists  crm_fund_logger(user_id string,type string, type_name string, amount double, date string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
