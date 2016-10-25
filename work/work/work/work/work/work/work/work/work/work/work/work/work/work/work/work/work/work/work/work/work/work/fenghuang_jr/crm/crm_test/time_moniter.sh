#!/bin/sh
before_file=before_all_cycle_time.txt

before_time=`cat ${before_file}`
echo "执行时间监控程序"
if [ -z ${before_time} ]
then
        before_time='1970-01-01 00:00:00'
fi

start_date1=`date +%s -d "$before_time"`
#echo  ${start_date1}
start2=`date "+%Y-%m-%d 01:00:00"`
#echo "start2 " ${start2}
#echo "date +%s -d '${start2}'"
start_date2=`date +%s -d "${start2}"`
#echo ${start_date2}
#echo "expr ${start_date2} - ${start_date1}"
time_dif=`expr ${start_date2} - ${start_date1}`
diff=`expr ${time_dif} / 68400`
#echo "${diff}"
is_all=0

if [ ${diff} -gt 0 ]
then 
	echo "`date` process is  all  input"
	is_all=1
else
	echo "`date` process is append input"
fi

if [ ${is_all} -eq 1 ]
then
        echo "all" > cycle_all.txt
	echo ${start2} > ${before_file}
else
        echo "append" >cycle_all.txt
fi
