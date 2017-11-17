# -*- coding: utf-8 -*-
import re
from urllib import request
import datetime
import calendar
import xml.etree.cElementTree as ET
import mysql_ground
import re
import test

def last_month_day(year, month):
    current_data = datetime.datetime.now()
    if year == current_data.year and int(month) == current_data.month:
        return current_data.day - 1
    else:
        return calendar.monthrange(year, int(month))[1]

def tag_text_return(tag):
    try:
        tt = tag[0].text
    except:
        tt = 'N\A'

    return tt

def list_download():
    table = "lot_list"
    bid = 2
    pub_year_from = "2001"
    pub_year_to = datetime.datetime.today().strftime("%Y")
    #pub_month_from = (datetime.datetime.today() - datetime.timedelta(days=31)).strftime("%m")
    pub_month_to = datetime.datetime.today().strftime("%m")

    publish_from = pub_year_from + "0101T0000"
    publish_to = datetime.datetime(int(pub_year_to), int(pub_month_to), last_month_day(int(pub_year_to), int(pub_month_to))).strftime(
        "%Y%m%d") + "T2359"

    change_from = (datetime.datetime.today() - datetime.timedelta(days=15)).strftime("%Y%m") + "01T0000"
    change_to = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y%m%d") + "T2359"

    #print 'http://torgi.gov.ru/opendata/7710349494-torgi/data.xml?bidKind=%s&publishDateFrom=%s&publishDateTo=%s&lastChangeFrom=%s&lastChangeTo=%s' % (        bid, publish_from, publish_to, change_from, change_to)

    requestURL = 'http://torgi.gov.ru/opendata/7710349494-torgi/data.xml?bidKind=%s&publishDateFrom=%s&publishDateTo=%s&lastChangeFrom=%s&lastChangeTo=%s' % (
                bid, publish_from, publish_to, change_from, change_to)


    html = request.urlopen(requestURL)
    f = html.read()

    test.sql_csv(f)

    return

#    quant = len(re.findall("notification",f))
    print (re.findall("notification",f))
    count = 0

    csv = ET.parse(html)
    print (csv)
    root = csv.getroot()
    mysql_ground.ct_dp_tl() # очистка или создание таблицы

    for notification in root:

        # if count/quant == 0.25:
        #     print ('25%')
        # elif count/quant == 0.50:
        #     print ('50%')

        #for notification in tags('{http://torgi.gov.ru/opendata}notification'):
        lot_list = ({'bidKindId' : "'" + notification.find('{http://torgi.gov.ruu /opendata}bidKindId').text + "'",
                     'bidKindName' : "'" + notification.find('{http://torgi.gov.ru/opendata}bidKindName').text + "'",
                     'bidNumber' : "'" + notification.find('{http://torgi.gov.ru/opendata}bidNumber').text + "'",
                     'organizationName': "'" + notification.find('{http://torgi.gov.ru/opendata}organizationName').text + "'",
                     'isArchived': "'" + notification.find('{http://torgi.gov.ru/opendata}isArchived').text + "'",
                     'publishDate': "'" +  notification.find('{http://torgi.gov.ru/opendata}publishDate').text + "'",
                     'lastChanged': "'" + notification.find('{http://torgi.gov.ru/opendata}lastChanged').text + "'",
                     'odDetailedHref' : "'" + notification.find('{http://torgi.gov.ru/opendata}odDetailedHref').text + "'"})
        mysql_ground.db_data_add(table, lot_list)

if __name__ == "__main__":
    list_download()