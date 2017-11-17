#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql
import sys

def ct_dp_tl():

    try:
        con = pymysql.connect('localhost', 'root', '2272as8a2', 'ground')
        cur = con.cursor()
        #print (con.set_charset())
        with con:
            req = "DROP TABLE IF EXISTS lot_list"
            cur.execute(req)
            # AUTO_INCREMENT убрал из примера т.к. считаю, что это автонумерация
            req = "CREATE TABLE   lot_list(Id INT PRIMARY KEY AUTO_INCREMENT, \
                         bidKindId VARCHAR(2), bidKindName VARCHAR(255), bidNumber VARCHAR(100), \
                         organizationName VARCHAR(1000), isArchived VARCHAR(1), publishDate VARCHAR(25), \
                         lastChanged VARCHAR(25), odDetailedHref VARCHAR(255)) DEFAULT CHARACTER SET utf8"
            cur.execute(req)

    except pymysql.Error as e:
        print ("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        if cur:
            cur.close()


def db_data_add(table, data):

    try:
        con = pymysql.connect('localhost', 'root', '2272as8a2', 'ground')
        con.set_charset('utf8')
        cur = con.cursor()

        with con:
            req = "INSERT INTO %s (%s) VALUES(%s)" % (table, ",".join(data.keys()), ",".join(data.values()))
            cur.execute(req)

    except pymysql.Error as e:
        print ("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        if cur:
            cur.close()