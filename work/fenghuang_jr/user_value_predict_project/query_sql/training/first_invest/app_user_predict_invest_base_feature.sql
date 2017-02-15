insert overwrite table app.app_user_predict_invest_base_feature_full
select
a.user_id,
a.is_register_ump_good,
a.is_new_user_loan,
a.is_register_recharge_good,
a.is_register_invest_good,
a.is_ump_recharge_good,
a.is_ump_invest_good,
a.is_recharge_invest_good,
c.first_invest_type_name, -- 首次投资产品名称
cast(datediff(c.first_invest_tm,aa.ump_account_tm) as string) as first_invest_date,--首次投资距托管
c.first_invest_amount ,--首次投资金额
c.first_invest_loan_months,--首次投资标的期限
c.first_invest_rate, -- 首次投资标的利率
cast(datediff(b.first_recharge_date,aa.ump_account_tm) as string) as first_recharge_date, -- 首次充值距注册
b.first_recharge_amount, -- 首次充值金额
cast(datediff(b.first_withdraw_date,aa.ump_account_tm) as string ) as first_withdraw_date, -- 首次提现日期
b.first_withdraw_amount,-- 首次提现金额
cast(datediff(b.first_repay_date,aa.ump_account_tm) as string ) as first_repay_date,--首次回款距托管
b.first_repay_amount --首次回款金额
from
(
select user_id, ump_account_tm from dim.dim_user_base where ump_account_tm is not null
) aa
left join
(
select
user_id,
is_register_ump_good,
is_new_user_loan,
is_register_recharge_good,
is_register_invest_good,
is_ump_recharge_good,
is_ump_invest_good,
is_recharge_invest_good
from
app.app_personas_user_label_full
where dt=edw_day_amount(-1)
) a
on aa.user_id=a.user_id
left join
(
select
user_id,
first_recharge_amount,
first_recharge_date,
first_withdraw_amount,
first_withdraw_date,
first_repay_amount,
first_repay_date
from
app.app_personas_user_account_full
where dt=edw_day_amount(-1)
) b
on aa.user_id=b.user_id
left join
(
select
user_id,
first_invest_tm,
first_invest_amount,
first_invest_loan_months,
first_invest_type_name,
first_invest_rate
from
app.app_personas_user_invest_full
where dt=edw_day_amount(-1)
) c
on aa.user_id=c.user_id

