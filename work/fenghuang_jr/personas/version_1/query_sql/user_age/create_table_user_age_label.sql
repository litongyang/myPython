use crm_v2_test;

create table if not exists  user_age_label(user_id string,age int,classified_id int,age_label string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';