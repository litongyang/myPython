use crm_v2_test;

create table if not exists  user_invest_var_label(user_id string,invest_var double,classified_id int,invest_var_label string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
