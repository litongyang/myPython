use tmp;

--因为活动和之前的不是一个版本，所以不支持md5对应的全增量统一方法
insert overwrite table crm_activity_contact_awards
select
 contact_id as user_id,
 toJson('count',count(*),0,'all_amount',sum(amount),0,'logger',json_list('activity_name',activity_name),1)
from
 activity_contact_awards
where
 is_joined='1'
 and award_type in('HONGBAO','CASHBACK')
group by
 contact_id;





--获取存在数据的用户

insert overwrite table crm_used_user_exist select a.* from common.user_static as a left outer join crm_desc_json_diff as b on a.user_id = b.user_id left outer join crm_coupon_json_diff as c on a.user_id = c.user_id left outer join crm_activity_contact_awards as d on a.user_id=d.user_id where b.user_id is not null or c.user_id is not null or d.user_id is not null;


--生成结果集
--insert overwrite table crm_end
insert overwrite local directory '/data/apps/tongyang/fund_test/data'
select
 toJson(
 'user_id',c.user_id,0,
 'login_name',c.login_name,0,
 'name',case when c.name is null then null else crm_aes_encode(c.name) end,0,
 'mobile',case when c.mobile is null then null else crm_aes_encode(user_decrypt(c.mobile)) end,0,
 'email',case when c.email is null then null else crm_aes_encode(c.email) end,0,
 'enabled',c.enabled,0,
 'enterprise',c.enterprise,0,
 'source',c.source,0,
 'referral_id',c.referral_id,0,
 'last_logindate',c.last_logindate,0,
 'last_logindate_t',substr(c.last_logindate,0,10),0,
 'age',c.age_d,0,
 'gender',c.gender,0,
 'province',c.pri,0,
 'city',c.city,0,
 'birth_date',c.birth_date,0,
 'register_date',c.register_date,0,
 'register_date_t',substr(c.register_date,0,10),0,
 'total_points',c.total_points,0,
 'upgrade_points',c.upgrade_points,0,
 'available_points',c.available_points,0,
 'level_level',c.level_level,0,
 'points_expired_time',c.points_expired_time,0,
 'is_permanent',c.is_permanent,0,'fund',
  toJson(
    'all_count',a.all_count,0,
    'first_time',a.first_time,0,
    'first_time_int',int(regexp_replace(a.first_time,'[-]','')),0,
    'lastest_time',a.lastest_time,0,
    'lastest_time_int',int(regexp_replace(a.lastest_time,'[-]','')),0,
    'brushstroke_max',a.brushstroke_max,0,
    'brushstroke_min',a.brushstroke_min,0,
    'all_amount',a.all_amount,0,
    'avg_amount',int(a.all_amount/a.all_count),'0',
    'is_new_user',a.is_new_user,0,
    'new_user_submit_time',a.new_user_submit_time,0,
    'new_user_submit_time_int',int(regexp_replace(a.new_user_submit_time,'[-]','')),0,
    'new_user_amount',a.new_user_amount,0,
    'other_amount',a.other_amount,0,
    'logger',b.logger,1),1,
  'coupon',d.logger,1,
  'activity',e.logger,1) as crm_of_es_json
from
 crm_used_user_exist as c
left outer join
 crm_desc_json_new as b
on
 c.user_id = b.user_id
left outer join
 crm_fund_status as a
on
 c.user_id = a.user_id
left outer join
 crm_coupon_json_diff as d
on
 c.user_id = d.user_id
left outer join
 crm_activity_contact_awards as e
on
 c.user_id = e.user_id;

--获取新增并且为空数据
insert overwrite table crm_used_user_blank select  u.user_id, toJson('user_id',u.user_id,0,'login_name',u.login_name,0,'name',case when u.name is null then null else crm_aes_encode(u.name) end,0,'mobile',case when u.mobile is null then null else crm_aes_encode(user_decrypt(u.mobile)) end,0,'email',case when u.email is null then null else crm_aes_encode(u.email) end,0,'enabled',u.enabled,0,'enterprise',u.enterprise,0,'source',u.source,0,'referral_id',u.referral_id,0,'last_logindate',u.last_logindate,0,'last_logindate_t',substr(u.last_logindate,0,10),0,'age',u.age_d,0,'gender',u.gender,0,'province',u.pri,0,'city',u.city,0,'birth_date',u.birth_date,0,'register_date',u.register_date,0,'register_date_t',substr(u.register_date,0,10),0,'total_points',u.total_points,0,'upgrade_points',u.upgrade_points,0,'available_points',u.available_points,0,'level_level',u.level_level,0,'points_expired_time',u.points_expired_time,0,'is_permanent',u.is_permanent,0) from common.user_static as u left outer join crm_used_user_static as a on a.user_id = u.user_id left outer join crm_used_user_exist as b on u.user_id = b.user_id  where a.user_id is null and b.user_id is null;
--新的空用户写入本地
insert overwrite local directory '/data/apps/tongyang/fund_test/data_user' select logger from crm_used_user_blank;
--和并使用过的 user_id
--insert overwrite table crm_used_user_static select user_id from crm_used_user_static union all select user_id from crm_used_user_new;
--static表会在初始化和后再一次执行空数据 目前不改
insert into table crm_used_user_static select user_id from crm_used_user_blank union all select user_id from crm_used_user_exist;


--修改表内容:
--drop table if exists crm_desc_json_old;
--ALTER TABLE crm_desc_json_new RENAME TO crm_desc_json_old;
--drop table if exists crm_fund_status_tmp;
--drop table if exists crm_fund_desc_status_tmp;
--alter table crm_fund_status rename to crm_fund_status_tmp;
--alter table crm_fund_desc_status rename to crm_fund_desc_status_tmp;
--create table crm_desc_json_new(user_id string,md5 string,logger string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
--drop table if exists crm_coupon_json_old;
--alter table crm_coupon_json_new rename to crm_coupon_json_old;
--create table crm_coupon_json_new(user_id string,all_count int,all_amount int,all_use_count int,accept int,send int,register_unused int,register_used int,points_unused int,points_used int,rebate_unused int,rebate_used int,weekend_unused int,weekend_used int,newyear_unused int,newyear_used int,turnplate_unused int,turnplate_used int,md5 string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';


--修改为当前执行error.sql脚本即可
drop table if exists crm_fund_status_inc;
drop table if exists tb_invite_reward_trace;
drop table if exists crm_coupon_desc_new_inc;
drop table if exists crm_inc_new_user_all;
drop table if exists tb_invest;

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

--红包
create table crm_coupon_json_new(user_id string,all_count int,all_amount int,all_use_count int,accept int,send int,register_count int,register_used int,
points_count int,points_used int,rebate_count int,rebate_used int,weekend_count int,weekend_used int,newyear_count int,
newyear_used int,turnplate_count int,turnplate_used int,md5 string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
create table crm_coupon_json_old(user_id string,all_count int,all_amount int,all_use_count int,accept int,send int,register_count int,register_used int,
points_count int,points_used int,rebate_count int,rebate_used int,weekend_count int,weekend_used int,newyear_count int,
newyear_used int,turnplate_count int,turnplate_used int,md5 string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
create table crm_coupon_json_diff(user_id string,logger string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';

--user
create table crm_used_user_static(user_id string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
create table crm_used_user_blank(user_id string,logger string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
create table crm_used_user_exist(user_id string,age int,gender string,pri string,city string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';

