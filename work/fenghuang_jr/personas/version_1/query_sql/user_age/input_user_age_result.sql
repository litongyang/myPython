use app;
load data local inpath '/root/personas_fengjr/model_data/user_age/result.txt' overwrite into table personas_user_age_label_full partition(dt='${dt}');