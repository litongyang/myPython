SELECT
  t.id as coupon_id,
  ( CASE WHEN EVENT_ID IN ( 'REGISTERCOUPON-20150801-001', 'INCLUSIVE-201511-001' ) THEN 1 ELSE 0 END ) AS register_count,
  ( CASE WHEN EVENT_ID IN ( 'REGISTERCOUPON-20150801-001', 'INCLUSIVE-201511-001' ) THEN CASE WHEN STATUS IN ('FROZEN', 'ACTIVATED') THEN 1 ELSE 0 END ELSE 0 END ) AS register_used,
  ( CASE WHEN EVENT_ID IN ('POINTSMALL-20151103-001','POINTSMALL-20151103-002','POINTSMALL-20151210-001','POINTSMALL-20151210-002','POINTSMALL-20151210-003') THEN 1 ELSE 0 END ) AS points_count,
  ( CASE WHEN EVENT_ID IN ('POINTSMALL-20151103-001','POINTSMALL-20151103-002','POINTSMALL-20151210-001','POINTSMALL-20151210-002','POINTSMALL-20151210-003') THEN CASE WHEN STATUS IN ('FROZEN', 'ACTIVATED') THEN 1 ELSE 0 END ELSE 0 END ) AS points_used,
  ( CASE WHEN EVENT_ID = 'REBATE-201507-001' THEN 1 ELSE 0 END ) AS rebate_count,
  ( CASE WHEN EVENT_ID = 'REBATE-201507-001' THEN CASE WHEN STATUS IN ('FROZEN', 'ACTIVATED') THEN 1 ELSE 0 END ELSE 0 END ) AS rebate_used,
  ( CASE WHEN EVENT_ID IN ( 'WEEKEND-201601-002', 'WEEKEND-201601-003') THEN 1 ELSE 0 END ) AS weekend_count,
  ( CASE WHEN EVENT_ID IN ( 'WEEKEND-201601-002', 'WEEKEND-201601-003') THEN CASE WHEN STATUS IN ('FROZEN', 'ACTIVATED') THEN 1 ELSE 0 END ELSE 0 END ) AS weekend_used,
  ( CASE WHEN EVENT_ID IN ( 'POINTSMALL-20160118-001', 'POINTSMALL-20160118-002' ) THEN 1 ELSE 0 END ) AS newyear_count,
  ( CASE WHEN EVENT_ID IN ( 'POINTSMALL-20160118-001', 'POINTSMALL-20160118-002' ) THEN CASE WHEN STATUS IN ('FROZEN', 'ACTIVATED') THEN 1 ELSE 0 END ELSE 0 END ) AS newyear_used,
  ( CASE WHEN EVENT_ID IN ( 'TURNPLATE-201601-001', 'TURNPLATE-201601-002', 'TURNPLATE-201601-003' ) THEN 1 ELSE 0 END ) AS turnplate_count,
  ( CASE WHEN EVENT_ID IN ( 'TURNPLATE-201601-001', 'TURNPLATE-201601-002', 'TURNPLATE-201601-003' ) THEN CASE WHEN STATUS IN ('FROZEN', 'ACTIVATED') THEN 1 ELSE 0 END ELSE 0 END ) AS turnplate_used,
  CASE WHEN EVENT_ID in ('REGISTERCOUPON-20150801-001', 'INCLUSIVE-201511-001') THEN 'register'
       WHEN EVENT_ID IN ('POINTSMALL-20151103-001','POINTSMALL-20151103-002','POINTSMALL-20151210-001','POINTSMALL-20151210-002','POINTSMALL-20151210-003') THEN 'points'
       WHEN EVENT_ID = 'REBATE-201507-001' THEN 'rebate'
       WHEN EVENT_ID in ('WEEKEND-201601-002', 'WEEKEND-201601-003') THEN 'weekend'
       WHEN EVENT_ID in ('POINTSMALL-20160118-001', 'POINTSMALL-20160118-002') THEN 'newyear'
	   WHEN EVENT_ID in ('TURNPLATE-201601-001', 'TURNPLATE-201601-002', 'TURNPLATE-201601-003') THEN 'turnplate' ELSE 'other' END as tag,
  t.*
FROM
 TB_COUPON_RECORD t
where \$CONDITIONS