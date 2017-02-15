--drop table app.app_user_predict_first_invest_predict_set_from_60_ful;
--create table if not exists app.app_user_predict_first_invest_predict_set_from_60_ful
--COMMENT '首投60天后预测未来投资的预测集'
--ROW FORMAT DELIMITED
--FIELDS TERMINATED BY '\t'
--LINES TERMINATED BY '\n'
--as
insert overwrite table app.app_user_predict_first_invest_predict_set_from_60
select
	a.user_id,
    b.age_generation,
    b.gender_code,
    b.telecom_operators,
    b.is_member,
    b.lv_name,
    b.has_bind_bank_card,
    b.card_value,
    b.mobile_value,
    b.mobile_phone_value,
    d.is_register_ump_good,
    d.is_new_user_loan,
    d.is_register_recharge_good,
    d.is_register_invest_good,
    d.is_ump_recharge_good,
    d.is_ump_invest_good,
    d.is_recharge_invest_good,
    b.zodiac,
    b.chinese_zodiac,
    b.mobile_province,
    d.first_invest_date,
    d.first_invest_amount,
    d.first_invest_loan_months,
    d.first_invest_rate,
    d.first_recharge_date,
    d.first_recharge_amount,
	c.invest_cnt_7,
	c.invest_sum_7,
	c.invest_max_7,
	c.invest_min_7,
	c.invest_avg_7,
	c.rate_max_7,
	c.rate_min_7,
	c.rate_avg_7,
	c.days_max_7,
	c.days_min_7,
	c.days_avg_7,
	c.invest_cnt_14,
	c.invest_sum_14,
	c.invest_max_14,
	c.invest_min_14,
	c.invest_avg_14,
	c.rate_max_14,
	c.rate_min_14,
	c.rate_avg_14,
	c.days_max_14,
	c.days_min_14,
	c.days_avg_14,
	c.invest_cnt_30,
	c.invest_sum_30,
	c.invest_max_30,
	c.invest_min_30,
	c.invest_avg_30,
	c.rate_max_30,
	c.rate_min_30,
	c.rate_avg_30,
	c.days_max_30,
	c.days_min_30,
	c.days_avg_30,
	c.invest_cnt_60,
	c.invest_sum_60,
	c.invest_max_60,
	c.invest_min_60,
	c.invest_avg_60,
	c.rate_max_60,
	c.rate_min_60,
	c.rate_avg_60,
	c.days_max_60,
	c.days_min_60,
	c.days_avg_60,
	c.deposit_cnt_7,
	c.deposit_sum_7,
	c.deposit_max_7,
	c.deposit_min_7,
	c.deposit_avg_7,
	c.deposit_cnt_14,
	c.deposit_sum_14,
	c.deposit_max_14,
	c.deposit_min_14,
	c.deposit_avg_14,
	c.deposit_cnt_30,
	c.deposit_sum_30,
	c.deposit_max_30,
	c.deposit_min_30,
	c.deposit_avg_30,
	c.deposit_cnt_60,
	c.deposit_sum_60,
	c.deposit_max_60,
	c.deposit_min_60,
	c.deposit_avg_60,
	c.withdraw_cnt_7,
	c.withdraw_sum_7,
	c.withdraw_max_7,
	c.withdraw_min_7,
	c.withdraw_avg_7,
	c.withdraw_cnt_14,
	c.withdraw_sum_14,
	c.withdraw_max_14,
	c.withdraw_min_14,
	c.withdraw_avg_14,
	c.withdraw_cnt_30,
	c.withdraw_sum_30,
	c.withdraw_max_30,
	c.withdraw_min_30,
	c.withdraw_avg_30,
	c.withdraw_cnt_60,
	c.withdraw_sum_60,
	c.withdraw_max_60,
	c.withdraw_min_60,
	c.withdraw_avg_60,
    a.dt
from
  (
  	select
  		user_id,
  		first_invest_tm,
		dt
  	from
  		dws.dws_user_base_full
  	where
  		dt=edw_day_amount(-1)
  		-- and to_date(first_invest_tm)<edw_day_amount(-60) -- 第一次预测
  		and to_date(first_invest_tm)=edw_day_amount(-61)
  		and first_invest_tm is not null
  		and first_invest_tm >'2016-12-31'
  ) a
left outer join
  app.app_user_predict_base_feature_full b
on
  a.user_id = b.user_id
left outer join
  app_user_predict_first_invest_account_feature_2017_full c
on
  a.user_id = c.user_id
left outer join
  app.app_user_predict_invest_base_feature_full d
on
  a.user_id = d.user_id
