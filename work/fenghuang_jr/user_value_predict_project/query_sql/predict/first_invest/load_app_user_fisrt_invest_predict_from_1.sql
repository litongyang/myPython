-- 下载首次当天投资的用户预测其未来两个月的投资的训练集表
set hive.exec.compress.output=false;
insert overwrite local directory '/root/user_value_predict/predict/data/first_invest/first_invest_1' row format delimited fields terminated by '\t'

select *
from
    app.app_user_predict_first_invest_predict_set_from_1
where
    dt=edw_day_amount(-1)

