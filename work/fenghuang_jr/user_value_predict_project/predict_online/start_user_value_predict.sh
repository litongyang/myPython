#!/bin/sh
. /etc/profile
. ~/.bash_profile
exec_path=/root/user_value_predict/user_value_predict_project/predict_online
cd ${exec_path}
(
flock -w 3 200 
[ $? -eq 1 ] && { echo "same one is running ----------------" ; exit 1; }
python predict_result_online.py
)200<>./start_job.lock