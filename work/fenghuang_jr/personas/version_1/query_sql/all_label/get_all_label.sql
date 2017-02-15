use app;
insert overwrite table personas_predict_label_full partition (dt='${dt}')
select 
	a.user_id as user_id,
	b.age_label as age_label,
	c.next_rate as next_rate,
	int(d.next_deadline) as next_dealine,
	e.invest_var_label as invest_var_label,
	f.recommend_bid_list as invest_recommend_bid_list,
	f.show_recommend_bid_list as show_invest_recommend_bid_list,
	g.recommend_user_list  as invest_recommend_user_list,
	h.recommend_bid_list  as view_recommend_bid_list,
	h.show_recommend_bid_list as show_view_recommend_bid_list,
	i.recommend_user_list  as view_recommend_user_list
from 
	dim.dim_user_base a
left outer join
	(
		select
			user_id,
			age,
			classified_id,
			age_label
		from
			app.personas_user_age_label_full
		where
			dt = '${dt}'
	)as b
on
	a.user_id = b.user_id
left outer join
	(
		select
			user_id,
			next_rate
		from
			app.personas_next_invest_bid_label_full
		where	
			dt = '${dt}'

	)as c
on
	a.user_id = c.user_id
left outer join
	(
		select
			user_id,
			next_deadline
		from
			app.personas_next_invest_bid_deadline_label_full
		where
			dt = '${dt}'
	)as d
on
	a.user_id = d.user_id
left outer join
	(
		select
			user_id,
			invest_var,
			classified_id,
			invest_var_label
		from
			app.personas_user_invest_var_label_full
		where
			dt = '${dt}'
	)as e
on
	a.user_id = e.user_id
left outer join
	(
		select
			user_id,
			concat_ws(',', collect_list(cast(recommend_bid as string))) as recommend_bid_list,
			concat_ws(',', collect_list(cast(show_recommend_bid as string))) as show_recommend_bid_list,
			concat_ws(',', collect_list(cast(recommend_bid_score as string))) as recommend_bid_score_list
		from
			(
				select 
				  user_id,
				  recommend_bid,
				  case when recommend_bid = 'short-low' then '短期、低利率'
				       when recommend_bid = 'short-mid' then '短期、适中利率'
				       when recommend_bid = 'short-high' then '短期、高利率'
				       when recommend_bid = 'between-low' then '中期、低利率'
				       when recommend_bid = 'between-mid' then '中期、适中利率'
				       when recommend_bid = 'between-high' then '中期、高利率'
				       when recommend_bid = 'long-low' then '长期、低利率'
				       when recommend_bid = 'long-mid' then '长期、适中利率'
				       when recommend_bid = 'long-high' then '长期、高利率'
				  else '未知' end as show_recommend_bid,
				  recommend_bid_score
				from
					app.personas_user_relation_invest_bid_label_full
				where
					dt = '${dt}'
			)as t
		group by
			user_id
	)as f
on
	a.user_id = f.user_id
left outer join
	(
		select
			user_id,
			concat_ws(',', collect_list(cast(recommend_user as string))) as recommend_user_list,
			concat_ws(',', collect_list(cast(recommend_user_score as string))) as recommend_user_score_list
		from
			app.personas_user_relation_invest_user_label_full
		where
			dt = '${dt}'
		group by
			user_id
	)as g
on
	a.user_id = g.user_id
left outer join
	(
		select
			user_id,
			concat_ws(',', collect_list(cast(recommend_bid as string))) as recommend_bid_list,
			concat_ws(',', collect_list(cast(show_recommend_bid as string))) as show_recommend_bid_list,
			concat_ws(',', collect_list(cast(recommend_bid_score as string))) as recommend_bid_score_list
		from
			(
             	select 
				  user_id,
				  recommend_bid,
				  case when recommend_bid = 'short-low' then '短期、低利率'
				       when recommend_bid = 'short-mid' then '短期、适中利率'
				       when recommend_bid = 'short-high' then '短期、高利率'
				       when recommend_bid = 'between-low' then '中期、低利率'
				       when recommend_bid = 'between-mid' then '中期、适中利率'
				       when recommend_bid = 'between-high' then '中期、高利率'
				       when recommend_bid = 'long-low' then '长期、低利率'
				       when recommend_bid = 'long-mid' then '长期、适中利率'
				       when recommend_bid = 'long-high' then '长期、高利率'
				  else '未知' end as show_recommend_bid,
				  recommend_bid_score
				from
				 app.personas_user_relation_invest_view_bid_label_full
				where
					dt = '${before}'
			)as t
		group by
			user_id
	)as h
on
	a.user_id = h.user_id
left outer join
	(
		select
			user_id,
			concat_ws(',', collect_list(cast(recommend_user as string))) as recommend_user_list,
			concat_ws(',', collect_list(cast(recommend_user_score as string))) as recommend_user_score_list
		from
			app.personas_user_relation_invest_view_user_label_full
		where
			dt = '${before}'
		group by
			user_id
	)as i
on
	a.user_id = i.user_id
