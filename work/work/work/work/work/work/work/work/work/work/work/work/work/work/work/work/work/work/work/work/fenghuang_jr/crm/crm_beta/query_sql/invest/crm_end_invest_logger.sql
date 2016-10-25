use crm_v2;
insert overwrite local directory '/data/ml/tongyang/data/invest/invest_logger'
select
    b.user_id,
    json_list('invest_id',b.invest_id,'category',b.category,'submit_time',b.submit_time,'submit_time_int',int(regexp_replace(b.submit_time,'[-]','')),'due_date',b.due_date,'due_date_int',int(regexp_replace(b.due_date,'[-]','')),'amount',amount,'due_amount',due_amount) as logger
from
    crm_invest_desc_status as b
group by
    b.user_id;