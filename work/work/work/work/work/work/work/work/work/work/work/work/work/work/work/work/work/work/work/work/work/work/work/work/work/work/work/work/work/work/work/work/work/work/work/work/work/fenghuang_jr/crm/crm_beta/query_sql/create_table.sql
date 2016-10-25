use tmp;
--×Ê½ð
create table if not exists  crm_desc_json_old(user_id string,md5 string,logger string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
create table if not exists  crm_desc_json_new(user_id string,md5 string,logger string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
create table if not exists  crm_desc_json_diff(user_id string,md5 string,logger string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';

--ºì°ü
create table if not exists  crm_coupon_json_new(user_id string,all_count int,all_amount int,all_use_count int,accept int,accept_user_id string,send int,send_user_id string,register_count int,register_used int,
points_count int,points_used int,rebate_count int,rebate_used int,weekend_count int,weekend_used int,newyear_count int,
newyear_used int,turnplate_count int,turnplate_used int,md5 string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';

create table if not exists  crm_coupon_json_old(user_id string,all_count int,all_amount int,all_use_count int,accept int,accept_user_id string,send int,send_user_id string,register_count int,register_used int,
points_count int,points_used int,rebate_count int,rebate_used int,weekend_count int,weekend_used int,newyear_count int,
newyear_used int,turnplate_count int,turnplate_used int,md5 string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';

create table if not exists  crm_coupon_json_diff(user_id string,logger string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';


create table if not exists  crm_desc_json_new(user_id string,md5 string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
create table if not exists crm_desc_json_old(user_id string,md5 string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';


create table if not exists  crm_used_user_static(user_id string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
create table if not exists  crm_used_user_blank(user_id string,logger string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
create table if not exists  crm_used_user_exist(user_id string,user_id_md5 string,login_name string,name string,id_number string,mobile string,email string,enabled int,enterprise int,channel string,source string,referral_id string,last_logindate string,gender string, age int,age_d int,birth_date int,pri string,city string,login_terminal string,register_date string,total_points int,upgrade_points int,available_points int,level_level string,points_expired_time string,is_permanent string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';

create table if not exists  crm_inc_new_user_all(user_id string,logger string,status int) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';

create table if not exists  coupon_record_crm_invest(invest_id string,entityid string,coupon_id string,couponname string, user_id string,timecreated string,submittime string,AMOUNT double,tag string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';



create table if not exists  crm_activity_contact_awards(user_id string,logger string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
create table if not exists  crm_activity_contact_awards_inc(user_id string,logger string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
