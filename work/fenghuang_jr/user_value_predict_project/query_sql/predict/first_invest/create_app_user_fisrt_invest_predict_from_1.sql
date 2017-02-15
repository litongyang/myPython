--drop table app.app_user_predict_first_invest_predict_set_from_1_full;
--create table if not exists app.app_user_predict_first_invest_predict_set_from_1_full
--COMMENT '首投当天预测未来投资的预测集'
--ROW FORMAT DELIMITED
--FIELDS TERMINATED BY '\t'
--LINES TERMINATED BY '\n'
--as
insert overwrite table app.app_user_predict_first_invest_predict_set_from_1
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
c.is_register_ump_good,
c.is_new_user_loan,
c.is_register_recharge_good,
c.is_register_invest_good,
c.is_ump_recharge_good,
c.is_ump_invest_good,
c.is_recharge_invest_good,
b.zodiac,
b.chinese_zodiac,
b.mobile_province,
c.first_invest_date,
c.first_invest_amount,
c.first_invest_loan_months,
c.first_invest_rate,
c.first_recharge_date,
c.first_recharge_amount,
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
            and to_date(first_invest_tm)<edw_day_amount(-1) -- 第一次预测
  		--and to_date(first_invest_tm)=edw_day_amount(-1)
  		and first_invest_tm is not null
  		and first_invest_tm >'2016-12-31'
  ) a
left outer join
  app.app_user_predict_base_feature_full b
on
  a.user_id = b.user_id
left outer join
  app.app_user_predict_invest_base_feature_full c
on
  a.user_id = c.user_id


