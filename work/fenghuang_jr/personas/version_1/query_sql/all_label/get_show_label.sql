use app;
insert overwrite table personas_predict_show_label_full partition (dt='${dt}')
select
	user_id,
	case when age_label = 'young' then '凤金平台的少年'
	     when age_label = 'young_mid' then '凤金平台的青年'
	     when age_label = 'mid' then '凤金平台的中年'
	     when age_label = 'mid_old' then '凤金平台的中老年'
	     when age_label = 'old' then '凤金平台的老年'
	     else null as show_age_label,
	case when invest_var_label = 'low' then '稳定'
	     when invest_var_label = 'mid' then '适中'
	     when invest_var_label = 'high' then '不稳定'
		 else invest_var_label is null end as show_invest_var_label,
	case when next_rate < 500 then '倾向小于5%的利率'
	     when next_rate >=500 and next_rate< 600  then '倾向在5%到6%之间的利率'
	     when next_rate >= 600 and next_rate<700 then '倾向在6%到7%之间的利率'
	     when next_rate >= 600 and next_rate<700 then '倾向7%以上的利率'
		 else null end as show_next_rate,
	case when next_dealine < 60 then '追求2个月以内的期限标的'
	     when next_dealine >=60 and next_rate< 90  then '追求2-3个月期限的标的'
	     when next_dealine >= 90 and next_rate<180 then '追求3-6个月期限的标的'
	     when next_dealine >= 180 and next_rate<270 then '追求6-9个月期限的标的'
	     when next_dealine >= 270 and next_rate<=365 then '追求9-12个月期限的标的'
	     when next_dealine >365  then '追求1年以上期限的标的'
		 else null end as show_next_dealine,
	show_invest_recommend_bid_list,
	invest_recommend_user_list as show_invest_recommend_user_list,
	show_view_recommend_bid_list,
	view_recommend_user_list as show_view_recommend_user_list
from
	personas_predict_label_full
where
    dt = '${dt}'