use crm_v2;
insert overwrite local directory '/data/ml/tongyang/data/invest/invest_statistics'
select
  a.user_id,
  toJson(
    'all_count',a.all_count,0,
    'no_debt_swap_cnt',a.no_debt_swap_cnt,0,
    'debt_swap_cnt',a.debt_swap_cnt,0,
    'all_amount',a.all_amount,0,
    'no_debt_swap_amount',a.no_debt_swap_amount,0,
    'debt_swap_amount',a.debt_swap_amount,0,
    'brushstroke_amount_max',a.brushstroke_amount_max,0,
    'brushstroke_amount_min',a.brushstroke_amount_min,0,
    'first_time_invest_amount',a.first_time_invest_amount,0,
    'new_user_amount',a.new_user_amount,0,
    'no_new_user_amount',a.no_new_user_amount,0,
    'first_time',a.first_time,0,
    'first_time_int',int(regexp_replace(a.first_time,'[-]','')),0,
    'lastest_time',a.lastest_time,0,
    'lastest_time_int',int(regexp_replace(a.lastest_time,'[-]','')),0,
    'is_new_user',a.is_new_user,0,
    'new_user_submit_time',a.new_user_submit_time,0,
    'new_user_submit_time_int',int(regexp_replace(a.new_user_submit_time,'[-]','')),0,
    'pc_invest_cnt',a.pc_invest_cnt,0,
    'app_invest_cnt',a.app_invest_cnt,0,
    'h5_invest_cnt',a.h5_invest_cnt,0,
    'other_channel_cnt',a.other_channel_cnt,0,
    'no_debtSwap_newUser_cnt',a.no_debtSwap_newUser_cnt,0,
    'no_debtSwap_newUser_cnt_ratio',a.no_debtSwap_newUser_cnt_ratio,0,
    'no_debt_swap_cnt_ratio',a.no_debt_swap_cnt_ratio,0,
    'debt_swap_cnt_ratio',a.debt_swap_cnt_ratio,0,
    'no_debt_swap_amount_ratio',a.no_debt_swap_amount_ratio,0,
    'debt_swap_amount_ratio',a.debt_swap_amount_ratio,0,
    'new_amount_ratio',a.new_amount_ratio,0,
    'pc_invest_cnt_ratio',a.pc_invest_cnt_ratio,0,
    'app_invest_cnt_ratio',a.app_invest_cnt_ratio,0,
    'h5_invest_cnt_ratio',a.h5_invest_cnt_ratio,0,
    'first_invest_type',a.first_invest_type,0,
    'first_invest_type_int',a.first_invest_type_int,0,
	'first_no_debt_days',0,0,
	'first_debt_days',0,0,
	'first_new_days',a.first_new_days,0,
	'first_no_debt_title',a.first_no_debt_title,0,
	'first_debt_title',a.first_debt_title,0,
	'first_new_title',a.first_new_title,0,
	'last_no_debt_amount',a.last_no_debt_amount,0,
	'last_debt_amount',a.last_debt_amount,0,
	'last_new_amount',a.last_new_amount,0,
    'avg_amount',int(a.all_amount/a.all_count),0) as invest_test
from
(
   select
     t1.*,
     t2.first_time_invest_amount,
     case when t1.new_user_submit_time < t2.first_no_debt_time then 'first_new_type'
          when t2.first_invest_type=1 then 'first_no_debt_type'
          when t2.first_invest_type=2 then 'first_debt_type'
     else 'other_type' end as first_invest_type,
     case when t1.new_user_submit_time < t2.first_no_debt_time then 3
          when t2.first_invest_type=1 then 1
          when t2.first_invest_type=2 then 2
     else 0 end as first_invest_type_int,
     t2.first_no_debt_title as first_no_debt_title,
     t2.first_debt_title as first_debt_title,
     t2.last_no_debt_amount as last_no_debt_amount,
     t2.last_debt_amount as last_debt_amount
   from
     crm_invest_status t1
   left outer join
     crm_invest_one_status t2
   on
     t1.user_id = t2.user_id
)as a;

--create table if not exists crm_desc_json_new(user_id string,md5 string,logger string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';


