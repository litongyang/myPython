insert overwrite table app.app_user_first_invest_predict_label
select
A.user_id,
A.y_1_amount,
B.y_2_amount,
C.y_3_amount,
D.y_6_amount,
E.y_9_amount,
F.y_12_amount
from
(
select
a.user_id,
sum(b.invest_amount) as y_1_amount
from
(
select user_id, first_invest_tm from dws.dws_user_base_full where first_invest_tm<'2016-12-01' and first_invest_tm is not null and dt='2017-01-04'
) a
left join
(
select
user_id,invest_amount,invest_tm from dwi.dwi_ordr_overall_invest_full where order_type = 'INVEST' and order_success_flag = 1 and dt='2017-01-01'
) b
on a.user_id = b.user_id
where datediff(substr(b.invest_tm,1,10), substr(a.first_invest_tm,1,10)) <= 30
group by a.user_id
) A
left join
(
select
a.user_id,
sum(b.invest_amount) as y_2_amount
from
(
select user_id, first_invest_tm from dws.dws_user_base_full where first_invest_tm<'2016-11-01' and first_invest_tm is not null and dt='2017-01-04'
) a
left join
(
select
user_id,invest_amount,invest_tm from dwi.dwi_ordr_overall_invest_full where  order_type = 'INVEST' and order_success_flag = 1 and dt='2017-01-01'
) b
on a.user_id = b.user_id
where datediff(substr(b.invest_tm,1,10), substr(a.first_invest_tm,1,10)) <= 60
group by a.user_id
) B
on A.user_id = B.user_id
left join
(
select
a.user_id,
sum(b.invest_amount) as y_3_amount
from
(
select user_id, first_invest_tm from dws.dws_user_base_full where first_invest_tm<'2016-10-01' and first_invest_tm is not null and dt='2017-01-04'
) a
left join
(
select
user_id,invest_amount,invest_tm from dwi.dwi_ordr_overall_invest_full where  order_type = 'INVEST' and order_success_flag = 1 and dt='2017-01-01'
) b
on a.user_id = b.user_id
where datediff(substr(b.invest_tm,1,10), substr(a.first_invest_tm,1,10)) <= 90
group by a.user_id
) C
on A.user_id = C.user_id
left join
(
select
a.user_id,
sum(b.invest_amount) as y_6_amount
from
(
select user_id, first_invest_tm from dws.dws_user_base_full where first_invest_tm<'2016-07-01' and first_invest_tm is not null and dt='2017-01-04'
) a
left join
(
select
user_id,invest_amount,invest_tm from dwi.dwi_ordr_overall_invest_full where  order_type = 'INVEST' and order_success_flag = 1 and dt='2017-01-01'
) b
on a.user_id = b.user_id
where datediff(substr(b.invest_tm,1,10), substr(a.first_invest_tm,1,10)) <= 180
group by a.user_id
) D
on A.user_id = D.user_id
left join
(
select
a.user_id,
sum(b.invest_amount) as y_9_amount
from
(
select user_id, first_invest_tm from dws.dws_user_base_full where first_invest_tm<'2016-04-01' and first_invest_tm is not null and dt='2017-01-04'
) a
left join
(
select
user_id,invest_amount,invest_tm from dwi.dwi_ordr_overall_invest_full where  order_type = 'INVEST' and order_success_flag = 1 and dt='2017-01-01'
) b
on a.user_id = b.user_id
where datediff(substr(b.invest_tm,1,10), substr(a.first_invest_tm,1,10)) <= 270
group by a.user_id
) E
on A.user_id = E.user_id
left join
(
select
a.user_id,
sum(b.invest_amount) as y_12_amount
from
(
select user_id, first_invest_tm from dws.dws_user_base_full where first_invest_tm<='2016-01-01' and first_invest_tm is not null and dt='2017-01-04'
) a
left join
(
select
user_id,invest_amount,invest_tm from dwi.dwi_ordr_overall_invest_full where  order_type = 'INVEST' and order_success_flag = 1 and dt='2017-01-01'
) b
on a.user_id = b.user_id
where datediff(substr(b.invest_tm,1,10), substr(a.first_invest_tm,1,10)) <= 365
group by a.user_id
) F
on A.user_id = F.user_id;