use crm_v2;

drop table if exists tb_fund_record;
drop table if exists tb_invest_repayment;
drop table if exists tb_invest;
drop table if exists tb_user_fund;

create table if not exists  crm_fund_statistics(user_id string,balance_amount double,total_amount double,available_amount double, first_deposit_date string,first_withdraw_date string,last_withdraw_date string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
create table if not exists  crm_fund_logger(user_id string,type string,type_name string,amount double, date string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
