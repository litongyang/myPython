use crm_v2;

drop table if exists tb_user;
drop table if exists tb_fund_record;
drop table if exists tb_loanrequest_privilege;
drop table if exists tb_loan;
drop table if exists tb_invest;
drop table if exists tb_invite_reward_trace;

drop table if exists crm_invest_status;
drop table if exists crm_invest_desc_status;
drop table if exists crm_invest_one_status;


create table if not exists  crm_invest_status(
user_id string,
all_count int,
no_debt_swap_cnt int,
debt_swap_cnt int,
no_debtSwap_newUser_cnt int,
all_amount double,
no_debt_swap_amount double,
debt_swap_amount double,
brushstroke_amount_max double,
brushstroke_amount_min double,
new_user_amount double,
no_new_user_amount double,
first_time string,
lastest_time string,
is_new_user int,
new_user_submit_time string,
pc_invest_cnt int,
app_invest_cnt int,
h5_invest_cnt int,
other_channel_cnt int,
no_debtSwap_newUser_cnt_ratio double,
no_debt_swap_cnt_ratio double,
debt_swap_cnt_ratio double,
no_debt_swap_amount_ratio double,
debt_swap_amount_ratio double,
new_amount_ratio double,
pc_invest_cnt_ratio double,
app_invest_cnt_ratio double,
h5_invest_cnt_ratio double,
first_new_days int,
first_new_title string,
last_new_amount double
) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
