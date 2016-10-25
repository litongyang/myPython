use tmp;

drop table if exists activity_contact_awards;

drop table if exists crm_fund_status_inc;
drop table if exists crm_fund_desc_status_inc;
drop table if exists tb_invest;
drop table if exists tb_user;
drop table if exists tb_coupon_record_crm;
drop table if exists tb_invite_reward_trace;
drop table if exists crm_coupon_desc_new_inc;
drop table if exists crm_inc_new_user_all;

create table crm_inc_new_user_all(user_id string,logger string,status int) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';

drop table if exists crm_desc_json_old;
drop table if exists crm_desc_json_diff;
drop table if exists crm_desc_json_new;
--ALTER TABLE crm_desc_json_new RENAME TO crm_desc_json_old;
drop table if exists crm_fund_status;
drop table if exists crm_fund_desc_status;
--alter table crm_fund_status rename to crm_fund_status_tmp;
--alter table crm_fund_desc_status rename to crm_fund_desc_status_tmp;
--create table crm_desc_json_new(user_id string,md5 string,logger string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
drop table if exists crm_coupon_json_old;
drop table if exists crm_coupon_json_new;
drop table if exists crm_coupon_json_diff;
--alter table crm_conpon_json_new rename to crm_conpon_json_old;
--create table crm_desc_json_new(user_id string,all_amount int,accept int,send int,register_unused int,register_used int,points_unused int,points_used int,rebate_unused int,rebate_used int,weekend_unused int,weekend_used int,newyear_unused int,newyear_used int,turnplate_unused int,turnplate_used int,md5 string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';

drop table if exists crm_used_user_static;
drop table if exists crm_used_user_exist;
drop table if exists crm_used_user_blank;

--fund
create table crm_desc_json_old(user_id string,md5 string,logger string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
create table crm_desc_json_diff(user_id string,md5 string,logger string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
create table crm_desc_json_new(user_id string,md5 string,logger string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';

--ºì°ü
create table crm_coupon_json_new(user_id string,all_count int,all_amount int,all_use_count int,accept int,accept_user_id string,send int,send_user_id string,register_count int,register_used int,
points_count int,points_used int,rebate_count int,rebate_used int,weekend_count int,weekend_used int,newyear_count int,
newyear_used int,turnplate_count int,turnplate_used int,md5 string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';

create table crm_coupon_json_old(user_id string,all_count int,all_amount int,all_use_count int,accept int,accept_user_id string,send int,send_user_id string,register_count int,register_used int,
points_count int,points_used int,rebate_count int,rebate_used int,weekend_count int,weekend_used int,newyear_count int,
newyear_used int,turnplate_count int,turnplate_used int,md5 string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
create table crm_coupon_json_diff(user_id string,logger string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';

--user
create table crm_used_user_static(user_id string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
create table crm_used_user_blank(user_id string,logger string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';

create table crm_used_user_exist(user_id string,user_id_md5 string,login_name string,name string,id_number string,mobile string,email string,enabled int,enterprise int,channel string,source string,referral_id string,last_logindate string,gender string, age int,age_d int,birth_date int,pri string,city string,login_terminal string,register_date string,total_points int,upgrade_points int,available_points int,level_level string,points_expired_time string,is_permanent string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';


