create table if not exists  app.app_user_predict_invest_base_feature_full(
user_id             	string,
is_register_ump_good	string,
is_new_user_loan    	string,
is_register_recharge_good	string,
is_register_invest_good	string,
is_ump_recharge_good	string,
is_ump_invest_good  	string,
is_recharge_invest_good	string,
first_invest_type_name	string,
first_invest_date   	string,
first_invest_amount 	string,
first_invest_loan_months	string,
first_invest_rate   	string,
first_recharge_date 	string,
first_recharge_amount	string,
first_withdraw_date 	string,
first_withdraw_amount	string,
first_repay_date    	string,
first_repay_amount  	string
) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';

