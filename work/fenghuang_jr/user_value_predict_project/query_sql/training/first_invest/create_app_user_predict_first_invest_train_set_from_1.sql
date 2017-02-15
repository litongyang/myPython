drop table app.app_user_predict_first_invest_train_set_from_1;
create table if not exists app.app_user_predict_first_invest_train_set_from_1
COMMENT '首投后预测未来投资的训练集'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
as
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
a.y_1_amount,
a.y_3_amount,
a.y_6_amount,
a.y_9_amount,
a.y_12_amount
from
  app.app_user_first_invest_predict_label a
left outer join
  app.app_user_predict_base_feature b
on
  a.user_id = b.user_id
left outer join
  app.app_user_predict_invest_base_feature c
on
  a.user_id = c.user_id

