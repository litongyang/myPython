use app;
load data local inpath '/root/personas_fengjr/model_data/next_invest_bid/rate_result.txt' overwrite into table personas_next_invest_bid_label_full partition(dt='${dt}');