use crm_v2;

drop table if exists activity_contact_awards_0;
drop table if exists activity_contact_awards_1;
drop table if exists activity_contact_awards_2;
drop table if exists activity_contact_awards_3;
drop table if exists activity_contact_awards_4;
drop table if exists activity_contact_awards_5;
drop table if exists activity_contact_awards_6;
drop table if exists activity_contact_awards_7;
drop table if exists activity_contact_awards_8;
drop table if exists activity_contact_awards_9;
drop table if exists activity_contact_awards_10;
drop table if exists activity_contact_awards_11;
drop table if exists activity_contact_awards_12;
drop table if exists activity_contact_awards_13;
drop table if exists activity_contact_awards_14;
drop table if exists activity_contact_awards_15;

create table if not exists  activity_contact_awards(id string,contact_id string,activity_id string,activity_type int, activity_name string,award_type string,type_id string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
