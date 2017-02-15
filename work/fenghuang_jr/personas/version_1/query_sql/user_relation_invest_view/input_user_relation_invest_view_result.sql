use app;
load data local inpath '/root/personas_fengjr/model_data/user_relation_invest_view/bid_result.txt' overwrite into table personas_user_relation_invest_view_bid_label_full partition(dt='${dt}');
load data local inpath '/root/personas_fengjr/model_data/user_relation_invest_view/user_result.txt' overwrite  into table personas_user_relation_invest_view_user_label_full partition(dt='${dt}');