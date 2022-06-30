# __author__ = 'tongyang.li'




import MySQLdb

try:
    conn=MySQLdb.connect(host='10.10.202.13', user='', passwd='', port=10000)
    cur=conn.cursor()
    sql = "select * from common.user_static limit 10"
    print sql
    cur.execute(sql)
    print cur.fetchAll()
    cur.close()
    conn.close()

except Exception, e:
     print Exception, e
