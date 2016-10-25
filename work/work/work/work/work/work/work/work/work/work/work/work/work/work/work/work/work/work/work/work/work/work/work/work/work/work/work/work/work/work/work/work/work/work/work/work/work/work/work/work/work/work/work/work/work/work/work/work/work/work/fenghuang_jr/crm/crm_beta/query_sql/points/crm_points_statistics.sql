use crm_v2;
insert overwrite table crm_points_statistics
select
	a.id_c as user_id,
	a.total_points_c as total_points,
	a.available_points_c as available_points,
	b.consum_points_cnt as consum_points_cnt,
	b.consum_points_max as consum_points_max,
	b.consum_points_min as consum_points_min,
	b.consum_points_sum as consum_points_sum
from
	crm_contacts_cstm a
left outer join
	(
		 select
			contacts_id as user_id,
			count(contacts_id) as consum_points_cnt,
			max(points) as consum_points_max,
			min(points) as consum_points_min,
			sum(points) as consum_points_sum
		from
			crm_ptsts_points_transaction
		where
			transaction_type = 'CONSUME'
		group by
			contacts_id
	)b
on
	a.id_c = b.user_id;