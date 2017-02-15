use app;
load data local inpath '/root/personas_fengjr/model_data/invest_var/result.txt' overwrite into table personas_user_invest_var_label_full partition(dt='${dt}');