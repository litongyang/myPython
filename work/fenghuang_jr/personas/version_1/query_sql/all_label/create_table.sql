use app;
drop table if exists personas_predict_label_full;
CREATE EXTERNAL TABLE personas_predict_label_full(
 user_id string COMMENT '用户id',
 age_label string  COMMENT '年龄分类',
 next_rate double COMMENT '预测下一次投资固收标的的利率',
 next_dealine int COMMENT '预测下一次投资固收标的的期限',
 invest_var_label string COMMENT '用户投资固收标的类型的稳定性分类',
 invest_recommend_bid_list string COMMENT '基于投资情况为用户推荐标的类型',
 show_invest_recommend_bid_list string COMMENT '基于投资情况为用户推荐标的类型(展示标签)',
 invest_recommend_user_list string COMMENT '基于投资情况为用户推荐关联度高的用户',
 view_recommend_bid_list string COMMENT '基于浏览情况为用户推荐标的类型',
 show_view_recommend_bid_list string COMMENT '基于浏览情况为用户推荐标的类型(展示标签)',
 view_recommend_user_list string COMMENT '基于浏览情况为用户推荐关联度高的用户'
)
COMMENT '用户画像所以预测标签'
PARTITIONED BY (dt string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n';

drop table if exists personas_predict_show_label_full;
CREATE EXTERNAL TABLE personas_predict_show_label_full(
 user_id string COMMENT '用户id',
 show_age_label string  COMMENT '展示年龄分类标签',
 show_invest_var_label string COMMENT '展示投资稳定性标签',
 show_next_rate string COMMENT '展示下一次投资利率标签',
 show_next_dealine string COMMENT '展示下一次投资期限标签',
 show_invest_recommend_bid_list string COMMENT '展示基于投资推荐标的标签',
 show_invest_recommend_user_list string COMMENT '展示基于投资推荐相关用户标签',
 show_view_recommend_bid_list string COMMENT '展示基于浏览推荐标的标签',
 show_view_recommend_user_list string COMMENT '展示基于浏览推荐相关用户标签'
 )
COMMENT '用户画像所以预测展示标签'
PARTITIONED BY (dt string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n';