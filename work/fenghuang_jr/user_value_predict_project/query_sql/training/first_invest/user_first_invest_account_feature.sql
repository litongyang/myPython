use app;
insert overwrite table app.app_user_predict_first_invest_account_feature
select
	t.user_id,
	t1.invest_cnt_7,
	t1.invest_sum_7,
	t1.invest_max_7,
	t1.invest_min_7,
	t1.invest_avg_7,
	t1.rate_max_7,
	t1.rate_min_7,
	t1.rate_avg_7,
	t1.days_max_7,
	t1.days_min_7,
	t1.days_avg_7,
	t2.invest_cnt_14,
	t2.invest_sum_14,
	t2.invest_max_14,
	t2.invest_min_14,
	t2.invest_avg_14,
	t2.rate_max_14,
	t2.rate_min_14,
	t2.rate_avg_14,
	t2.days_max_14,
	t2.days_min_14,
	t2.days_avg_14,
	t3.invest_cnt_30,
	t3.invest_sum_30,
	t3.invest_max_30,
	t3.invest_min_30,
	t3.invest_avg_30,
	t3.rate_max_30,
	t3.rate_min_30,
	t3.rate_avg_30,
	t3.days_max_30,
	t3.days_min_30,
	t3.days_avg_30,
	t4.invest_cnt_60,
	t4.invest_sum_60,
	t4.invest_max_60,
	t4.invest_min_60,
	t4.invest_avg_60,
	t4.rate_max_60,
	t4.rate_min_60,
	t4.rate_avg_60,
	t4.days_max_60,
	t4.days_min_60,
	t4.days_avg_60,
	t5.invest_cnt_90,
	t5.invest_sum_90,
	t5.invest_max_90,
	t5.invest_min_90,
	t5.invest_avg_90,
	t5.rate_max_90,
	t5.rate_min_90,
	t5.rate_avg_90,
	t5.days_max_90,
	t5.days_min_90,
	t5.days_avg_90,
	t6.invest_cnt_120,
	t6.invest_sum_120,
	t6.invest_max_120,
	t6.invest_min_120,
	t6.invest_avg_120,
	t6.rate_max_120,
	t6.rate_min_120,
	t6.rate_avg_120,
	t6.days_max_120,
	t6.days_min_120,
	t6.days_avg_120,
	t2_1.deposit_cnt_7,
	t2_1.deposit_sum_7,
	t2_1.deposit_max_7,
	t2_1.deposit_min_7,
	t2_1.deposit_avg_7,
	t2_2.deposit_cnt_14,
	t2_2.deposit_sum_14,
	t2_2.deposit_max_14,
	t2_2.deposit_min_14,
	t2_2.deposit_avg_14,
	t2_3.deposit_cnt_30,
	t2_3.deposit_sum_30,
	t2_3.deposit_max_30,
	t2_3.deposit_min_30,
	t2_3.deposit_avg_30,
	t2_4.deposit_cnt_60,
	t2_4.deposit_sum_60,
	t2_4.deposit_max_60,
	t2_4.deposit_min_60,
	t2_4.deposit_avg_60,
	t2_5.deposit_cnt_90,
	t2_5.deposit_sum_90,
	t2_5.deposit_max_90,
	t2_5.deposit_min_90,
	t2_5.deposit_avg_90,
	t2_6.deposit_cnt_120,
	t2_6.deposit_sum_120,
	t2_6.deposit_max_120,
	t2_6.deposit_min_120,
	t2_6.deposit_avg_120,
	t3_1.withdraw_cnt_7,
	t3_1.withdraw_sum_7,
	t3_1.withdraw_max_7,
	t3_1.withdraw_min_7,
	t3_1.withdraw_avg_7,
	t3_2.withdraw_cnt_14,
	t3_2.withdraw_sum_14,
	t3_2.withdraw_max_14,
	t3_2.withdraw_min_14,
	t3_2.withdraw_avg_14,
	t3_3.withdraw_cnt_30,
	t3_3.withdraw_sum_30,
	t3_3.withdraw_max_30,
	t3_3.withdraw_min_30,
	t3_3.withdraw_avg_30,
	t3_4.withdraw_cnt_60,
	t3_4.withdraw_sum_60,
	t3_4.withdraw_max_60,
	t3_4.withdraw_min_60,
	t3_4.withdraw_avg_60,
	t3_5.withdraw_cnt_90,
	t3_5.withdraw_sum_90,
	t3_5.withdraw_max_90,
	t3_5.withdraw_min_90,
	t3_5.withdraw_avg_90,
	t3_6.withdraw_cnt_120,
	t3_6.withdraw_sum_120,
	t3_6.withdraw_max_120,
	t3_6.withdraw_min_120,
	t3_6.withdraw_avg_120
from
(
	select
		user_id,
		first_invest_tm
	from
		dws.dws_user_base_full
	where
		first_invest_tm<'2016-12-24'
		and first_invest_tm is not null
		and dt='2017-01-01'
) as t
left outer join
(
	select
		a.user_id,
		count(b.user_id) as invest_cnt_7,
		sum(b.invest_amount) as invest_sum_7,
		max(b.invest_amount) as invest_max_7,
		min(b.invest_amount) as invest_min_7,
		round(avg(b.invest_amount), 2) as invest_avg_7,
		max(b.loan_rate) as rate_max_7,
		min(b.loan_rate) as rate_min_7,
		round(avg(b.loan_rate),3) as rate_avg_7,
		max(b.loan_days) as days_max_7,
		min(b.loan_days) as days_min_7,
		round(avg(b.loan_days), 2) as days_avg_7
	from
		(
		    select
		    	user_id,
		    	first_invest_tm
		    from
			    dws.dws_user_base_full
			where
			    dt='2017-01-01'
			    and first_invest_tm<'2016-12-24'
			    and first_invest_tm is not null
		) as a
	left outer join
		(
			select
				user_id,
				invest_amount,
				loan_rate,
				loan_years*365+loan_months*30+loan_days as loan_days,
				invest_tm
			from
				dwi.dwi_ordr_overall_invest_full
			where
				order_type = 'INVEST'
				and order_success_flag = 1
				and dt='2017-01-01'
		) as b
	on
		a.user_id = b.user_id
	where
		datediff(substr(b.invest_tm,1,10), substr(a.first_invest_tm,1,10))<=7
	group by
		a.user_id
)t1
on
	t.user_id = t1.user_id
left outer join
(
	select
		a.user_id,
		count(b.user_id) as invest_cnt_14,
		sum(b.invest_amount) as invest_sum_14,
		max(b.invest_amount) as invest_max_14,
		min(b.invest_amount) as invest_min_14,
		round(avg(b.invest_amount), 2) as invest_avg_14,
		max(b.loan_rate) as rate_max_14,
		min(b.loan_rate) as rate_min_14,
		round(avg(b.loan_rate),3) as rate_avg_14,
		max(b.loan_days) as days_max_14,
		min(b.loan_days) as days_min_14,
		round(avg(b.loan_days), 2) as days_avg_14
	from
		(
		    select
		    	user_id,
		    	first_invest_tm
		    from
			    dws.dws_user_base_full
			where
			    dt='2017-01-01'
			    and first_invest_tm<'2016-12-17'
			    and first_invest_tm is not null
		) as a
	left outer join
		(
			select
				user_id,
				invest_amount,
				loan_rate,
				loan_years*365+loan_months*30+loan_days as loan_days,
				invest_tm
			from
				dwi.dwi_ordr_overall_invest_full
			where
				order_type = 'INVEST'
				and order_success_flag = 1
				and dt='2017-01-01'
		) as b
	on
		a.user_id = b.user_id
	where
		datediff(substr(b.invest_tm,1,10), substr(a.first_invest_tm,1,10))<=14
	group by
		a.user_id
)t2
on
	t.user_id = t2.user_id
left outer join
(
	select
		a.user_id,
		count(b.user_id) as invest_cnt_30,
		sum(b.invest_amount) as invest_sum_30,
		max(b.invest_amount) as invest_max_30,
		min(b.invest_amount) as invest_min_30,
		round(avg(b.invest_amount), 2) as invest_avg_30,
		max(b.loan_rate) as rate_max_30,
		min(b.loan_rate) as rate_min_30,
		round(avg(b.loan_rate),3) as rate_avg_30,
		max(b.loan_days) as days_max_30,
		min(b.loan_days) as days_min_30,
		round(avg(b.loan_days), 2) as days_avg_30

	from
		(
		    select
		    	user_id,
		    	first_invest_tm
		    from
			    dws.dws_user_base_full
			where
			    dt='2017-01-01'
			    and first_invest_tm<'2016-12-01'
			    and first_invest_tm is not null
		) as a
	left outer join
		(
			select
				user_id,
				invest_amount,
				loan_rate,
				loan_years*365+loan_months*30+loan_days as loan_days,
				invest_tm
			from
				dwi.dwi_ordr_overall_invest_full
			where
				order_type = 'INVEST'
				and order_success_flag = 1
				and dt='2017-01-01'
		) as b
	on
		a.user_id = b.user_id
	where
		datediff(substr(b.invest_tm,1,10), substr(a.first_invest_tm,1,10))<=30
	group by
		a.user_id
)t3
on
	t.user_id = t3.user_id
left outer join
(
	select
		a.user_id,
		count(b.user_id) as invest_cnt_60,
		sum(b.invest_amount) as invest_sum_60,
		max(b.invest_amount) as invest_max_60,
		min(b.invest_amount) as invest_min_60,
		round(avg(b.invest_amount), 2) as invest_avg_60,
		max(b.loan_rate) as rate_max_60,
		min(b.loan_rate) as rate_min_60,
		round(avg(b.loan_rate),3) as rate_avg_60,
		max(b.loan_days) as days_max_60,
		min(b.loan_days) as days_min_60,
		round(avg(b.loan_days), 2) as days_avg_60

	from
		(
		    select
		    	user_id,
		    	first_invest_tm
		    from
			    dws.dws_user_base_full
			where
			    dt='2017-01-01'
			    and first_invest_tm<'2016-11-01'
			    and first_invest_tm is not null
		) as a
	left outer join
		(
			select
				user_id,
				invest_amount,
				loan_rate,
				loan_years*365+loan_months*30+loan_days as loan_days,
				invest_tm
			from
				dwi.dwi_ordr_overall_invest_full
			where
				order_type = 'INVEST'
				and order_success_flag = 1
				and dt='2017-01-01'
		) as b
	on
		a.user_id = b.user_id
	where
		datediff(substr(b.invest_tm,1,10), substr(a.first_invest_tm,1,10))<=60
	group by
		a.user_id
)t4
on
	t.user_id = t4.user_id
left outer join
(
	select
		a.user_id,
		count(b.user_id) as invest_cnt_90,
		sum(b.invest_amount) as invest_sum_90,
		max(b.invest_amount) as invest_max_90,
		min(b.invest_amount) as invest_min_90,
		round(avg(b.invest_amount), 2) as invest_avg_90,
		max(b.loan_rate) as rate_max_90,
		min(b.loan_rate) as rate_min_90,
		round(avg(b.loan_rate),3) as rate_avg_90,
		max(b.loan_days) as days_max_90,
		min(b.loan_days) as days_min_90,
		round(avg(b.loan_days), 2) as days_avg_90

	from
		(
		    select
		    	user_id,
		    	first_invest_tm
		    from
			    dws.dws_user_base_full
			where
			    dt='2017-01-01'
			    and first_invest_tm<'2016-10-01'
			    and first_invest_tm is not null
		) as a
	left outer join
		(
			select
				user_id,
				invest_amount,
				loan_rate,
				loan_years*365+loan_months*30+loan_days as loan_days,
				invest_tm
			from
				dwi.dwi_ordr_overall_invest_full
			where
				order_type = 'INVEST'
				and order_success_flag = 1
				and dt='2017-01-01'
		) as b
	on
		a.user_id = b.user_id
	where
		datediff(substr(b.invest_tm,1,10), substr(a.first_invest_tm,1,10))<=90
	group by
		a.user_id
)t5
on
	t.user_id = t5.user_id
left outer join
(
	select
		a.user_id,
		count(b.user_id) as invest_cnt_120,
		sum(b.invest_amount) as invest_sum_120,
		max(b.invest_amount) as invest_max_120,
		min(b.invest_amount) as invest_min_120,
		round(avg(b.invest_amount), 2) as invest_avg_120,
		max(b.loan_rate) as rate_max_120,
		min(b.loan_rate) as rate_min_120,
		round(avg(b.loan_rate),3) as rate_avg_120,
		max(b.loan_days) as days_max_120,
		min(b.loan_days) as days_min_120,
		round(avg(b.loan_days), 2) as days_avg_120

	from
		(
		    select
		    	user_id,
		    	first_invest_tm
		    from
			    dws.dws_user_base_full
			where
			    dt='2017-01-01'
			    and first_invest_tm<'2016-09-01'
			    and first_invest_tm is not null
		) as a
	left outer join
		(
			select
				user_id,
				invest_amount,
				loan_rate,
				loan_years*365+loan_months*30+loan_days as loan_days,
				invest_tm
			from
				dwi.dwi_ordr_overall_invest_full
			where
				order_type = 'INVEST'
				and order_success_flag = 1
				and dt='2017-01-01'
		) as b
	on
		a.user_id = b.user_id
	where
		datediff(substr(b.invest_tm,1,10), substr(a.first_invest_tm,1,10))<=120
	group by
		a.user_id
)t6
on
	t.user_id = t6.user_id
left outer join
-- 充值
(
	select
		a.user_id,
		count(distinct b.order_id) as deposit_cnt_7,
		sum(b.fund_record_amount) as deposit_sum_7,
		max(b.fund_record_amount) as deposit_max_7,
		min(b.fund_record_amount) as deposit_min_7,
		round(avg(b.fund_record_amount), 2) as deposit_avg_7
	from
		(
		    select
		    	user_id,
		    	first_invest_tm
		    from
			    dws.dws_user_base_full
			where
			    dt='2017-01-01'
			    and first_invest_tm<'2016-12-24'
			    and first_invest_tm is not null
		) as a
	left outer join
		(
			select
				user_id,
				order_id,
				fund_record_amount,
				create_tm
			from
				dwi.dwi_finc_record_full
			where
				dt= '2017-01-01'
				and fund_record_status='SUCCESSFUL'
				and fund_record_operation_type='IN'
				and fund_record_sec_type ='DEPOSIT'
		) as b
	on
		a.user_id = b.user_id
	where
		datediff(substr(b.create_tm,1,10), substr(a.first_invest_tm,1,10))<=7
	group by
		a.user_id
)as t2_1
on
	t.user_id = t2_1.user_id
left outer join
(
	select
		a.user_id,
		count(distinct b.order_id) as deposit_cnt_14,
		sum(b.fund_record_amount) as deposit_sum_14,
		max(b.fund_record_amount) as deposit_max_14,
		min(b.fund_record_amount) as deposit_min_14,
		round(avg(b.fund_record_amount), 2) as deposit_avg_14
	from
		(
		    select
		    	user_id,
		    	first_invest_tm
		    from
			    dws.dws_user_base_full
			where
			    dt='2017-01-01'
			    and first_invest_tm<'2016-12-17'
			    and first_invest_tm is not null
		) as a
	left outer join
		(
			select
				user_id,
				order_id,
				fund_record_amount,
				create_tm
			from
				dwi.dwi_finc_record_full
			where
				dt= '2017-01-01'
				and fund_record_status='SUCCESSFUL'
				and fund_record_operation_type='IN'
				and fund_record_sec_type ='DEPOSIT'
		) as b
	on
		a.user_id = b.user_id
	where
		datediff(substr(b.create_tm,1,10), substr(a.first_invest_tm,1,10))<=14
	group by
		a.user_id
)as t2_2
on
	t.user_id = t2_2.user_id
left outer join
(
	select
		a.user_id,
		count(distinct b.order_id) as deposit_cnt_30,
		sum(b.fund_record_amount) as deposit_sum_30,
		max(b.fund_record_amount) as deposit_max_30,
		min(b.fund_record_amount) as deposit_min_30,
		round(avg(b.fund_record_amount), 2) as deposit_avg_30
	from
		(
		    select
		    	user_id,
		    	first_invest_tm
		    from
			    dws.dws_user_base_full
			where
			    dt='2017-01-01'
			    and first_invest_tm<'2016-12-01'
			    and first_invest_tm is not null
		) as a
	left outer join
		(
			select
				user_id,
				order_id,
				fund_record_amount,
				create_tm
			from
				dwi.dwi_finc_record_full
			where
				dt= '2017-01-01'
				and fund_record_status='SUCCESSFUL'
				and fund_record_operation_type='IN'
				and fund_record_sec_type ='DEPOSIT'
		) as b
	on
		a.user_id = b.user_id
	where
		datediff(substr(b.create_tm,1,10), substr(a.first_invest_tm,1,10))<=30
	group by
		a.user_id
)as t2_3
on
	t.user_id = t2_3.user_id
left outer join
(
	select
		a.user_id,
		count(distinct b.order_id) as deposit_cnt_60,
		sum(b.fund_record_amount) as deposit_sum_60,
		max(b.fund_record_amount) as deposit_max_60,
		min(b.fund_record_amount) as deposit_min_60,
		round(avg(b.fund_record_amount), 2) as deposit_avg_60
	from
		(
		    select
		    	user_id,
		    	first_invest_tm
		    from
			    dws.dws_user_base_full
			where
			    dt='2017-01-01'
			    and first_invest_tm<'2016-11-01'
			    and first_invest_tm is not null
		) as a
	left outer join
		(
			select
				user_id,
				order_id,
				fund_record_amount,
				create_tm
			from
				dwi.dwi_finc_record_full
			where
				dt= '2017-01-01'
				and fund_record_status='SUCCESSFUL'
				and fund_record_operation_type='IN'
				and fund_record_sec_type ='DEPOSIT'
		) as b
	on
		a.user_id = b.user_id
	where
		datediff(substr(b.create_tm,1,10), substr(a.first_invest_tm,1,10))<=60
	group by
		a.user_id
)as t2_4
on
	t.user_id = t2_4.user_id
left outer join
(
	select
		a.user_id,
		count(distinct b.order_id) as deposit_cnt_90,
		sum(b.fund_record_amount) as deposit_sum_90,
		max(b.fund_record_amount) as deposit_max_90,
		min(b.fund_record_amount) as deposit_min_90,
		round(avg(b.fund_record_amount), 2) as deposit_avg_90
	from
		(
		    select
		    	user_id,
		    	first_invest_tm
		    from
			    dws.dws_user_base_full
			where
			    dt='2017-01-01'
			    and first_invest_tm<'2016-10-01'
			    and first_invest_tm is not null
		) as a
	left outer join
		(
			select
				user_id,
				order_id,
				fund_record_amount,
				create_tm
			from
				dwi.dwi_finc_record_full
			where
				dt= '2017-01-01'
				and fund_record_status='SUCCESSFUL'
				and fund_record_operation_type='IN'
				and fund_record_sec_type ='DEPOSIT'
		) as b
	on
		a.user_id = b.user_id
	where
		datediff(substr(b.create_tm,1,10), substr(a.first_invest_tm,1,10))<=90
	group by
		a.user_id
)as t2_5
on
	t.user_id = t2_5.user_id
left outer join
(
	select
		a.user_id,
		count(distinct b.order_id) as deposit_cnt_120,
		sum(b.fund_record_amount) as deposit_sum_120,
		max(b.fund_record_amount) as deposit_max_120,
		min(b.fund_record_amount) as deposit_min_120,
		round(avg(b.fund_record_amount), 2) as deposit_avg_120
	from
		(
		    select
		    	user_id,
		    	first_invest_tm
		    from
			    dws.dws_user_base_full
			where
			    dt='2017-01-01'
			    and first_invest_tm<'2016-09-01'
			    and first_invest_tm is not null
		) as a
	left outer join
		(
			select
				user_id,
				order_id,
				fund_record_amount,
				create_tm
			from
				dwi.dwi_finc_record_full
			where
				dt= '2017-01-01'
				and fund_record_status='SUCCESSFUL'
				and fund_record_operation_type='IN'
				and fund_record_sec_type ='DEPOSIT'
		) as b
	on
		a.user_id = b.user_id
	where
		datediff(substr(b.create_tm,1,10), substr(a.first_invest_tm,1,10))<=120
	group by
		a.user_id
)as t2_6
on
	t.user_id = t2_6.user_id
-- 提现
left outer join
(
	select
		a.user_id,
		count(distinct b.order_id) as withdraw_cnt_7,
		sum(b.fund_record_amount) as withdraw_sum_7,
		max(b.fund_record_amount) as withdraw_max_7,
		min(b.fund_record_amount) as withdraw_min_7,
		round(avg(b.fund_record_amount), 2) as withdraw_avg_7
	from
	(
	    select
	    	user_id,
	    	first_invest_tm
	    from
		    dws.dws_user_base_full
		where
		    dt='2017-01-01'
		    and first_invest_tm<'2016-12-24'
		    and first_invest_tm is not null
	) as a
	left outer join
	(
		select
			user_id,
			order_id,
			fund_record_amount,
			create_tm
		from
			dwi.dwi_finc_record_full
		where
			dt= '2017-01-01'
			and fund_record_status='SUCCESSFUL'
			and fund_record_operation_type='OUT'
			and fund_record_sec_type ='WITHDRAW'
	) as b
	on
		a.user_id = b.user_id
	where
		datediff(substr(b.create_tm,1,10), substr(a.first_invest_tm,1,10))<=7
	group by
		a.user_id
) as t3_1
on
	t.user_id = t3_1.user_id
left outer join
(
	select
		a.user_id,
		count(distinct b.order_id) as withdraw_cnt_14,
		sum(b.fund_record_amount) as withdraw_sum_14,
		max(b.fund_record_amount) as withdraw_max_14,
		min(b.fund_record_amount) as withdraw_min_14,
		round(avg(b.fund_record_amount), 2) as withdraw_avg_14
	from
	(
	    select
	    	user_id,
	    	first_invest_tm
	    from
		    dws.dws_user_base_full
		where
		    dt='2017-01-01'
		    and first_invest_tm<'2016-12-17'
		    and first_invest_tm is not null
	) as a
	left outer join
	(
		select
			user_id,
			order_id,
			fund_record_amount,
			create_tm
		from
			dwi.dwi_finc_record_full
		where
			dt= '2017-01-01'
			and fund_record_status='SUCCESSFUL'
			and fund_record_operation_type='OUT'
			and fund_record_sec_type ='WITHDRAW'
	) as b
	on
		a.user_id = b.user_id
	where
		datediff(substr(b.create_tm,1,10), substr(a.first_invest_tm,1,10))<=14
	group by
		a.user_id
) as t3_2
on
	t.user_id = t3_2.user_id
left outer join
(
	select
		a.user_id,
		count(distinct b.order_id) as withdraw_cnt_30,
		sum(b.fund_record_amount) as withdraw_sum_30,
		max(b.fund_record_amount) as withdraw_max_30,
		min(b.fund_record_amount) as withdraw_min_30,
		round(avg(b.fund_record_amount), 2) as withdraw_avg_30
	from
	(
	    select
	    	user_id,
	    	first_invest_tm
	    from
		    dws.dws_user_base_full
		where
		    dt='2017-01-01'
		    and first_invest_tm<'2016-12-01'
		    and first_invest_tm is not null
	) as a
	left outer join
	(
		select
			user_id,
			order_id,
			fund_record_amount,
			create_tm
		from
			dwi.dwi_finc_record_full
		where
			dt= '2017-01-01'
			and fund_record_status='SUCCESSFUL'
			and fund_record_operation_type='OUT'
			and fund_record_sec_type ='WITHDRAW'
	) as b
	on
		a.user_id = b.user_id
	where
		datediff(substr(b.create_tm,1,10), substr(a.first_invest_tm,1,10))<=30
	group by
		a.user_id
) as t3_3
on
	t.user_id = t3_3.user_id
left outer join
(
	select
		a.user_id,
		count(distinct b.order_id) as withdraw_cnt_60,
		sum(b.fund_record_amount) as withdraw_sum_60,
		max(b.fund_record_amount) as withdraw_max_60,
		min(b.fund_record_amount) as withdraw_min_60,
		round(avg(b.fund_record_amount), 2) as withdraw_avg_60
	from
	(
	    select
	    	user_id,
	    	first_invest_tm
	    from
		    dws.dws_user_base_full
		where
		    dt='2017-01-01'
		    and first_invest_tm<'2016-11-01'
		    and first_invest_tm is not null
	) as a
	left outer join
	(
		select
			user_id,
			order_id,
			fund_record_amount,
			create_tm
		from
			dwi.dwi_finc_record_full
		where
			dt= '2017-01-01'
			and fund_record_status='SUCCESSFUL'
			and fund_record_operation_type='OUT'
			and fund_record_sec_type ='WITHDRAW'
	) as b
	on
		a.user_id = b.user_id
	where
		datediff(substr(b.create_tm,1,10), substr(a.first_invest_tm,1,10))<=60
	group by
		a.user_id
) as t3_4
on
	t.user_id = t3_4.user_id
left outer join
(
	select
		a.user_id,
		count(distinct b.order_id) as withdraw_cnt_90,
		sum(b.fund_record_amount) as withdraw_sum_90,
		max(b.fund_record_amount) as withdraw_max_90,
		min(b.fund_record_amount) as withdraw_min_90,
		round(avg(b.fund_record_amount), 2) as withdraw_avg_90
	from
	(
	    select
	    	user_id,
	    	first_invest_tm
	    from
		    dws.dws_user_base_full
		where
		    dt='2017-01-01'
		    and first_invest_tm<'2016-10-01'
		    and first_invest_tm is not null
	) as a
	left outer join
	(
		select
			user_id,
			order_id,
			fund_record_amount,
			create_tm
		from
			dwi.dwi_finc_record_full
		where
			dt= '2017-01-01'
			and fund_record_status='SUCCESSFUL'
			and fund_record_operation_type='OUT'
			and fund_record_sec_type ='WITHDRAW'
	) as b
	on
		a.user_id = b.user_id
	where
		datediff(substr(b.create_tm,1,10), substr(a.first_invest_tm,1,10))<=90
	group by
		a.user_id
) as t3_5
on
	t.user_id = t3_5.user_id
left outer join
(
	select
		a.user_id,
		count(distinct b.order_id) as withdraw_cnt_120,
		sum(b.fund_record_amount) as withdraw_sum_120,
		max(b.fund_record_amount) as withdraw_max_120,
		min(b.fund_record_amount) as withdraw_min_120,
		round(avg(b.fund_record_amount), 2) as withdraw_avg_120
	from
	(
	    select
	    	user_id,
	    	first_invest_tm
	    from
		    dws.dws_user_base_full
		where
		    dt='2017-01-01'
		    and first_invest_tm<'2016-09-01'
		    and first_invest_tm is not null
	) as a
	left outer join
	(
		select
			user_id,
			order_id,
			fund_record_amount,
			create_tm
		from
			dwi.dwi_finc_record_full
		where
			dt= '2017-01-01'
			and fund_record_status='SUCCESSFUL'
			and fund_record_operation_type='OUT'
			and fund_record_sec_type ='WITHDRAW'
	) as b
	on
		a.user_id = b.user_id
	where
		datediff(substr(b.create_tm,1,10), substr(a.first_invest_tm,1,10))<=120
	group by
		a.user_id
) as t3_6
on
	t.user_id = t3_6.user_id;
