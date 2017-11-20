#!/usr/bin/python

import pymysql
def sql_csv(data):
    sqlLoadData = 'LOAD DATA LOCAL INFILE "csv?%s" INTO TABLE tablename ' % data
    sqlLoadData += 'FIELDS TERMINATED BY "," LINES TERMINATED BY "\n"'
    sqlLoadData += 'IGNORE 1 LINES \n'
    sqlLoadData += 'ENCLOSED BY ' + '\"' + 'ESCAPED BY "\" '

    try:
        con = pymysql.connect('localhost', 'root', '2272as8a2', 'ground')
        curs = con.cursor()
        curs.execute(sqlLoadData)
        resultSet = curs.fetchall()
    except pymysql.Error as e:
        print (e)
        con.rollback()
        con.close()