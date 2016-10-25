use crm_v2;

drop table if exists coupon_record_crm_invest;
drop table if exists tb_coupon_record_crm;
drop table if exists crm_coupon_static_json;
drop table if exists tb_invite_reward_trace;
drop table if exists tb_invest;
--drop table if exists tb_user_fund;

create table if not exists  coupon_record_crm_invest(invest_id string,entityid string,coupon_id string,couponname string, user_id string,timecreated string,submittime string,AMOUNT double,tag string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
create table if not exists  crm_coupon_json_new(user_id string,all_count int,all_amount int,all_use_count int,accept int,accept_user_id string,send int,send_user_id string,register_count int,register_used int,
points_count int,points_used int,rebate_count int,rebate_used int,weekend_count int,weekend_used int,newyear_count int,
newyear_used int,turnplate_count int,turnplate_used int,last_new_coupon_endtime string,md5 string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';