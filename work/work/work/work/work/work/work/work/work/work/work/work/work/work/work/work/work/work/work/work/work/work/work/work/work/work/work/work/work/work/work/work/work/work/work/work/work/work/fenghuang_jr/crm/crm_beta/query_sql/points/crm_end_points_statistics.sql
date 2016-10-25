use crm_v2;
insert overwrite local directory '/data/ml/tongyang/data/points/points_statistics'

select
    user_id,
    toJson(
	'total_points',total_points,0,
	'available_points',available_points,0,
	'consum_points_cnt',consum_points_cnt,0,
	'consum_points_max',consum_points_max,0,
	'consum_points_min',consum_points_min,0,
	'consum_points_sum',consum_points_sum,0) as points_statistics_json
from
    crm_points_statistics;