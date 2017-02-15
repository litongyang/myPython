use app;
load data local inpath '/root/personas_fengjr/model_data/user_relation_invest/bid_result.txt' overwrite into table personas_user_relation_invest_bid_label_full partition(dt='${dt}');
load data local inpath '/root/personas_fengjr/model_data/user_relation_invest/user_result.txt' overwrite into table personas_user_relation_invest_user_label_full partition(dt='${dt}');