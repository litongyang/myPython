use crm_v2;
drop table if exists crm_ptsts_points_transaction;
drop table if exists crm_contacts_cstm;
create table if not exists  crm_points_statistics(user_id string,total_points int,available_points int,consum_points_cnt int, consum_points_max int,consum_points_min int,consum_points_sum int) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
