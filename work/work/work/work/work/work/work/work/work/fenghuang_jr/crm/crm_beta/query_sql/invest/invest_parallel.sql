use crm_v2;
insert overwrite table crm_desc_json_new
select
    b.user_id,
    'null',
--    md5_sort(concat_ws(',',collect_set(md5(toJson('id',b.invest_id,0,'ca',b.category,0,'su',b.submit_time,0,'due',b.due_date,0,'am',amount,0,'due_amount',due_amount,0)))),','),
    json_list('invest_id',b.invest_id,'category',b.category,'submit_time',b.submit_time,'submit_time_int',int(regexp_replace(b.submit_time,'[-]','')),'due_date',b.due_date,'due_date_int',int(regexp_replace(b.due_date,'[-]','')),'amount',amount,'due_amount',due_amount) as logger
from
    crm_invest_desc_status as b
group by
    b.user_id;